#!/usr/bin/env python3
"""Analyze Bing AI Performance CSV exports without treating rolling deltas as causal."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit


class AuditError(ValueError):
    """Raised when an export cannot be interpreted safely."""


def clean_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = "".join(ch for ch in text if not unicodedata.category(ch).startswith("C"))
    return re.sub(r"\s+", " ", text).strip()


def normalize_header(value: str) -> str:
    text = unicodedata.normalize("NFKD", clean_text(value))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def parse_number(value: Any, *, percent: bool = False) -> float:
    text = clean_text(value).replace("%", "").replace("\u00a0", "")
    if not text:
        raise AuditError("valor numérico vazio")
    text = text.replace(" ", "")
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")
    try:
        result = float(text)
    except ValueError as exc:
        raise AuditError(f"valor numérico inválido: {value!r}") from exc
    return result / 100 if percent else result


def parse_date(value: str, date_order: str) -> datetime:
    text = clean_text(value)
    iso_formats = ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S")
    local_formats = (
        ("%d/%m/%Y", "%d/%m/%Y %H:%M:%S")
        if date_order == "day-first"
        else ("%m/%d/%Y", "%m/%d/%Y %H:%M:%S")
    )
    for fmt in (*iso_formats, *local_formats):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    raise AuditError(f"data inválida ou ambígua: {value!r}")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise AuditError(f"não foi possível ler {path}: {exc}") from exc
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise AuditError(f"encoding não reconhecido: {path}")
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    reader = csv.DictReader(text.splitlines(), dialect=dialect)
    if not reader.fieldnames:
        raise AuditError(f"CSV sem cabeçalho: {path}")
    return [dict(row) for row in reader]


def resolve_column(rows: list[dict[str, str]], aliases: Iterable[str], label: str) -> str:
    if not rows:
        raise AuditError(f"CSV sem linhas para localizar {label}")
    columns = {normalize_header(key): key for key in rows[0]}
    for alias in aliases:
        if normalize_header(alias) in columns:
            return columns[normalize_header(alias)]
    raise AuditError(f"coluna {label!r} ausente; encontradas: {', '.join(rows[0])}")


@dataclass(frozen=True)
class DailyMetric:
    date: str
    citations: int
    cited_pages: int | None


def load_overview(path: Path, date_order: str) -> list[DailyMetric]:
    rows = read_csv_rows(path)
    date_col = resolve_column(rows, ("Data", "Date"), "data")
    citation_col = resolve_column(rows, ("Citations", "Citacoes", "Citações"), "citações")
    pages_col = None
    try:
        pages_col = resolve_column(rows, ("Cited Pages", "Paginas citadas", "Páginas citadas"), "páginas citadas")
    except AuditError:
        pass
    seen: set[str] = set()
    result: list[DailyMetric] = []
    for index, row in enumerate(rows, start=2):
        day = parse_date(row.get(date_col, ""), date_order).date().isoformat()
        if day in seen:
            raise AuditError(f"data duplicada no Overview: {day} (linha {index})")
        seen.add(day)
        citations = int(parse_number(row.get(citation_col, "")))
        cited_pages = int(parse_number(row.get(pages_col, ""))) if pages_col and clean_text(row.get(pages_col, "")) else None
        result.append(DailyMetric(day, citations, cited_pages))
    if not result:
        raise AuditError("Overview sem dados")
    return sorted(result, key=lambda item: item.date)


def normalize_page(value: str) -> str:
    text = clean_text(value)
    parsed = urlsplit(text if "://" in text else f"https://example.invalid/{text.lstrip('/')}")
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/" and not path.endswith("/"):
        path += "/"
    return path.lower()


def load_pages(path: Path) -> list[dict[str, Any]]:
    rows = read_csv_rows(path)
    page_col = resolve_column(rows, ("Pagina", "Página", "Page", "URL"), "página")
    citation_col = resolve_column(rows, ("Citations", "Citacoes", "Citações"), "citações")
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        page = clean_text(row.get(page_col, ""))
        key = normalize_page(page)
        if not page or key in seen:
            if key in seen:
                raise AuditError(f"página duplicada: {key} (linha {index})")
            continue
        seen.add(key)
        result.append({"page": page, "key": key, "citations": int(parse_number(row.get(citation_col, "")))})
    return sorted(result, key=lambda item: (-item["citations"], item["key"]))


def load_queries(path: Path) -> tuple[list[dict[str, Any]], int]:
    rows = read_csv_rows(path)
    query_col = resolve_column(rows, ("Grounding Query", "Query", "Consulta"), "grounding query")
    citation_col = resolve_column(rows, ("Citations", "Citacoes", "Citações"), "citações")
    intent_col = resolve_column(rows, ("Intent", "Intencao", "Intenção"), "intent")
    topic_col = resolve_column(rows, ("Topic", "Topico", "Tópico"), "topic")
    share_col = resolve_column(rows, ("Citation Share", "Participacao de citacao", "Participação de citação"), "Citation Share")
    result: list[dict[str, Any]] = []
    skipped = 0
    for row in rows:
        query = clean_text(row.get(query_col, ""))
        if not query:
            skipped += 1
            continue
        share_text = clean_text(row.get(share_col, ""))
        result.append(
            {
                "query": query,
                "intent": clean_text(row.get(intent_col, "")),
                "topic": clean_text(row.get(topic_col, "")),
                "citations": int(parse_number(row.get(citation_col, ""))),
                "citation_share_pct": round(parse_number(share_text, percent=True) * 100, 2) if share_text else None,
            }
        )
    return sorted(result, key=lambda item: (-item["citations"], item["query"])), skipped


def pct_change(current: int, previous: int) -> float | None:
    if previous == 0:
        return None
    return round((current - previous) / previous * 100, 1)


def summarize_overview(rows: list[DailyMetric]) -> dict[str, Any]:
    citations = sum(row.citations for row in rows)
    last7 = sum(row.citations for row in rows[-7:])
    prior7 = sum(row.citations for row in rows[-14:-7]) if len(rows) >= 14 else None
    return {
        "start": rows[0].date,
        "end": rows[-1].date,
        "days": len(rows),
        "citations": citations,
        "average_per_returned_date": round(citations / len(rows), 1),
        "last_7_returned_dates": last7,
        "prior_7_returned_dates": prior7,
        "last7_vs_prior7_pct": pct_change(last7, prior7) if prior7 is not None else None,
        "max_cited_pages": max((row.cited_pages or 0) for row in rows),
    }


def compare_windows(current: list[DailyMetric], previous: list[DailyMetric]) -> dict[str, Any]:
    current_dates = {row.date for row in current}
    previous_dates = {row.date for row in previous}
    overlap = len(current_dates & previous_dates)
    current_total = sum(row.citations for row in current)
    previous_total = sum(row.citations for row in previous)
    return {
        "overlap_days": overlap,
        "current_overlap_pct": round(overlap / len(current_dates) * 100, 1),
        "previous_overlap_pct": round(overlap / len(previous_dates) * 100, 1),
        "comparison_type": "rolling_overlapping" if overlap else "non_overlapping",
        "current_total": current_total,
        "previous_total": previous_total,
        "delta": current_total - previous_total,
        "delta_pct": pct_change(current_total, previous_total),
    }


def compare_pages(current: list[dict[str, Any]], previous: list[dict[str, Any]]) -> list[dict[str, Any]]:
    current_map = {item["key"]: item for item in current}
    previous_map = {item["key"]: item for item in previous}
    result: list[dict[str, Any]] = []
    for key in sorted(current_map.keys() | previous_map.keys()):
        cur = current_map.get(key)
        prev = previous_map.get(key)
        if cur and prev:
            delta = cur["citations"] - prev["citations"]
            status = "increased" if delta > 0 else "decreased" if delta < 0 else "stable"
        elif cur:
            delta = None
            status = "not_returned_previous"
        else:
            delta = None
            status = "not_returned_current"
        result.append(
            {
                "key": key,
                "current_citations": cur["citations"] if cur else None,
                "previous_citations": prev["citations"] if prev else None,
                "delta": delta,
                "status": status,
            }
        )
    return result


def build_analysis(args: argparse.Namespace) -> dict[str, Any]:
    overview = load_overview(args.overview, args.date_order)
    pages = load_pages(args.pages) if args.pages else []
    queries, skipped_queries = load_queries(args.queries) if args.queries else ([], 0)
    summary = summarize_overview(overview)
    total = summary["citations"]
    page_sum = sum(item["citations"] for item in pages)
    query_sum = sum(item["citations"] for item in queries)
    top5_sum = sum(item["citations"] for item in pages[:5])
    analysis: dict[str, Any] = {
        "site_label": args.site_label,
        "overview": summary,
        "pages": {
            "rows": len(pages),
            "citation_sum": page_sum,
            "overview_difference": total - page_sum if pages else None,
            "top5_share_pct": round(top5_sum / total * 100, 1) if total and pages else None,
            "top": pages[: args.top],
        },
        "queries": {
            "rows": len(queries),
            "citation_sum": query_sum,
            "overview_difference": total - query_sum if queries else None,
            "skipped_unreadable_rows": skipped_queries,
            "top": queries[: args.top],
            "intent_counts": dict(Counter(item["intent"] or "Unclassified" for item in queries)),
            "topic_counts": dict(Counter(item["topic"] or "Unclassified" for item in queries)),
        },
        "comparison": None,
        "page_comparison": [],
    }
    if args.previous_overview:
        previous_overview = load_overview(args.previous_overview, args.date_order)
        analysis["comparison"] = compare_windows(overview, previous_overview)
    if args.previous_pages:
        if not pages:
            raise AuditError("--previous-pages exige --pages")
        previous_pages = load_pages(args.previous_pages)
        analysis["page_comparison"] = compare_pages(pages, previous_pages)
    return analysis


def fmt_int(value: int | None) -> str:
    return "n.a." if value is None else f"{value:,}".replace(",", ".")


def fmt_pct(value: float | None) -> str:
    return "n.a." if value is None or math.isnan(value) else f"{value:+.1f}%".replace(".", ",")


def md_cell(value: Any) -> str:
    return clean_text(value).replace("|", "\\|")


def render_markdown(analysis: dict[str, Any]) -> str:
    overview = analysis["overview"]
    lines = [
        "# Auditoria de visibilidade em IA",
        "",
        f"Propriedade: **{md_cell(analysis['site_label'])}**",
        "",
        "## Escopo",
        "",
        f"- Período real retornado: **{overview['start']} a {overview['end']}** ({overview['days']} datas).",
        f"- Citações no Overview: **{fmt_int(overview['citations'])}**.",
        f"- Média por data retornada: **{str(overview['average_per_returned_date']).replace('.', ',')}**.",
        f"- Últimas 7 datas: **{fmt_int(overview['last_7_returned_dates'])}**; variação vs 7 anteriores: **{fmt_pct(overview['last7_vs_prior7_pct'])}**.",
    ]
    comparison = analysis.get("comparison")
    if comparison:
        lines.extend(
            [
                "",
                "## Comparação de snapshots",
                "",
                f"- Tipo: **{'janelas móveis sobrepostas' if comparison['overlap_days'] else 'janelas não sobrepostas'}**.",
                f"- Sobreposição: **{comparison['overlap_days']} dias** ({str(comparison['current_overlap_pct']).replace('.', ',')}% da janela atual).",
                f"- Variação do total móvel: **{fmt_int(comparison['delta'])} ({fmt_pct(comparison['delta_pct'])})**.",
                "- Esse delta não representa citações líquidas adquiridas quando há sobreposição.",
            ]
        )
    pages = analysis["pages"]
    if pages["rows"]:
        lines.extend(
            [
                "",
                "## Páginas",
                "",
                f"O CSV retornou {pages['rows']} páginas e soma {fmt_int(pages['citation_sum'])} citações. Diferença para o Overview: {fmt_int(pages['overview_difference'])}. As cinco líderes representam {str(pages['top5_share_pct']).replace('.', ',')}% do Overview.",
                "",
                "| Página | Citações |",
                "|---|---:|",
            ]
        )
        lines.extend(f"| `{md_cell(item['key'])}` | {fmt_int(item['citations'])} |" for item in pages["top"])
    page_comparison = analysis.get("page_comparison", [])
    comparable = [item for item in page_comparison if item["delta"] is not None]
    if comparable:
        rising = sorted((item for item in comparable if item["delta"] > 0), key=lambda item: -item["delta"])[:5]
        falling = sorted((item for item in comparable if item["delta"] < 0), key=lambda item: item["delta"])[:5]
        lines.extend(["", "## Mudanças por página", ""])
        if rising:
            lines.append("Maiores altas entre URLs retornadas nos dois snapshots:")
            lines.append("")
            lines.extend(f"- `{md_cell(item['key'])}`: {fmt_int(item['delta'])}." for item in rising)
        if falling:
            lines.append("")
            lines.append("Maiores quedas entre URLs retornadas nos dois snapshots:")
            lines.append("")
            lines.extend(f"- `{md_cell(item['key'])}`: {fmt_int(item['delta'])}." for item in falling)
        absent_current = sum(item["status"] == "not_returned_current" for item in page_comparison)
        absent_previous = sum(item["status"] == "not_returned_previous" for item in page_comparison)
        lines.extend(
            [
                "",
                f"Não retornadas no atual: {absent_current}. Não retornadas no anterior: {absent_previous}. Esses estados não foram convertidos em zero.",
            ]
        )
    queries = analysis["queries"]
    if queries["rows"]:
        lines.extend(
            [
                "",
                "## Grounding queries",
                "",
                f"O CSV retornou {queries['rows']} consultas legíveis e soma {fmt_int(queries['citation_sum'])} citações. Diferença para o Overview: {fmt_int(queries['overview_difference'])}.",
                "",
                "| Consulta agrupada | Intent | Topic | Citações | Citation Share |",
                "|---|---|---|---:|---:|",
            ]
        )
        for item in queries["top"]:
            share = "n.a." if item["citation_share_pct"] is None else f"{item['citation_share_pct']:.2f}%".replace(".", ",")
            lines.append(
                f"| {md_cell(item['query'])} | {md_cell(item['intent'] or 'n.a.')} | {md_cell(item['topic'] or 'n.a.')} | {fmt_int(item['citations'])} | {share} |"
            )
    lines.extend(
        [
            "",
            "## Limitações",
            "",
            "- Citação não equivale a clique, sessão, conversão, ranking, backlink ou autoridade.",
            "- Totais de Overview, Pages e Grounding queries podem diferir por agregação e amostragem.",
            "- Linha ausente em um snapshot significa não retornada, não zero.",
            "- Grounding queries são frases agrupadas e podem não reproduzir o prompt completo.",
            "- Mudanças temporais são observacionais e não demonstram causalidade de uma edição.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overview", type=Path, required=True)
    parser.add_argument("--pages", type=Path)
    parser.add_argument("--queries", type=Path)
    parser.add_argument("--previous-overview", type=Path)
    parser.add_argument("--previous-pages", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--site-label", default="site analisado")
    parser.add_argument("--date-order", choices=("day-first", "month-first"), default="day-first")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args(argv)
    if args.top < 1:
        parser.error("--top deve ser maior que zero")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        analysis = build_analysis(args)
        report = render_markdown(analysis)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(report, encoding="utf-8")
        else:
            print(report)
        if args.json_output:
            args.json_output.parent.mkdir(parents=True, exist_ok=True)
            args.json_output.write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")
    except AuditError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
