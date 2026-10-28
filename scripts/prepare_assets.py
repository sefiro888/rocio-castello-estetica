# -*- coding: utf-8 -*-
"""Prepara imágenes y vídeos optimizados para la web a partir de _fuentes/.

    python scripts/prepare_assets.py
"""
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_fuentes"
IG = SRC / "instagram"
POSTS = IG / "posts"
OUT = ROOT / "assets" / "img"
VID = ROOT / "assets" / "video"
FF = r"C:\Users\sefir\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

# nombre: (origen, recorte vertical en fracciones (arriba, abajo))
FOTOS = {
    # cabeceras
    "hero-centro": ("posts/087.jpg", (0, 1)),
    "hero-faciales": ("posts/008.jpg", (0, 1)),
    "hero-tecnologia": ("posts/060.jpg", (0, .86)),
    "hero-tesla": ("posts/055.jpg", (.42, 1)),
    "hero-corporales": ("posts/026.jpg", (0, 1)),
    "hero-laser": ("posts/006.jpg", (.31, .9)),
    "hero-cera": ("posts/028.jpg", (0, 1)),
    "hero-pestanas": ("posts/093.jpg", (0, 1)),
    "hero-cejas": ("posts/074.jpg", (0, 1)),
    "hero-unas": ("posts/025.jpg", (0, 1)),
    "hero-rituales": ("posts/130.jpg", (0, 1)),
    "hero-cosmetica": ("posts/053.jpg", (0, 1)),
    "hero-resultados": ("posts/110.jpg", (0, 1)),
    "hero-regalo": ("posts/057.jpg", (0, 1)),
    "hero-tarifas": ("posts/092.jpg", (0, 1)),
    "hero-contacto": ("posts/122.jpg", (0, 1)),
    # marca y centro
    "rocio-sofa": ("posts/049.jpg", (0, 1)),
    "rocio-retrato": ("posts/103.jpg", (0, 1)),
    "rocio-estanteria": ("posts/053.jpg", (0, 1)),
    "rocio-promo": ("posts/012.jpg", (0, 1)),
    "rocio-bambu": ("posts/113.jpg", (0, 1)),
    "rocio-referente": ("posts/036.jpg", (0, 1)),
    "rocio-aniversario": ("posts/023.jpg", (0, .6)),
    "logo-dorado": ("posts/072.jpg", (0, 1)),
    "equipo": ("posts/102.jpg", (0, 1)),
    "equipo-navidad": ("posts/119.jpg", (0, 1)),
    "equipo-web": ("web-actual/estetica-rocio-castello-equipo.jpg", (0, 1)),
    "sala-espera": ("posts/087.jpg", (0, 1)),
    "cabina": ("posts/092.jpg", (0, 1)),
    "cabina-verde": ("posts/110.jpg", (0, 1)),
    "recepcion": ("posts/117.jpg", (0, 1)),
    "cafe": ("posts/094.jpg", (0, 1)),
    "velas": ("posts/080.jpg", (.3, 1)),
    "piedras": ("posts/142.jpg", (0, 1)),
    "fachada": ("posts/122.jpg", (0, 1)),
    "tarjetas-regalo": ("posts/057.jpg", (0, 1)),
    "tarjeta-mostrador": ("posts/123.jpg", (0, 1)),
    "regalo-madre": ("posts/032.jpg", (0, .54)),
    # faciales
    "facial-masaje": ("posts/016.jpg", (0, 1)),
    "facial-mascarilla": ("posts/125.jpg", (0, 1)),
    "facial-bn": ("posts/127.jpg", (0, 1)),
    "facial-equipo": ("posts/141.jpg", (0, 1)),
    "facial-symmed": ("posts/136.jpg", (0, 1)),
    "facial-lampara": ("posts/132.jpg", (0, 1)),
    "facial-pincel": ("posts/008.jpg", (0, 1)),
    "facial-led": ("web-actual/estetica-rocio-castello-facial-3.jpg", (0, 1)),
    "facial-diagnostico": ("instagram/Faciales/25.jpg", (.28, .88)),
    "facial-guasha": ("web-actual/estetica-rocio-castello-facial-gua-sha-e1679412627401.jpg", (0, 1)),
    "facial-kobido": ("instagram/Faciales/27.jpg", (0, 1)),
    "facial-cabina": ("posts/114.jpg", (0, 1)),
    "hydronature": ("posts/121.jpg", (.25, .78)),
    "symmed-sesion": ("posts/043.jpg", (0, .7)),
    "muse": ("posts/040.jpg", (0, 1)),
    "dermapen": ("posts/064.jpg", (0, 1)),
    # tecnología corporal
    "zionic-luz": ("posts/060.jpg", (0, .86)),
    "zionic-abdomen": ("posts/084.jpg", (0, 1)),
    "zionic-equipo": ("posts/035.jpg", (0, 1)),
    "zionic-crema": ("posts/021.jpg", (0, 1)),
    "ondas-choque": ("posts/031.jpg", (0, .72)),
    "tesla-cabina": ("posts/104.jpg", (0, 1)),
    "tesla-labios": ("posts/070.jpg", (0, 1)),
    "maderoterapia": ("posts/026.jpg", (0, 1)),
    "masaje-piernas": ("posts/024.jpg", (0, 1)),
    "lipodrenaje": ("posts/033.jpg", (0, 1)),
    "presoterapia": ("posts/105.jpg", (0, 1)),
    "masaje-espalda": ("posts/047.jpg", (0, 1)),
    "masaje-pinceles": ("posts/130.jpg", (0, 1)),
    "fisio": ("posts/100.jpg", (0, 1)),
    "fisio-facial": ("posts/088.jpg", (0, 1)),
    "masaje-navidad": ("posts/052.jpg", (0, .58)),
    "evo-sculpt": ("instagram/Corporales/12.jpg", (0, 1)),
    "geotermal": ("instagram/Corporales/13.jpg", (0, .8)),
    "ritual-web": ("web-actual/ritual-1.jpg", (0, 1)),
    "masaje-web": ("web-actual/estetica-rocio-castello-masajes-e1679421860613.jpg", (0, 1)),
    # depilación
    "laser-pierna": ("posts/006.jpg", (.31, .9)),
    "laser-equipo": ("instagram/Corporales/05.jpg", (0, .8)),
    "laser-web": ("web-actual/doctora-haciendo-depilacion-laser-piel-brazos-scaled.jpg", (0, 1)),
    "hilo": ("posts/039.jpg", (0, 1)),
    "cejas-web": ("web-actual/estetica-rocio-garcia-cejas.jpg", (0, 1)),
    "henna": ("instagram/Cejas/12.jpg", (0, .78)),
    # mirada
    "pestanas-ojo": ("posts/093.jpg", (0, 1)),
    "pestanas-lifting": ("posts/029.jpg", (0, 1)),
    "pestanas-aplicacion": ("posts/089.jpg", (0, 1)),
    "pestanas-rocio": ("posts/051.jpg", (0, 1)),
    "pestanas-web": ("web-actual/estetica-rocio-castello-pestanas-2.jpg", (0, 1)),
    "pestanas-web2": ("web-actual/251172778_1020464751861690_8864444108660611978_n.jpg", (0, 1)),
    "micro-labios": ("posts/004.jpg", (0, .58)),
    # uñas
    "unas-nude": ("posts/025.jpg", (0, 1)),
    "unas-verano": ("posts/013.jpg", (0, 1)),
    "unas-flores": ("posts/015.jpg", (0, 1)),
    "unas-francesa": ("posts/037.jpg", (0, 1)),
    "unas-rosa": ("posts/061.jpg", (0, 1)),
    "unas-babyboomer": ("posts/099.jpg", (0, 1)),
    "unas-corazones": ("posts/108.jpg", (0, 1)),
    "unas-rojo": ("posts/118.jpg", (0, 1)),
    "unas-oro": ("posts/126.jpg", (.25, .78)),
    "unas-esmaltes": ("posts/034.jpg", (0, 1)),
    "unas-web": ("web-actual/estetica-rocio-castello-manicura-2-scaled.jpg", (0, 1)),
    "unas-pies": ("posts/003.jpg", (.4, 1)),
    # cosmética
    "cosmetica-cofre": ("posts/077.jpg", (0, 1)),
    "cosmetica-ampollas": ("posts/048.jpg", (0, 1)),
    "cosmetica-eberlin": ("instagram/Faciales/01.jpg", (0, 1)),
    "cosmetica-casmara": ("instagram/Cosmética/06.jpg", (0, 1)),
    "cosmetica-mascarillas": ("posts/041.jpg", (0, 1)),
    "cosmetica-web": ("web-actual/estetica-rocio-castello-tratamientos.jpg", (0, 1)),
    # Facebook
    "fb-referentes": ("facebook/051.jpg", (0, 1)),
    "fb-referentes-2": ("facebook/050.jpg", (0, 1)),
    "fb-equipo": ("facebook/196.jpg", (0, 1)),
    "fb-equipo-2": ("facebook/132.jpg", (0, 1)),
    "fb-rocio-cejas": ("facebook/190.jpg", (0, 1)),
    "fb-rocio-mascarilla": ("facebook/060.jpg", (0, 1)),
    "fb-labios": ("facebook/184.jpg", (0, 1)),
    "fb-labios2": ("facebook/187.jpg", (0, 1)),
    "fb-micro-cejas": ("facebook/006.jpg", (0, 1)),
    "fb-serum": ("facebook/145.jpg", (0, 1)),
    "fb-crema": ("facebook/146.jpg", (0, 1)),
    "fb-ampolla": ("facebook/147.jpg", (0, 1)),
    "fb-gold": ("facebook/071.jpg", (0, 1)),
}

# antes / después (se muestran tal cual, son diseños del propio centro)
RESULTADOS = ["007", "014", "027", "042", "050", "059", "083", "090", "106", "111", "140",
              "071", "079", "063", "098", "133", "135", "097", "020", "018"]

# vídeos: nombre: (origen, inicio, duración, recorte_inferior)
VIDEOS = {
    "hero-facial": ("Faciales/18.mp4", 0.2, 9, 0),
    "hero-cabina": ("Faciales/20.mp4", 3.5, 9, 0),
    "hero-geotermal": ("Corporales/13.mp4", 1.5, 9, .2),
    "reel-kobido": ("Faciales/27.mp4", 0, 12, 0),
    "reel-zionic": ("Corporales/23.mp4", 2, 10, 0),
    "reel-unas": ("Manipedi/46.mp4", 0, 9, 0),
    "reel-henna": ("Cejas/12.mp4", 0, 12, 0),
    "reel-pestanas": ("Pestañas/75.mp4", 0, 11, 0),
    "reel-tesla": ("TESLA MED/03.mp4", 0, 12, 0),
    "reel-pinceles": ("Corporales/15.mp4", 0, 12, 0),
    "reel-limpieza": ("Faciales/34.mp4", 0, 7, 0),
}


# Cabeceras generadas con IA (sustituyen a la foto real sólo en la cabecera)
IA = {
    "hero-laser": "Tratamiento láser en clínica de lujo-1.png",
    "hero-tesla": "Tratamiento facial de lujo en clínica-2.png",
    "hero-pestanas": "Pestañas perfectas bajo luz dorada-3.png",
    "hero-cera": "Cejas perfectas en clínica de lujo-4.png",
    "hero-tecnologia": "Aplicador de radiofrecuencia con aro azul-5.png",
    "hero-tarifas": "Recepción de lujo al atardecer-6.png",
    "og": "Serenidad dorada en clínica estética-7.png",
    "hero-corporales": "Masaje con rodillo de madera-8.png",
}
UHD = ROOT / "_para-mejorar-UHD"


def uhd(nombre, original):
    """Usa la versión mejorada (superresolución) si existe en _para-mejorar-UHD/."""
    candidatos = [UHD / "imagenes-mejoradas" / "web-escritorio" / f"{nombre}.webp"]
    candidatos += [UHD / f"{nombre}{ext}" for ext in (".png", ".jpg", ".jpeg", ".webp")]
    for p in candidatos:
        if p.exists() and Image.open(p).width > Image.open(original).width:
            return p
    return original


def src_path(rel):
    if rel.startswith("posts/"):
        return POSTS / rel[6:]
    if rel.startswith("instagram/"):
        return IG / rel[10:]
    return SRC / rel


def guardar(im, destino, ancho):
    im = im.copy()
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    im.save(destino, "WEBP", quality=80, method=6)


def fotos():
    (OUT / "sm").mkdir(parents=True, exist_ok=True)
    for nombre, (rel, (a, b)) in FOTOS.items():
        if nombre in IA:
            continue
        im = ImageOps.exif_transpose(Image.open(uhd(nombre, src_path(rel)))).convert("RGB")
        if (a, b) != (0, 1):
            im = im.crop((0, round(im.height * a), im.width, round(im.height * b)))
        guardar(im, OUT / f"{nombre}.webp", 2000 if nombre.startswith("hero-") else 1500)
        guardar(im, OUT / "sm" / f"{nombre}.webp", 800)
    for nombre, archivo in IA.items():
        im = Image.open(SRC / "ia" / archivo).convert("RGB")
        guardar(im, OUT / f"{nombre}.webp", 2000)
        guardar(im, OUT / "sm" / f"{nombre}.webp", 800)
    (OUT / "resultados").mkdir(exist_ok=True)
    for n in RESULTADOS:
        im = Image.open(POSTS / f"{n}.jpg").convert("RGB")
        guardar(im, OUT / "resultados" / f"{n}.webp", 900)


def logo():
    """Extrae el monograma RC del logo sobre mármol y crea versiones con transparencia."""
    im = Image.open(next(SRC.parent.glob("Logo RC*.png"))).convert("L")
    rc = im.crop((440, 330, 830, 690))
    alpha = rc.point(lambda v: 255 if v < 95 else (0 if v > 165 else int((165 - v) * 255 / 70)))
    alpha = alpha.filter(ImageFilter.GaussianBlur(.6))
    alpha = alpha.crop(alpha.getbbox())
    for nombre, color in {"rc-tinta": (38, 34, 33), "rc-crema": (246, 239, 228), "rc-oro": (190, 152, 98)}.items():
        capa = Image.new("RGBA", alpha.size, color + (0,))
        capa.putalpha(alpha)
        capa.save(OUT / f"{nombre}.png", optimize=True)
    # favicon / icono
    ico = Image.new("RGBA", (512, 512), (246, 239, 228, 255))
    m = Image.new("RGBA", alpha.size, (38, 34, 33, 0))
    m.putalpha(alpha)
    m.thumbnail((330, 330), Image.LANCZOS)
    ico.alpha_composite(m, ((512 - m.width) // 2, (512 - m.height) // 2))
    ico.save(OUT / "icono-512.png")
    ico.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png")
    ico.resize((48, 48), Image.LANCZOS).save(ROOT / "favicon.ico")
    # textura de mármol para fondos
    marmol = Image.open(next(SRC.parent.glob("Logo RC*.png"))).convert("RGB").crop((0, 900, 1254, 1254))
    marmol.save(OUT / "marmol.webp", "WEBP", quality=72)


def videos():
    VID.mkdir(parents=True, exist_ok=True)
    for nombre, (rel, ini, dur, recorte) in VIDEOS.items():
        origen = IG / rel
        vf = "scale=540:-2"
        if recorte:
            vf = f"crop=iw:ih*{1 - recorte}:0:0,scale=540:-2"
        subprocess.run([FF, "-loglevel", "error", "-y", "-ss", str(ini), "-t", str(dur), "-i", str(origen),
                        "-an", "-vf", vf + ",fps=30", "-c:v", "libx264", "-crf", "27", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(VID / f"{nombre}.mp4")], check=True)
        subprocess.run([FF, "-loglevel", "error", "-y", "-i", str(VID / f"{nombre}.mp4"), "-frames:v", "1",
                        "-q:v", "4", str(VID / f"{nombre}.jpg")], check=True)
        Image.open(VID / f"{nombre}.jpg").save(VID / f"{nombre}.webp", "WEBP", quality=72)
        (VID / f"{nombre}.jpg").unlink()


if __name__ == "__main__":
    import sys
    pasos = sys.argv[1:] or ["logo", "fotos", "videos"]
    for paso in pasos:
        globals()[paso]()
    print("ok")
