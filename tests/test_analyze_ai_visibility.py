import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ai-visibility-audit" / "scripts" / "analyze_ai_visibility.py"


class AnalyzeAiVisibilityTest(unittest.TestCase):
    def test_example_exports_generate_expected_totals(self):
        example = ROOT / "examples" / "bing-ai-export-example"
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "report.md"
            json_output = Path(temporary) / "report.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--overview",
                    str(example / "overview.csv"),
                    "--pages",
                    str(example / "pages.csv"),
                    "--queries",
                    str(example / "queries.csv"),
                    "--output",
                    str(output),
                    "--json-output",
                    str(json_output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(json_output.read_text(encoding="utf-8"))
            self.assertEqual(data["overview"]["citations"], 1990)
            self.assertEqual(data["overview"]["days"], 14)
            self.assertEqual(data["pages"]["citation_sum"], 1775)
            report = output.read_text(encoding="utf-8")
            self.assertIn("Grounding queries", report)
            self.assertIn("Linha ausente", report)

    def test_overlap_and_absent_page_are_not_treated_as_zero(self):
        spec = importlib.util.spec_from_file_location("audit", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        current = [module.DailyMetric(f"2026-09-{day:02d}", 10, 1) for day in range(10, 20)]
        previous = [module.DailyMetric(f"2026-09-{day:02d}", 8, 1) for day in range(5, 15)]
        comparison = module.compare_windows(current, previous)
        self.assertEqual(comparison["overlap_days"], 5)
        self.assertEqual(comparison["comparison_type"], "rolling_overlapping")
        pages = module.compare_pages(
            [{"key": "/nova/", "citations": 20}],
            [{"key": "/antiga/", "citations": 30}],
        )
        statuses = {item["key"]: item for item in pages}
        self.assertIsNone(statuses["/nova/"]["previous_citations"])
        self.assertIsNone(statuses["/nova/"]["delta"])
        self.assertEqual(statuses["/antiga/"]["status"], "not_returned_current")

    def test_empty_citation_share_remains_unavailable(self):
        spec = importlib.util.spec_from_file_location("audit_empty_share", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "queries.csv"
            path.write_text(
                "Grounding Query,Intent,Topic,Citations,Citation Share\n"
                "consulta de teste,Research,Technology,12,\n",
                encoding="utf-8",
            )
            rows, skipped = module.load_queries(path)
        self.assertEqual(skipped, 0)
        self.assertIsNone(rows[0]["citation_share_pct"])


if __name__ == "__main__":
    unittest.main()
