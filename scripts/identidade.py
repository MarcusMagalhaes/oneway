"""Gera as imagens do site a partir da arte original da One Way (docs/marca/oneway-logo-original.jpg).

Uso: python3 scripts/identidade.py

Tira o fundo claro da arte (transparência) e recorta:
  public/img/oneway-simbolo.png   símbolo completo (esfera, pixels e circuitos)
  public/img/oneway-nome.png      "ONE WAY"
  public/img/oneway-logo.png      arte completa sem fundo
  public/favicon.png, public/apple-touch-icon.png, public/icon-512.png   só a esfera
  public/img/og-oneway.jpg        imagem de compartilhamento 1200x630
"""
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGINAL = RAIZ / "docs/marca/oneway-logo-original.jpg"
PUBLIC = RAIZ / "public"


def sem_fundo(img: Image.Image) -> Image.Image:
    """Fundo branco/cinza-claro vira transparente, com borda suave."""
    img = img.convert("RGBA")
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            claro = min(r, g, b)
            satur = max(r, g, b) - claro
            if satur > 40:          # laranja: sempre opaco
                a = 255
            elif claro >= 236:
                a = 0
            elif claro <= 190:
                a = 255
            else:
                a = int((236 - claro) * 255 / 46)
            px[x, y] = (r, g, b, a)
    return img


def aparar(img: Image.Image, margem: int = 6) -> Image.Image:
    caixa = img.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox()
    x0, y0, x1, y1 = caixa
    return img.crop((max(0, x0 - margem), max(0, y0 - margem),
                     min(img.width, x1 + margem), min(img.height, y1 + margem)))


def quadrado(img: Image.Image, lado: int, fundo=None, folga: float = 0.08) -> Image.Image:
    base = Image.new("RGBA", (lado, lado), fundo or (0, 0, 0, 0))
    util = int(lado * (1 - 2 * folga))
    copia = img.copy()
    copia.thumbnail((util, util), Image.LANCZOS)
    base.alpha_composite(copia, ((lado - copia.width) // 2, (lado - copia.height) // 2))
    return base


def main() -> None:
    (PUBLIC / "img").mkdir(parents=True, exist_ok=True)
    arte = Image.open(ORIGINAL).convert("RGB")
    limpa = sem_fundo(arte)

    simbolo = aparar(limpa.crop((340, 70, 980, 494)))
    simbolo.save(PUBLIC / "img/oneway-simbolo.png", optimize=True)

    esfera = aparar(limpa.crop((600, 70, 980, 494)))

    nome = aparar(limpa.crop((90, 530, 1440, 705)))
    nome.thumbnail((900, 200), Image.LANCZOS)
    nome.save(PUBLIC / "img/oneway-nome.png", optimize=True)

    logo = aparar(limpa)
    logo.thumbnail((1200, 1200), Image.LANCZOS)
    logo.save(PUBLIC / "img/oneway-logo.png", optimize=True)

    quadrado(esfera, 64, folga=0.02).save(PUBLIC / "favicon.png", optimize=True)
    quadrado(esfera, 512, folga=0.06).save(PUBLIC / "icon-512.png", optimize=True)
    quadrado(esfera, 180, fundo=(255, 255, 255, 255), folga=0.12).convert("RGB").save(PUBLIC / "apple-touch-icon.png", optimize=True)

    og = Image.new("RGB", (1200, 630), (255, 255, 255))
    copia = arte.copy()
    copia.thumbnail((1200, 630), Image.LANCZOS)
    og.paste(copia, ((1200 - copia.width) // 2, (630 - copia.height) // 2))
    og.save(PUBLIC / "img/og-oneway.jpg", quality=88)

    for f in sorted((PUBLIC).rglob("*.png")) + [PUBLIC / "img/og-oneway.jpg"]:
        print(f.relative_to(RAIZ), Image.open(f).size, f.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
