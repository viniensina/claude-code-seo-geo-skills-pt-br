#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cover-image — gera capa 1200x675 para post do WordPress.
Uso:
  python gerar_capa.py --post-id 1923 --query "advertising metrics screen dark" --pill "IA Marketing"
  python gerar_capa.py --title "Meu Artigo" --pill "Meta Ads" --query "facebook ads dashboard laptop"

Credenciais vêm do ambiente (ver .env.example na raiz do repo):
  WP_URL, WP_USER, WP_APP_PASSWORD, UNSPLASH_KEY
"""

import argparse, base64, io, os, sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, errors="replace")

import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Carrega o .env (raiz do repo e/ou diretório atual) se python-dotenv estiver
# instalado. Sem ele, o script ainda funciona com as variáveis já exportadas
# no ambiente.
try:
    from pathlib import Path
    from dotenv import load_dotenv
    _repo_env = Path(__file__).resolve().parents[3] / ".env"
    if _repo_env.exists():
        load_dotenv(_repo_env)
    load_dotenv()  # também tenta o .env do diretório onde você rodou o comando
except ImportError:
    pass

# --- Config via ambiente (nunca hardcodar segredo) ---
WP_URL       = os.environ.get("WP_URL")
WP_USER      = os.environ.get("WP_USER")
WP_PASSWORD  = os.environ.get("WP_APP_PASSWORD")
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY")

# Paleta do overlay — troque pelas cores do seu site
W, H = 1200, 675
PURPLE    = (124, 58, 237)
PURPLE_LT = (167, 139, 250)
WHITE     = (241, 241, 245)
MUTED     = (180, 180, 200)
# Fontes: default escolhido por SO; sobrescreva com COVER_FONT_BOLD / COVER_FONT_REG.
# Se a fonte não existir, o script cai na fonte padrão do PIL (com aviso — ver font()).
def _default_fonts():
    if sys.platform.startswith("win"):
        return "C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"
    if sys.platform == "darwin":
        return ("/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                "/System/Library/Fonts/Supplemental/Arial.ttf")
    # Linux e outros
    return ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")

_DEF_BOLD, _DEF_REG = _default_fonts()
FONT_BOLD = os.environ.get("COVER_FONT_BOLD", _DEF_BOLD)
FONT_REG  = os.environ.get("COVER_FONT_REG", _DEF_REG)

def wp_auth():
    if not WP_URL or not WP_USER or not WP_PASSWORD:
        print("Erro: defina WP_URL, WP_USER e WP_APP_PASSWORD no ambiente (.env)."); sys.exit(1)
    token = base64.b64encode(f"{WP_USER}:{WP_PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}"}

_font_warned = False
def font(path, size):
    global _font_warned
    try:
        return ImageFont.truetype(path, size)
    except (OSError, IOError):
        if not _font_warned:
            print(f"Aviso: fonte '{path}' não encontrada. Usando a fonte padrão do PIL — "
                  f"a capa fica com texto pequeno. Defina COVER_FONT_BOLD / COVER_FONT_REG "
                  f"apontando para uma .ttf do seu sistema.")
            _font_warned = True
        return ImageFont.load_default()

def wrap_text(text, f, max_w):
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        if f.getbbox(test)[2] <= max_w: line = test
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    return lines

def fetch_photo(query, index=0):
    if not UNSPLASH_KEY:
        print("Erro: defina UNSPLASH_KEY no ambiente (.env)."); sys.exit(1)
    r = requests.get("https://api.unsplash.com/search/photos",
        headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"},
        params={"query": query, "orientation": "landscape", "per_page": 10}, timeout=10)
    if r.status_code in (401, 403):
        print(f"Erro Unsplash: {r.status_code} — chave inválida ou sem permissão. Confira UNSPLASH_KEY."); sys.exit(1)
    if r.status_code != 200:
        print(f"Erro Unsplash: {r.status_code} {r.text[:200]}"); sys.exit(1)
    results = r.json().get("results", [])
    if not results:
        return None, None, None
    i = min(index, len(results)-1)
    res = results[i]
    photo_url = res["urls"]["regular"]
    desc = (res.get("description") or res.get("alt_description") or "")[:60]
    user = res["user"]["username"]
    img = Image.open(io.BytesIO(requests.get(photo_url, timeout=15).content)).convert("RGB")
    return img, desc, user

def make_cover(photo, title, pill, subtitle=None):
    pw, ph = photo.size
    ratio = W / H
    if pw/ph > ratio:
        nw = int(ph * ratio); off = (pw-nw)//2
        photo = photo.crop((off, 0, off+nw, ph))
    else:
        nh = int(pw/ratio); off = (ph-nh)//3
        photo = photo.crop((0, off, pw, off+nh))
    photo = photo.resize((W, H), Image.LANCZOS)
    photo = ImageEnhance.Brightness(photo).enhance(0.50)
    photo = ImageEnhance.Contrast(photo).enhance(1.1)
    base = photo.convert("RGBA")

    # Overlay gradiente esq→dir
    ov = Image.new("RGBA", (W, H), (0,0,0,0))
    od = ImageDraw.Draw(ov)
    for x in range(W):
        if x < 500: alpha = 225
        elif x < 900: alpha = int(225*(1-(x-500)/400))
        else: alpha = 0
        od.line([(x,0),(x,H)], fill=(5,5,15,alpha))
    # Toque roxo no rodapé esq
    for x in range(500):
        for y in range(H-160, H):
            blend = int(30*(1-x/500)*((y-(H-160))/160))
            if blend > 0: od.point((x,y), fill=(*PURPLE, blend))
    base = Image.alpha_composite(base, ov)
    draw = ImageDraw.Draw(base)

    # Barra roxa topo
    draw.rectangle([0,0,W,4], fill=(*PURPLE,255))

    # Pill badge
    ft = font(FONT_BOLD, 15)
    pill_up = pill.upper()
    bbox = ft.getbbox(pill_up)
    tw = bbox[2]-bbox[0]
    draw.rounded_rectangle([68,58, 68+tw+32, 58+bbox[3]-bbox[1]+18],
        radius=100, fill=(*PURPLE,50), outline=(*PURPLE_LT,130), width=1)
    draw.text((84,67), pill_up, font=ft, fill=PURPLE_LT)
    pill_bottom = 58+bbox[3]-bbox[1]+18+20

    # Título
    tf = None
    for size in [58,46,38]:
        f = font(FONT_BOLD, size)
        lines = wrap_text(title, f, 630)
        if len(lines) <= 3: tf = f; break
    if not tf: tf = font(FONT_BOLD,38); lines = wrap_text(title, tf, 630)

    y = pill_bottom + 10
    for line in lines[:3]:
        draw.text((68,y), line, font=tf, fill=WHITE)
        y += tf.getbbox(line)[3] - tf.getbbox(line)[1] + 10

    # Subtítulo — troque pelo seu domínio
    sub = subtitle or "seusite.com"
    draw.text((68, y+12), sub, font=font(FONT_REG,22), fill=MUTED)

    # Linha decorativa vertical
    draw.rectangle([48, pill_bottom-4, 52, y+12], fill=PURPLE)

    # Branding — troque pelo seu domínio
    bf = font(FONT_BOLD,20)
    br = os.environ.get("COVER_BRAND", "seusite.com")
    bw = bf.getbbox(br)[2]
    draw.ellipse([W-bw-36, H-38, W-bw-30, H-32], fill=PURPLE_LT)
    draw.text((W-bw-22, H-42), br, font=bf, fill=(*MUTED,220))

    return base.convert("RGB")

def upload_and_set(img, filename, post_id):
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=92)
    buf.seek(0)
    r = requests.post(f"{WP_URL}/wp-json/wp/v2/media",
        headers={**wp_auth(),
                 "Content-Disposition": f'attachment; filename="{filename}"',
                 "Content-Type": "image/jpeg"},
        data=buf.read())
    if r.status_code not in (200,201):
        print(f"Erro upload: {r.status_code} {r.text[:200]}")
        return
    body = r.json()
    media_id = body.get("id")
    if not media_id:
        print(f"Erro upload: resposta sem 'id' — {str(body)[:200]}")
        return
    media_url = body.get("source_url","")
    print(f"Upload OK — Media ID: {media_id}")
    print(f"URL: {media_url}")

    if post_id:
        r2 = requests.post(f"{WP_URL}/wp-json/wp/v2/posts/{post_id}",
            headers={**wp_auth(), "Content-Type": "application/json"},
            json={"featured_media": media_id})
        if r2.status_code == 200:
            print(f"Featured image definida no post {post_id}")
        else:
            print(f"Erro ao setar featured: {r2.status_code}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--post-id", type=int)
    parser.add_argument("--title")
    parser.add_argument("--pill", default="Blog")
    parser.add_argument("--query", required=True)
    parser.add_argument("--subtitle")
    parser.add_argument("--photo-index", type=int, default=0)
    parser.add_argument("--no-upload", action="store_true")
    args = parser.parse_args()

    # Buscar título do WP se só tiver post-id
    title = args.title
    if not title and args.post_id:
        import html as html_lib, re
        r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts/{args.post_id}",
            headers=wp_auth(), params={"context":"edit"})
        if r.status_code != 200:
            print(f"Erro ao buscar post {args.post_id}: {r.status_code} {r.text[:200]}"); sys.exit(1)
        raw = r.json().get("title", {}).get("raw")
        if not raw:
            print(f"Erro: post {args.post_id} sem título 'raw' (use context=edit e um usuário com permissão de edição)."); sys.exit(1)
        title = re.sub(r"<[^>]+>","", html_lib.unescape(raw))
        print(f"Título do post: {title}")

    if not title:
        print("Erro: informe --title ou --post-id"); sys.exit(1)

    print(f"Buscando foto: '{args.query}' (index {args.photo_index})...")
    photo, desc, user = fetch_photo(args.query, args.photo_index)
    if not photo:
        print("Sem resultados para essa query."); sys.exit(1)
    print(f"Foto: @{user} — {desc}")

    img = make_cover(photo, title, args.pill, args.subtitle)

    slug = title.lower()[:40].replace(" ","-").replace("/","-")
    import re; slug = re.sub(r"[^a-z0-9\-]","",slug)
    filename = f"cover-{slug}.jpg"
    img.save(filename, "JPEG", quality=92)
    print(f"Salvo: {filename}")

    if not args.no_upload:
        upload_and_set(img, filename, args.post_id)

if __name__ == "__main__":
    main()
