#!/usr/bin/env python3
"""Logo, favicons et image de partage de Jolies Pieces.
Source du logo : logo-source.png (logo fait par Charlie le 2026-09-25, Anton noir sur deux lignes),
vectorise par potrace en logo-trace.svg, decline dans static/images/logo-jolies-pieces*.svg.
Usage : cd brand && python3 make_brand.py"""
from PIL import Image, ImageDraw, ImageFont
import os
OUT = "../static/images"
PAGE, PEARL, INK, WHITE = (244, 243, 241), (221, 217, 213), (47, 43, 41), (255, 255, 255)

src = Image.open("logo-source.png").convert("RGBA")
bg = Image.new("RGBA", src.size, "white"); bg.alpha_composite(src)
mask = bg.convert("L").point(lambda v: 255 if v < 128 else 0)
mask = mask.crop(mask.getbbox())

def logo_on(size, fg, back, pad=.16):
    im = Image.new("RGB", (size, size), back)
    inner = int(size * (1 - 2 * pad))
    m = mask.copy(); m.thumbnail((inner, inner), Image.LANCZOS)
    im.paste(Image.new("RGB", m.size, fg), ((size - m.width) // 2, (size - m.height) // 2), m)
    return im

for s, name in [(512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png"), (48, "favicon-48.png")]:
    logo_on(s, PAGE, INK, .14).save(os.path.join(OUT, name))
logo_on(64, PAGE, INK, .1).save("../static/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
# favicon SVG : logo clair sur carre encre
logo = open(os.path.join(OUT, "logo-jolies-pieces-blanc.svg")).read()
inner = logo[logo.index("<g "):logo.index("</svg>")].replace("#FFFFFF", "#F4F3F1")
open(os.path.join(OUT, "favicon.svg"), "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-200 -250 1894 1842"><rect x="-200" y="-250" width="1894" height="1842" fill="#2F2B29"/>'
    + inner + '</svg>\n')
# logo carre pour Organization.logo (fond clair)
logo_on(600, INK, PAGE, .14).save(os.path.join(OUT, "logo-jolies-pieces-carre.png"))

# og:image 1200x630 : photo du hero a droite, logo a gauche sur papier
W, H = 1200, 630
og = Image.new("RGB", (W, H), PAGE)
hero = Image.open("../static/images/visuels/hero.webp").convert("RGB")
ph = hero.resize((int(hero.width * H / hero.height), H)).crop((0, 0, 640, H))
x0 = int(hero.width * H / hero.height) // 2 - 320
ph = hero.resize((int(hero.width * H / hero.height), H)).crop((x0 + 80, 0, x0 + 720, H))
og.paste(ph, (W - 640, 0))
m = mask.copy(); m.thumbnail((440, 400), Image.LANCZOS)
og.paste(Image.new("RGB", m.size, INK), ((W - 640 - m.width) // 2, (H - m.height) // 2 - 30), m)
d = ImageDraw.Draw(og)
d.text(((W - 640) // 2, (H + m.height) // 2 + 20), "le magazine des créateurs", font=ImageFont.truetype("yellowtail.ttf", 40), fill=(138, 131, 126), anchor="mt")
og.save(os.path.join(OUT, "og-jolies-pieces.jpg"), quality=86)
print("ok")
