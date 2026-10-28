# -*- coding: utf-8 -*-
"""Genera la web estática de Rocío Castelló Estética Avanzada.

    python scripts/prepare_assets.py   # (solo si cambian fotos, vídeos o logo)
    python build.py
"""
import json
import sys
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from content import (NEGOCIO as N, CENTROS, HORARIO, HORARIO_VERANO, CINTA, RESENAS,  # noqa: E402
                     IG_DESTACADOS, IG_POSTS, REELS, SERVICIOS, SERV, GRUPOS, QUIZ, COMPARA, EQUIPO)
from detalle import DETALLE  # noqa: E402

VERSION = "10"
BASE = "https://sefiro888.github.io/rocio-castello-estetica/"
e = escape
POSTS_META = json.loads((ROOT / "_fuentes" / "instagram" / "posts" / "meta.json").read_text(encoding="utf-8"))
SANTO, MURCIA = CENTROS


def ig_post(num):
    return "https://www.instagram.com" + POSTS_META[f"posts/{num}.jpg"]["code"]


def wa(numero, texto):
    return f"https://wa.me/{numero}?text={quote(texto)}"


def img(nombre, sm=False):
    return f"assets/img/{'sm/' if sm else ''}{nombre}.webp"


def foto(nombre, alt="", cls="", sm=True, eager=False):
    carga = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img class="{cls}" src="{img(nombre, sm)}" srcset="{img(nombre, True)} 720w, {img(nombre)} 1500w" '
            f'sizes="(max-width: 800px) 100vw, 50vw" alt="{e(alt)}" {carga} decoding="async">')


ICONOS = {
    "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z" fill="currentColor"/>',
    "tel": '<path d="M6.6 10.8a15.2 15.2 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.2 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .6 3.6 1 1 0 0 1-.3 1Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>',
    "pin": '<path d="M12 21s-7-7.2-7-12a7 7 0 0 1 14 0c0 4.8-7 12-7 12Z" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="12" cy="9" r="2.5" fill="none" stroke="currentColor" stroke-width="1.5"/>',
    "reloj": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    "ig": '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="17.5" cy="6.5" r="1.1" fill="currentColor"/>',
    "fb": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8.5a.5.5 0 0 1 .5-.5Z" fill="currentColor"/>',
    "flecha": '<path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>',
    "estrella": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9Z" fill="currentColor"/>',
    "mas": '<path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    "x": '<path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    "play": '<path d="M8 5.5v13l11-6.5Z" fill="currentColor"/>',
    "chev": '<path d="m9 6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "chevi": '<path d="m15 6-6 6 6 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "buscar": '<circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m16 16 4.5 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    "regalo": '<rect x="3.5" y="8.5" width="17" height="4" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M5 12.5V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7.5M12 8.5V21M12 8.5S10.5 3.5 8 4.2C6 4.8 7 8.5 12 8.5Zm0 0s1.5-5 4-4.3c2 .6 1 4.3-4 4.3Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>',
    "chispa": '<path d="M12 2.5c.6 4.6 2.9 6.9 7.5 7.5-4.6.6-6.9 2.9-7.5 7.5-.6-4.6-2.9-6.9-7.5-7.5 4.6-.6 6.9-2.9 7.5-7.5Z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/>',
    "check": '<path d="m5 12.5 4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "sonido": '<path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
}


def ico(n, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONOS[n]}</svg>'


def logo(cls="logo", tono="tinta"):
    return (f'<a class="{cls}" href="index.html" aria-label="Rocío Castelló Estética Avanzada, inicio">'
            f'<img class="logo-rc" src="assets/img/rc-{tono}.png" alt="" width="44" height="40">'
            '<span class="logo-txt"><span class="logo-nombre">Rocío Castelló</span>'
            '<span class="logo-sub">Estética Avanzada</span></span></a>')


def sello(texto="Rocío Castelló · Estética Avanzada · Santomera · Murcia · "):
    """Sello circular con texto girando alrededor del monograma."""
    return ('<div class="sello" aria-hidden="true"><svg viewBox="0 0 200 200"><defs>'
            '<path id="circ" d="M100 100m-78 0a78 78 0 1 1 156 0a78 78 0 1 1-156 0"/></defs>'
            f'<text><textPath href="#circ">{e(texto * 2)}</textPath></text></svg>'
            '<img src="assets/img/rc-oro.png" alt=""></div>')


def estrellas(n=5):
    return '<span class="estrellas" aria-label="5 de 5">' + ico("estrella") * n + "</span>"


# ------------------------------------------------------------------ estructura común
def head(titulo, desc, pagina, pre=""):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#f4ede2">
<link rel="canonical" href="{BASE}{'' if pagina == 'inicio' else pagina + '.html'}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rocío Castelló · Estética Avanzada">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{BASE}{'' if pagina == 'inicio' else pagina + '.html'}">
<meta property="og:image" content="{BASE}assets/img/og-logo.jpg">
<meta property="og:image:secure_url" content="{BASE}assets/img/og-logo.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Logotipo de Rocío Castelló Estética Avanzada sobre mármol crema">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(titulo)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{BASE}assets/img/og-logo.jpg">
<link rel="icon" href="favicon.ico">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Jost:wght@300;400;500&family=Pinyon+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css?v={VERSION}">
<script>document.documentElement.classList.add("anim")</script>
{pre}
</head>
<body data-pagina="{pagina}">
<a class="saltar" href="#main">Saltar al contenido</a>
"""


def cinta_superior():
    items = [f"Diagnóstico facial gratuito", f"Santomera · {SANTO['tel']}", f"Murcia · {MURCIA['tel']}",
             "Lunes a viernes de 9:00 a 21:00", f"{N['rating']} ★ en Google", "Tarjetas regalo personalizadas"]
    fila = "".join(f"<span>{e(t)}</span><i>✦</i>" for t in items)
    return f'<div class="cinta-top" aria-label="Información rápida"><div class="cinta-pista">{fila}{fila}</div></div>'


def menu():
    cols = ""
    for g in GRUPOS:
        links = "".join(
            f'<a href="{s["slug"]}.html" data-img="{img(s["hero"], True)}"><span>{e(s["menu"])}</span>{ico("flecha")}</a>'
            for s in SERVICIOS if s["grupo"] == g)
        cols += f'<div class="mega-col"><p class="mega-h">{e(g)}</p>{links}</div>'
    return f"""
<header class="cab" id="cab">
  {cinta_superior()}
  <div class="cab-in">
    {logo()}
    <nav class="nav" aria-label="Principal">
      <a href="centro.html" data-nav="centro">El centro</a>
      <div class="nav-mega">
        <button class="nav-btn" aria-expanded="false" aria-controls="mega">Tratamientos <span class="nav-plus">{ico('mas')}</span></button>
        <div class="mega" id="mega">
          <div class="mega-in">
            <div class="mega-cols">{cols}</div>
            <a class="mega-card" href="tesla-med.html">
              <span class="mega-img"><img src="{img('hero-tesla', True)}" alt="" loading="lazy" data-def="{img('hero-tesla', True)}"></span>
              <span class="mega-card-txt"><small>Exclusivo</small><strong>Tesla Med</strong><em>Dos patentes mundiales. Cero agujas.</em></span>
            </a>
          </div>
        </div>
      </div>
      <a href="tecnologia.html" data-nav="tecnologia">Tecnología</a>
      <a href="resultados.html" data-nav="resultados">Resultados</a>
      <a href="tarifas.html" data-nav="tarifas">Tarifas</a>
      <a href="tarjeta-regalo.html" data-nav="tarjeta-regalo">Regala</a>
      <a href="contacto.html" data-nav="contacto">Contacto</a>
    </nav>
    <div class="cab-acc">
      <a class="cab-ig" href="{N['instagram']}" target="_blank" rel="noopener" aria-label="Instagram">{ico('ig')}</a>
      <button class="btn btn-tinta btn-sm" data-reserva>Reservar cita</button>
      <button class="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="movil"><span></span><span></span></button>
    </div>
  </div>
</header>
{menu_movil()}
"""


def menu_movil():
    grupos = ""
    for g in GRUPOS:
        links = "".join(f'<a href="{s["slug"]}.html"><em>{s["num"]}</em>{e(s["menu"])}</a>' for s in SERVICIOS if s["grupo"] == g)
        grupos += f'<details class="mov-g"><summary>{e(g)}<span>{ico("mas")}</span></summary><div>{links}</div></details>'
    return f"""
<div class="movil" id="movil" hidden>
  <div class="movil-in">
    <div class="movil-top">{logo('logo logo-claro', 'crema')}<button class="movil-x" aria-label="Cerrar menú">{ico('x')}</button></div>
    <nav class="movil-nav" aria-label="Menú móvil">
      <a class="mov-big" href="index.html">Inicio</a>
      <a class="mov-big" href="centro.html">El centro</a>
      <p class="mov-lab">Tratamientos</p>
      {grupos}
      <a class="mov-big" href="resultados.html">Resultados</a>
      <a class="mov-big" href="tarifas.html">Tarifas</a>
      <a class="mov-big" href="tarjeta-regalo.html">Tarjeta regalo</a>
      <a class="mov-big" href="contacto.html">Contacto</a>
    </nav>
    <div class="movil-pie">
      <a class="btn btn-oro" href="{wa(SANTO['wa'], 'Hola, me gustaría pedir cita en Santomera.')}" target="_blank" rel="noopener">{ico('wa')} Santomera</a>
      <a class="btn btn-linea-c" href="{wa(MURCIA['wa'], 'Hola, me gustaría pedir cita en Murcia.')}" target="_blank" rel="noopener">{ico('wa')} Murcia</a>
      <a class="movil-ig" href="{N['instagram']}" target="_blank" rel="noopener">{ico('ig')} @{N['ig_user']}</a>
    </div>
  </div>
</div>
"""


def modal_reserva():
    centros = ""
    for c in CENTROS:
        centros += f"""
      <a class="res-centro" data-wa="{c['wa']}" data-centro="{e(c['nombre'])}" href="{wa(c['wa'], 'Hola, me gustaría pedir cita.')}" target="_blank" rel="noopener">
        <img src="{img(c['foto'], True)}" alt="" loading="lazy">
        <span><small>{e(c['etiqueta'])}</small><strong>{e(c['nombre'])}</strong><em>{e(c['direccion'])} · {e(c['tel'])}</em></span>
        {ico('wa', 'ico res-wa')}
      </a>"""
    return f"""
<dialog class="reserva" id="reserva" aria-labelledby="res-t">
  <form method="dialog" class="reserva-in">
    <button class="reserva-x" aria-label="Cerrar" value="cerrar">{ico('x')}</button>
    <p class="eyebrow">Reserva tu cita</p>
    <h2 class="h3" id="res-t">¿En qué centro te esperamos?</h2>
    <p class="res-serv" hidden>Tratamiento: <strong></strong></p>
    <div class="res-centros">{centros}</div>
    <p class="res-nota">Te respondemos por WhatsApp en horario de lunes a viernes, de 9:00 a 21:00. Si lo prefieres, llámanos.</p>
  </form>
</dialog>
"""


def pie():
    servs = "".join(f'<a href="{s["slug"]}.html">{e(s["menu"])}</a>' for s in SERVICIOS)
    centros = "".join(f"""
      <div class="pie-centro"><p class="pie-h">{e(c['nombre'])}</p>
        <p>{e(c['direccion'])}<br>{e(c['cp'])}</p>
        <p><a href="tel:+34{c['tel'].replace(' ', '')}">{e(c['tel'])}</a></p></div>""" for c in CENTROS)
    return f"""
<section class="pre-pie">
  <div class="wrap pre-pie-in reveal">
    <p class="script">Te estamos esperando</p>
    <h2 class="display">Reserva tu momento</h2>
    <div class="pre-pie-btns">
      <button class="btn btn-oro" data-reserva>{ico('wa')} Pedir cita por WhatsApp</button>
      <a class="btn btn-linea-c" href="tarjeta-regalo.html">{ico('regalo')} Regalar una experiencia</a>
    </div>
  </div>
</section>
<footer class="pie">
  <div class="wrap pie-grid">
    <div class="pie-marca">
      {logo('logo logo-claro', 'crema')}
      <p>Estética avanzada con alma de spa. Tecnología de vanguardia, manos expertas y un trato cercano en Santomera y Murcia desde {N['desde']}.</p>
      <div class="pie-redes">
        <a href="{N['instagram']}" target="_blank" rel="noopener" aria-label="Instagram">{ico('ig')}</a>
        <a href="{N['facebook']}" target="_blank" rel="noopener" aria-label="Facebook">{ico('fb')}</a>
        <a href="{N['google']}" target="_blank" rel="noopener" aria-label="Google">{ico('estrella')}</a>
      </div>
    </div>
    <div class="pie-col"><p class="pie-h">Tratamientos</p><div class="pie-links">{servs}</div></div>
    <div class="pie-col">{centros}
      <div class="pie-centro"><p class="pie-h">Horario</p><p>Lunes a viernes · 9:00 – 21:00<br>Sábado y domingo · cerrado</p></div>
    </div>
  </div>
  <div class="wrap pie-base">
    <p>© 2026 Rocío Castelló Estética Avanzada</p>
    <p><a href="centro.html">El centro</a> · <a href="tarifas.html">Tarifas</a> · <a href="contacto.html">Contacto</a> · Aviso legal · Privacidad · Cookies</p>
  </div>
  <div class="pie-gigante" aria-hidden="true">Rocío Castelló</div>
</footer>
<button class="wa-flot" data-reserva aria-label="Pedir cita por WhatsApp">{ico('wa')}<span>¿Hablamos?</span></button>
{modal_reserva()}
<script src="assets/js/site.js?v={VERSION}" defer></script>
</body>
</html>
"""


def migas(*items):
    li = '<a href="index.html">Inicio</a>' + "".join(f"<span>/</span>{e(t)}" for t in items)
    return f'<nav class="migas" aria-label="Migas de pan">{li}</nav>'


def hero_split(eyebrow, titulo, acento, intro, imagen, alt, num="", datos=(), btns="", miga=()):
    chips = "".join(f'<li><small>{e(a)}</small><strong>{e(b)}</strong></li>' for a, b in datos)
    return f"""
<section class="hero-s">
  <div class="hero-s-fondo" aria-hidden="true"></div>
  <div class="hero-s-media">
    <img class="hero-s-foto" src="{img(imagen)}" srcset="{img(imagen, True)} 800w, {img(imagen)} 2000w" sizes="(max-width: 1000px) 100vw, 56vw" alt="{e(alt)}" fetchpriority="high" decoding="async">
    <span class="hero-s-chip">{ico('chispa')} Rocío Castelló · Santomera y Murcia</span>
    {sello()}
  </div>
  {f'<span class="hero-s-num" aria-hidden="true">{num}</span>' if num else ''}
  <div class="wrap hero-s-grid">
    <div class="hero-s-txt">
      {migas(*miga) if miga else ''}
      <p class="eyebrow">{f'<b>{num}</b>' if num else ''}{e(eyebrow)}</p>
      <h1 class="display hero-s-h"><span>{e(titulo)}</span><span class="script">{e(acento)}</span></h1>
      <p class="lead">{e(intro)}</p>
      <div class="hero-btns">{btns}</div>
      {f'<ul class="hero-datos">{chips}</ul>' if chips else ''}
    </div>
  </div>
</section>
"""


def btn_reserva(servicio="", txt="Reservar cita"):
    attr = f' data-servicio="{e(servicio)}"' if servicio else ""
    return f'<button class="btn btn-tinta" data-reserva{attr}>{ico("wa")} {txt}</button>'


def marquesina(palabras, cls=""):
    fila = "".join(f'<span>{e(p)}</span><img src="assets/img/rc-oro.png" alt="">' for p in palabras)
    return f'<div class="marq {cls}" aria-hidden="true"><div class="marq-pista">{fila}{fila}</div></div>'


# ------------------------------------------------------------------ bloques reutilizables
def sec_resenas():
    tarjetas = "".join(f"""
      <figure class="resena">
        {estrellas()}
        <blockquote>“{e(t)}”</blockquote>
        <figcaption><strong>{e(n)}</strong><span>{e(f)}</span></figcaption>
      </figure>""" for n, f, t in RESENAS)
    return f"""
<section class="sec resenas-sec">
  <div class="wrap">
    <div class="sec-cab reveal">
      <div>
        <p class="eyebrow">Lo que dicen nuestras clientas</p>
        <h2 class="h2">Confianza que se <em>nota</em> en la piel</h2>
      </div>
      <a class="google-nota" href="{N['google']}" target="_blank" rel="noopener">
        <span class="google-num">{N['rating']}</span>
        <span>{estrellas()}<small>{N['resenas']} reseñas en Google</small></span>
      </a>
    </div>
    <div class="carrusel" data-carrusel>
      <div class="carrusel-pista">{tarjetas}</div>
      <div class="carrusel-nav"><button class="c-prev" aria-label="Anterior">{ico('chevi')}</button><button class="c-next" aria-label="Siguiente">{ico('chev')}</button></div>
    </div>
  </div>
</section>
"""


def sec_redes():
    hls = "".join(f"""
        <a class="hl" href="https://www.instagram.com/stories/highlights/{i}/" target="_blank" rel="noopener">
          <span class="hl-aro"><img src="{img(f, True)}" alt="" loading="lazy"></span><small>{e(t)}</small></a>""" for t, f, i in IG_DESTACADOS)
    posts = "".join(f"""
        <a class="ig-post" href="{ig_post(n)}" target="_blank" rel="noopener" aria-label="Ver publicación en Instagram">
          <img src="{img(f, True)}" alt="Publicación de @{N['ig_user']}" loading="lazy"><span>{ico('ig')}</span></a>""" for f, n in IG_POSTS)
    return f"""
<section class="sec redes" id="redes">
  <div class="wrap">
    <div class="redes-grid">
      <div class="redes-txt reveal">
        <p class="eyebrow">Síguenos</p>
        <h2 class="h2">Cada día, <em>en directo</em> desde cabina</h2>
        <p class="lead">Resultados reales, novedades, promociones de temporada y el día a día de nuestro equipo. Más de {N['seguidores']} personas ya nos siguen.</p>
        <div class="redes-btns">
          <a class="btn btn-ig" href="{N['instagram']}" target="_blank" rel="noopener">{ico('ig')} Seguir a @{N['ig_user']}</a>
          <a class="btn btn-linea" href="{N['facebook']}" target="_blank" rel="noopener">{ico('fb')} Facebook</a>
        </div>
      </div>
      <div class="igc reveal">
        <div class="igc-top">
          <a class="igc-av" href="{N['instagram']}" target="_blank" rel="noopener" aria-label="Perfil de Instagram"><span><img src="assets/img/rc-tinta.png" alt=""></span></a>
          <div class="igc-datos">
            <a class="igc-user" href="{N['instagram']}" target="_blank" rel="noopener">{N['ig_user']}</a>
            <div class="igc-nums"><span><b>{N['publicaciones']}</b> publicaciones</span><span><b>{N['seguidores']}</b> seguidores</span></div>
            <p class="igc-bio"><strong>ROCIO CASTELLÓ ESTÉTICA</strong> · Salón de belleza<br>✨ C/ de la Gloria 20, Santomera · {SANTO['tel']}<br>✨ Av. Libertad 7, Barrio del Progreso · {MURCIA['tel']}</p>
          </div>
        </div>
        <div class="hls">{hls}</div>
        <div class="ig-grid">{posts}</div>
        <a class="igc-cta" href="{N['instagram']}" target="_blank" rel="noopener">Ver perfil completo {ico('flecha')}</a>
      </div>
    </div>
  </div>
</section>
"""


def sec_reels(lista=None, titulo="Así se vive <em>dentro</em>", eyebrow="Reels desde cabina"):
    lista = lista or REELS
    tarjetas = "".join(f"""
      <figure class="reel">
        <div class="reel-marco">
          <video muted loop playsinline preload="none" poster="assets/video/{v}.webp" data-src="assets/video/{v}.mp4"></video>
          <span class="reel-ig">{ico('ig')}</span>
        </div>
        <figcaption><strong>{e(t)}</strong><span>{e(s)}</span></figcaption>
      </figure>""" for v, t, s in lista)
    return f"""
<section class="sec reels-sec">
  <div class="wrap">
    <div class="sec-cab reveal">
      <div><p class="eyebrow">{e(eyebrow)}</p><h2 class="h2">{titulo}</h2></div>
      <a class="enlace" href="{N['instagram']}" target="_blank" rel="noopener">Más en Instagram {ico('flecha')}</a>
    </div>
  </div>
  <div class="reels-pista" data-arrastre>{tarjetas}</div>
</section>
"""


def sec_centros(titulo=True):
    tarjetas = ""
    for c in CENTROS:
        tarjetas += f"""
      <article class="centro reveal">
        <div class="centro-img">{foto(c['foto'], 'Centro de ' + c['nombre'])}<span class="centro-tag">{e(c['etiqueta'])}</span></div>
        <div class="centro-txt">
          <h3 class="h3">{e(c['nombre'])}</h3>
          <p class="centro-dir">{ico('pin')} {e(c['direccion'])}, {e(c['cp'])}</p>
          <p class="centro-dir">{ico('reloj')} Lunes a viernes · 9:00 – 21:00</p>
          <p class="centro-nota">{e(c['nota'])}</p>
          <div class="centro-btns">
            <a class="btn btn-tinta btn-sm" href="{wa(c['wa'], 'Hola, me gustaría pedir cita.')}" target="_blank" rel="noopener">{ico('wa')} WhatsApp</a>
            <a class="btn btn-linea btn-sm" href="tel:+34{c['tel'].replace(' ', '')}">{ico('tel')} {e(c['tel'])}</a>
            <a class="enlace" href="{c['como']}" target="_blank" rel="noopener">Cómo llegar {ico('flecha')}</a>
          </div>
        </div>
      </article>"""
    cab = """
    <div class="sec-cab reveal"><div><p class="eyebrow">Dos centros, un mismo cuidado</p><h2 class="h2">Ven a <em>conocernos</em></h2></div></div>""" if titulo else ""
    return f'<section class="sec centros-sec"><div class="wrap">{cab}<div class="centros">{tarjetas}</div></div></section>'


def sec_regalo():
    return f"""
<section class="sec regalo-banda">
  <div class="wrap regalo-grid">
    <div class="regalo-img reveal">{foto('tarjetas-regalo', 'El equipo con tarjetas regalo')}</div>
    <div class="regalo-txt reveal">
      <p class="eyebrow">Tarjetas regalo personalizadas</p>
      <h2 class="h2">Regala un <em>momento</em>, no un objeto</h2>
      <p class="lead">Elige el importe, el tratamiento o el ritual y la preparamos totalmente personalizada. Nuestros rituales de 90 minutos son el regalo favorito de cumpleaños, aniversarios y Navidad.</p>
      <a class="btn btn-oro" href="tarjeta-regalo.html">{ico('regalo')} Diseñar mi tarjeta</a>
    </div>
  </div>
</section>
"""


def galeria(nombres, titulo="En cabina", eyebrow="Galería real"):
    items = "".join(f'<button class="gal-item" data-lb="{img(n)}" aria-label="Ampliar imagen">{foto(n, "")}</button>' for n in nombres)
    return f"""
<section class="sec gal-sec">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">{e(eyebrow)}</p><h2 class="h2">{titulo}</h2></div><p class="sec-nota">Fotos reales de nuestros centros y clientas.</p></div>
    <div class="galeria">{items}</div>
  </div>
</section>
"""


CMP = {n: (t, d, c) for n, t, d, c in COMPARA}


def comparador(n, cls="", eager=False, cat=""):
    """Comparador antes/después: se arrastra la línea central (también con teclado)."""
    t, d, _ = CMP[n]
    carga = "" if eager else ' loading="lazy"'
    dcat = f' data-cat="{e(cat)}"' if cat else ""
    return f"""
      <figure class="cmp {cls}" data-cmp{dcat} style="--pos:50%">
        <div class="cmp-marco">
          <img class="cmp-d" src="assets/img/ad/{n}-d.webp" alt="Después: {e(t)}, {e(d.lower())}"{carga} draggable="false">
          <div class="cmp-a"><img src="assets/img/ad/{n}-a.webp" alt="Antes: {e(t)}"{carga} draggable="false"></div>
          <span class="cmp-et cmp-et-a">Antes</span><span class="cmp-et cmp-et-d">Después</span>
          <div class="cmp-linea" aria-hidden="true"><span>{ico('chevi')}{ico('chev')}</span></div>
          <input class="cmp-rango" type="range" min="0" max="100" value="50" aria-label="Comparar antes y después de {e(t)}">
        </div>
        <figcaption><strong>{e(t)}</strong><span>{e(d)}</span></figcaption>
      </figure>"""


def sec_equipo(completa=True):
    lista = EQUIPO if completa else EQUIPO[:4]
    tarjetas = "".join(f"""
      <article class="miembro reveal">
        <div class="miembro-img">{foto(f, n)}</div>
        <div class="miembro-txt"><small>{e(r)}</small><h3>{e(n)}</h3><p>{e(d)}</p></div>
      </article>""" for f, n, r, d in lista)
    extra = ""
    if completa:
        extra = f"""
    <div class="equipo-fotos">
      <figure class="reveal">{foto('equipo-navidad', 'El equipo celebrando la Navidad')}<figcaption>Navidad en el centro</figcaption></figure>
      <figure class="reveal">{foto('tarjetas-regalo', 'Parte del equipo con tarjetas regalo')}<figcaption>Preparando tarjetas regalo</figcaption></figure>
      <figure class="reveal">{foto('equipo-web', 'El equipo en sus inicios')}<figcaption>Donde empezó todo</figcaption></figure>
      <figure class="reveal">{foto('fb-equipo', 'El equipo en el centro')}<figcaption>Equipo 2025</figcaption></figure>
      <figure class="reveal">{foto('fb-referentes', 'Gala Mujeres Referentes de Santomera')}<figcaption>Gala Mujeres Referentes</figcaption></figure>
      <figure class="reveal">{foto('rocio-sofa', 'Rocío en el centro')}<figcaption>Rocío, en casa</figcaption></figure>
    </div>"""
    enlace = "" if completa else f'<a class="enlace" href="centro.html#equipo">Conocer al equipo {ico("flecha")}</a>'
    return f"""
<section class="sec equipo-sec" id="equipo">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">Nuestro equipo</p><h2 class="h2">Las manos que <em>te cuidan</em></h2></div>{enlace}</div>
    <figure class="equipo-foto reveal">{foto('equipo', 'Equipo de Rocío Castelló Estética Avanzada', sm=False)}<figcaption><span class="script">Somos Rocío Castelló</span>Más de diez profesionales entre Santomera y Murcia, en formación constante.</figcaption></figure>
    <div class="miembros">{tarjetas}</div>{extra}
  </div>
</section>"""


def resultados_grid(nums, cls=""):
    return "".join(
        f'<button class="res-item {cls}" data-lb="assets/img/resultados/{n}.webp" aria-label="Ampliar resultado">'
        f'<img src="assets/img/resultados/{n}.webp" alt="Antes y después de un tratamiento" loading="lazy"></button>' for n in nums)


def tabla_tarifas(grupos, abierto=False):
    out = ""
    for i, (titulo, filas) in enumerate(grupos):
        li = "".join(f'<li><span>{e(a)}</span><i></i><strong>{e(b)}</strong></li>' for a, b in filas)
        out += f'<details class="tarifa"{" open" if abierto or i == 0 else ""}><summary><span>{e(titulo)}</span><small>{len(filas)} servicios</small>{ico("mas")}</summary><ul>{li}</ul></details>'
    return out


def faq(items):
    return "".join(f'<details class="faq"><summary>{e(p)}{ico("mas")}</summary><p>{e(r)}</p></details>' for p, r in items)


# ------------------------------------------------------------------ secciones de detalle
def slugify(t):
    import unicodedata
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return "".join(c if c.isalnum() else "-" for c in t).strip("-")


def sec_sobre(s, d):
    titular, parrafos, cita = d["sobre"]
    ps = "".join(f"<p>{e(x)}</p>" for x in parrafos)
    return f"""
<section class="sec sobre-sec">
  <div class="wrap sobre-grid">
    <div class="sobre-cab reveal">
      <p class="eyebrow">{e(s['corto'])} · Rocío Castelló</p>
      <h2 class="h2">{e(titular)}</h2>
    </div>
    <div class="sobre-txt reveal">
      {ps}
      <blockquote class="sobre-cita"><span aria-hidden="true">“</span>{e(cita)}</blockquote>
    </div>
  </div>
</section>"""


def sec_fichas(s, d):
    fichas = d["fichas"]
    indice = "".join(f'<li><a href="#t-{slugify(n)}"><em>{i + 1:02d}</em>{e(n)}</a></li>' for i, (n, *_) in enumerate(fichas))
    tarjetas = ""
    for i, (n, desc, ideal, ben, dato) in enumerate(fichas):
        bens = "".join(f"<li>{ico('check')}{e(b)}</li>" for b in ben)
        tarjetas += f"""
      <article class="ficha reveal" id="t-{slugify(n)}">
        <header class="ficha-cab">
          <span class="ficha-n">{i + 1:02d}</span>
          <h3>{e(n)}</h3>
          <span class="ficha-dato">{e(dato)}</span>
        </header>
        <p class="ficha-desc">{e(desc)}</p>
        <div class="ficha-pie">
          <div class="ficha-ideal"><small>Ideal para</small><p>{e(ideal)}</p></div>
          <div class="ficha-ben"><small>Lo que notarás</small><ul>{bens}</ul></div>
        </div>
        <button class="enlace ficha-res" data-reserva data-servicio="{e(n)}">Reservar este tratamiento {ico('flecha')}</button>
      </article>"""
    return f"""
<section class="sec fichas-sec" id="carta">
  <div class="wrap">
    <div class="sec-cab reveal">
      <div><p class="eyebrow">Carta de tratamientos</p><h2 class="h2">Cada tratamiento, <em>explicado</em></h2></div>
      <p class="sec-nota">{len(fichas)} tratamientos · qué son, para quién y qué vas a notar.</p>
    </div>
    <div class="fichas-grid">
      <aside class="fichas-indice">
        <p class="q-paso">Índice</p>
        <ol>{indice}</ol>
        {btn_reserva(s['menu'], 'Pedir asesoramiento')}
        <p class="fichas-nota">¿Dudas? Te asesoramos gratis y sin compromiso.</p>
      </aside>
      <div class="fichas">{tarjetas}</div>
    </div>
  </div>
</section>"""


def sec_proceso(d):
    pasos = "".join(f'<li class="reveal"><span class="paso-n">{i + 1}</span><h3>{e(t)}</h3><p>{e(x)}</p></li>' for i, (t, x) in enumerate(d["proceso"]))
    cuid = "".join(f'<li>{ico("chispa")}<span>{e(c)}</span></li>' for c in d["cuidados"])
    return f"""
<section class="sec proceso-sec">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">Paso a paso</p><h2 class="h2">Así es <em>tu sesión</em></h2></div></div>
    <ol class="pasos">{pasos}</ol>
    <div class="cuidados reveal">
      <div><p class="eyebrow">Antes y después de tu cita</p><h3 class="h3">Consejos para <em>cuidarte</em></h3></div>
      <ul>{cuid}</ul>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ página de servicio
def pagina_servicio(s):
    det = DETALLE[s["slug"]]
    btns = btn_reserva(s["menu"]) + f'<a class="btn btn-linea" href="#carta">Ver tratamientos</a>'
    hero = hero_split(s["eyebrow"], s["titulo"], s["acento"], s["intro"], s["hero"], s["menu"],
                      s["num"], s["datos"], btns, ("Tratamientos", s["corto"]))
    bloques = ""
    for i, (t, d, f) in enumerate(s["bloques"]):
        bloques += f"""
    <article class="bloque {'bloque-inv' if i % 2 else ''}">
      <div class="bloque-img reveal">{foto(f, t)}<span class="bloque-n">0{i + 1}</span></div>
      <div class="bloque-txt reveal">
        <p class="eyebrow">{e(s['corto'])}</p>
        <h2 class="h2">{e(t)}</h2>
        <p class="lead">{e(d)}</p>
        <button class="enlace" data-reserva data-servicio="{e(t)}">Reservar este tratamiento {ico('flecha')}</button>
      </div>
    </article>"""
    lista = "".join(f'<li class="reveal"><span class="tr-n">{i + 1:02d}</span><div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>'
                    for i, (a, b) in enumerate(s["tratamientos"]))
    rituales = ""
    if s.get("rituales"):
        rituales = '<section class="sec rituales-sec"><div class="wrap"><div class="sec-cab reveal"><div><p class="eyebrow">Seis rituales · 90 minutos · 65 €</p><h2 class="h2">Elige tu <em>viaje</em></h2></div></div><div class="rituales">' + "".join(
            f'<article class="ritual reveal"><span class="ritual-n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p><small>Peeling · envoltura · ducha · masaje 1 h</small></article>'
            for i, (a, b) in enumerate(s["rituales"])) + "</div></div></section>"
    res = ""
    if s.get("resultados"):
        res = f"""
<section class="sec res-sec">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">Antes y después</p><h2 class="h2">Desliza y <em>compruébalo</em></h2></div><a class="enlace" href="resultados.html">Ver todos {ico('flecha')}</a></div>
    <div class="cmp-grid">{''.join(comparador(n) for n in s['resultados'] if n in CMP)}</div>
  </div>
</section>"""
    reel = ""
    if s.get("reel"):
        v = next(r for r in REELS if r[0] == s["reel"])
        reel = f"""
<section class="sec video-sec">
  <div class="wrap video-grid">
    <div class="video-tel reveal"><video muted loop playsinline preload="none" poster="assets/video/{v[0]}.webp" data-src="assets/video/{v[0]}.mp4"></video></div>
    <div class="video-txt reveal">
      <p class="eyebrow">Míralo en movimiento</p>
      <h2 class="h2">{e(v[1])}: <em>{e(v[2].lower())}</em></h2>
      <p class="lead">Grabado en nuestras cabinas, con nuestras clientas. Así trabajamos cada día: sin filtros, con mimo y técnica.</p>
      <a class="btn btn-ig" href="{N['instagram']}" target="_blank" rel="noopener">{ico('ig')} Ver más en Instagram</a>
    </div>
  </div>
</section>"""
    tarifas = ""
    if s["tarifas"]:
        tarifas = f"""
<section class="sec tarifas-sec" id="tarifas">
  <div class="wrap tarifas-grid">
    <div class="tarifas-txt reveal">
      <p class="eyebrow">Tarifas</p>
      <h2 class="h2">Precios <em>claros</em></h2>
      <p>Precios por sesión con IVA incluido. Pregúntanos por bonos y promociones de temporada.</p>
      <a class="enlace" href="tarifas.html">Todas las tarifas {ico('flecha')}</a>
    </div>
    <div class="tarifas-lista reveal">{tabla_tarifas(s['tarifas'])}</div>
  </div>
</section>"""
    extra = {"resultados": {"hero": "hero-resultados", "menu": "Resultados reales", "num": "✦"},
             "tarjeta-regalo": {"hero": "hero-regalo", "menu": "Tarjeta regalo", "num": "✦"},
             "tarifas": {"hero": "hero-tarifas", "menu": "Todas las tarifas", "num": "✦"}}
    pag = {**extra, **SERV}
    rel = "".join(f"""
      <a class="rel reveal" href="{r}.html">{foto(pag[r]['hero'], pag[r]['menu'])}<span><small>{pag[r]['num']}</small><strong>{e(pag[r]['menu'])}</strong>{ico('flecha')}</span></a>"""
                  for r in s["relacionados"])
    cuerpo = f"""
<main id="main">
{hero}
{marquesina([f[0] for f in det['fichas']], 'marq-fina')}
{sec_sobre(s, det)}
<section class="sec bloques">
  <div class="wrap">{bloques}</div>
</section>
{rituales}
{sec_fichas(s, det)}
{res}
{sec_proceso(det)}
{galeria(s['galeria'])}
{reel}
{tarifas}
<section class="sec faq-sec">
  <div class="wrap faq-grid">
    <div class="reveal"><p class="eyebrow">Dudas frecuentes</p><h2 class="h2">Preguntas <em>y respuestas</em></h2></div>
    <div class="faqs reveal">{faq(s['faq'])}</div>
  </div>
</section>
<section class="sec rel-sec">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">Sigue descubriendo</p><h2 class="h2">También te puede <em>interesar</em></h2></div></div>
    <div class="rels">{rel}</div>
  </div>
</section>
{sec_redes()}
</main>
"""
    titulo = f"{s['menu']} en Santomera y Murcia | Rocío Castelló Estética Avanzada"
    return head(titulo, s["intro"][:155], s["slug"]) + menu() + cuerpo + pie()


# ------------------------------------------------------------------ inicio
def pagina_inicio():
    cards = ""
    for s in SERVICIOS:
        cards += f"""
      <a class="serv reveal" href="{s['slug']}.html">
        <span class="serv-img">{foto(s['hero'], s['menu'])}</span>
        <span class="serv-txt"><small>{s['num']} · {e(s['grupo'])}</small><strong>{e(s['menu'])}</strong><em>{e(s['card'])}</em><span class="serv-mas">Descubrir {ico('flecha')}</span></span>
      </a>"""
    tecno = [
        ("Tesla Med", "Dos patentes mundiales que estimulan tus fibroblastos: lifting, manchas, acné, estrías y labios sin agujas.", "tesla-cabina", "tesla-med.html"),
        ("Symmed", "Radiofrecuencia y mesoterapia: el efecto buena cara desde la primera sesión, sin pinchazos.", "symmed-sesion", "tecnologia.html"),
        ("Zionic", "Radiofrecuencia + masaje rotacional. Adiós grasa localizada, celulitis y flacidez.", "zionic-luz", "tecnologia.html"),
        ("Hydronature", "Nueve tecnologías en una higiene facial: limpia, exfolia, extrae, hidrata y calma.", "hydronature", "tecnologia.html"),
        ("Láser de diodo", "810 nm, sesiones cada dos meses, también en verano. Resultados desde la primera.", "laser-pierna", "depilacion-laser.html"),
    ]
    tabs = "".join(f'<button class="tec-tab{" on" if i == 0 else ""}" data-tab="{i}" role="tab" aria-selected="{"true" if i == 0 else "false"}"><em>0{i + 1}</em>{e(t)}</button>' for i, (t, *_ ) in enumerate(tecno))
    panes = "".join(f"""
        <div class="tec-pane{" on" if i == 0 else ""}" data-pane="{i}" role="tabpanel">
          <div class="tec-img">{foto(f, t)}</div>
          <div class="tec-txt"><h3 class="h2">{e(t)}</h3><p class="lead">{e(d)}</p><a class="btn btn-linea-c" href="{u}">Conocer {e(t)} {ico('flecha')}</a></div>
        </div>""" for i, (t, d, f, u) in enumerate(tecno))
    quiz_zonas = "".join(f'<button class="q-zona{" on" if i == 0 else ""}" data-z="{i}">{e(z)}</button>' for i, (z, _) in enumerate(QUIZ))
    quiz_ops = "".join(
        f'<div class="q-ops{" on" if i == 0 else ""}" data-z="{i}">' + "".join(
            f'<button class="q-op" data-url="{u}.html" data-rec="{e(r)}" data-n="{e(SERV[u]["menu"] if u in SERV else "Tarjeta regalo")}">{e(o)}</button>' for o, u, r in ops) + "</div>"
        for i, (_, ops) in enumerate(QUIZ))
    experiencia = [
        ("sala-espera", "Llegas", "Una sala de espera en terciopelo y oro. Respira."),
        ("cafe", "Te mimamos", "Un café recién hecho mientras preparamos tu cabina."),
        ("velas", "Desconectas", "Música relajante, aroma amaderado y luz cálida."),
        ("cabina", "Te cuidamos", "Manos expertas y tecnología a tu servicio."),
        ("piedras", "Sales nueva", "Y siempre, un pequeño detalle para llevarte."),
    ]
    exp = "".join(f'<figure class="exp reveal" style="--i:{i}">{foto(f, t)}<figcaption><em>{i + 1:02d}</em><strong>{e(t)}</strong><span>{e(d)}</span></figcaption></figure>' for i, (f, t, d) in enumerate(experiencia))

    cmp_sel = "".join(
        f'<button class="cmp-chip{" on" if i == 0 else ""}" data-n="{n}" data-t="{e(t)}" data-d="{e(d)}"><img src="assets/img/ad/{n}-d.webp" alt="" loading="lazy"><span>{e(t)}<small>{e(d)}</small></span></button>'
        for i, (n, t, d, _) in enumerate(COMPARA[:6]))
    cuerpo = f"""
<main id="main">
<section class="hero-v" aria-label="Presentación">
  <div class="hero-v-media" aria-hidden="true">
    <div class="hv-col"><video autoplay muted loop playsinline poster="assets/video/hero-facial.webp"><source src="assets/video/hero-facial.mp4" type="video/mp4"></video></div>
    <div class="hv-col"><video autoplay muted loop playsinline poster="assets/video/hero-cabina.webp"><source src="assets/video/hero-cabina.mp4" type="video/mp4"></video></div>
    <div class="hv-col"><video autoplay muted loop playsinline poster="assets/video/hero-geotermal.webp"><source src="assets/video/hero-geotermal.mp4" type="video/mp4"></video></div>
  </div>
  <div class="hero-v-velo" aria-hidden="true"></div>
  <div class="wrap hero-v-in">
    <p class="eyebrow eyebrow-c">Santomera · Murcia · desde {N['desde']}</p>
    <h1 class="hero-v-h">
      <span class="hv-l1">El arte de cuidarte,</span>
      <span class="hv-l2">elevado a <em>ciencia</em></span>
      <span class="script hv-s">Estética Avanzada</span>
    </h1>
    <p class="hero-v-p">Tecnología que no encontrarás en otro centro de la zona, manos expertas y un trato que te hace sentir en casa. Faciales, corporales, láser, mirada y uñas en dos centros pensados para ti.</p>
    <div class="hero-btns">
      <button class="btn btn-oro" data-reserva>{ico('wa')} Reservar mi cita</button>
      <a class="btn btn-linea-c" href="#tratamientos">Descubrir tratamientos</a>
    </div>
    <ul class="hero-v-datos">
      <li><strong>{N['rating']}<small>★</small></strong><span>{N['resenas']} reseñas en Google</span></li>
      <li><strong>{N['seguidores']}</strong><span>seguidoras en Instagram</span></li>
      <li><strong>2</strong><span>centros en Santomera y Murcia</span></li>
      <li><strong>+60</strong><span>tratamientos y servicios</span></li>
    </ul>
  </div>
  <a class="hero-scroll" href="#intro" aria-label="Bajar"><span></span></a>
</section>

<div class="cinta-serv" aria-label="Servicios destacados">
  <div class="cinta-serv-pista">{''.join(f'<a href="{s["slug"]}.html">{e(s["menu"])}</a><i>✦</i>' for s in SERVICIOS) * 2}</div>
</div>

<section class="sec intro" id="intro">
  <div class="wrap intro-grid">
    <div class="intro-fotos reveal">
      <div class="intro-f1">{foto('rocio-sofa', 'Rocío Castelló en su centro')}</div>
      <div class="intro-f2">{foto('logo-dorado', 'Monograma dorado en recepción')}</div>
      <div class="intro-badge"><span class="script">Mujer referente</span><small>de Santomera</small></div>
    </div>
    <div class="intro-txt reveal">
      <p class="eyebrow">Bienvenida a tu santuario</p>
      <h2 class="h2">Belleza realzada <em>de forma natural</em>, con resultados que se ven</h2>
      <p class="lead">Rocío Castelló abrió las puertas de su centro en Santomera en {N['desde']} con una idea muy clara: que cada clienta se sienta única. Hoy, con dos centros y un equipo de profesionales en formación constante, seguimos haciendo lo mismo, con la tecnología más avanzada del sector.</p>
      <p>Diagnosticamos antes de tratar, combinamos aparatología y técnicas manuales y cuidamos todos los detalles: desde el café que te espera hasta el masaje final. Por eso el Ayuntamiento de Santomera reconoció a Rocío como <strong>Mujer Referente</strong>.</p>
      <div class="firma"><span class="script">Rocío Castelló</span><small>Fundadora y esteticista</small></div>
      <a class="enlace" href="centro.html">Conoce el centro y al equipo {ico('flecha')}</a>
    </div>
  </div>
</section>

{marquesina(CINTA, 'marq-grande')}

<section class="sec serv-sec" id="tratamientos">
  <div class="wrap">
    <div class="sec-cab reveal">
      <div><p class="eyebrow">Tratamientos</p><h2 class="h2">Once universos para <em>sentirte tú</em></h2></div>
      <a class="enlace" href="tarifas.html">Ver todas las tarifas {ico('flecha')}</a>
    </div>
    <div class="servs">{cards}</div>
  </div>
</section>

<section class="sec tec-sec">
  <div class="tec-fondo" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-cab reveal">
      <div><p class="eyebrow eyebrow-c">Aparatología de vanguardia</p><h2 class="h2 c-crema">La tecnología que <em>nos distingue</em></h2></div>
      <a class="enlace enlace-c" href="tecnologia.html">Toda la tecnología {ico('flecha')}</a>
    </div>
    <div class="tec reveal">
      <div class="tec-tabs" role="tablist">{tabs}</div>
      <div class="tec-panes">{panes}</div>
    </div>
  </div>
</section>

<section class="sec quiz-sec">
  <div class="wrap quiz-grid">
    <div class="quiz-txt reveal">
      <p class="eyebrow">Encuentra tu tratamiento</p>
      <h2 class="h2">¿Qué te <em>apetece</em> hoy?</h2>
      <p class="lead">Elige una zona y lo que buscas. Te diremos por dónde empezar y, después, lo afinamos juntas en tu diagnóstico gratuito.</p>
    </div>
    <div class="quiz reveal" data-quiz>
      <p class="q-paso">1 · Zona</p>
      <div class="q-zonas">{quiz_zonas}</div>
      <p class="q-paso">2 · Objetivo</p>
      {quiz_ops}
      <div class="q-res" hidden aria-live="polite">
        <span class="q-ico">{ico('chispa')}</span>
        <div><small>Te recomendamos</small><strong class="q-rec"></strong><a class="enlace q-url" href="#">Ver <span class="q-n"></span> {ico('flecha')}</a></div>
        <button class="btn btn-tinta btn-sm q-res-btn" data-reserva>{ico('wa')} Reservar</button>
      </div>
    </div>
  </div>
</section>

<section class="sec res-home">
  <div class="wrap res-home-grid">
    <div class="res-home-txt reveal">
      <p class="eyebrow">Antes y después</p>
      <h2 class="h2">Sin filtros. <em>Sin cirugía.</em></h2>
      <p class="lead">Arrastra la línea y mira el cambio con tus propios ojos. Casos reales de nuestras clientas, publicados con su permiso.</p>
      <div class="cmp-sel" role="tablist">{cmp_sel}</div>
      <a class="enlace" href="resultados.html">Ver los {len(COMPARA)} casos {ico('flecha')}</a>
    </div>
    <div class="res-home-cmp reveal" data-cmp-destacado>{comparador('106', 'cmp-xl', eager=True)}</div>
  </div>
</section>

<section class="sec exp-sec">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">La experiencia Rocío Castelló</p><h2 class="h2">Cada visita es un <em>ritual</em>, no una cita</h2></div></div>
    <div class="exps">{exp}</div>
  </div>
</section>

{sec_equipo(False)}
{sec_reels()}
{sec_resenas()}
{sec_regalo()}
{sec_redes()}
{sec_centros()}
</main>
"""
    return head("Rocío Castelló · Estética Avanzada en Santomera y Murcia",
                "Tu centro de estética avanzada en Santomera y Murcia ✨ Tesla Med, Symmed, Zionic, láser de diodo, faciales, corporales, pestañas, micropigmentación y uñas. 4,9★ en Google · Reserva por WhatsApp.",
                "inicio") + menu() + cuerpo + pie()


# ------------------------------------------------------------------ páginas especiales
def pagina_centro():
    hero = hero_split("El centro", "Una idea", "hecha con amor", "Un refugio tranquilo frente al ritmo del día a día. Espacios modernos y elegantes, cabinas privadas y un equipo que comparte la misma pasión: ayudarte a sentirte y verte mejor.",
                      "hero-centro", "Sala de espera del centro", "", (("Desde", N["desde"]), ("Centros", "2"), ("Equipo", "+10")),
                      btn_reserva() + '<a class="btn btn-linea" href="#equipo">Conocer al equipo</a>', ("El centro",))
    hitos = [
        (N["desde"], "Abrimos en Santomera", "Calle de la Gloria, 20. El comienzo de un sueño y de miles de clientas felices."),
        ("2024", "Barrio del Progreso", "Abrimos nuestro segundo centro en Murcia y estrenamos Symmed e Hydronature."),
        ("2025", "Llega Tesla Med", "Una tecnología única en el mundo. Y el Ayuntamiento homenajea a Rocío por el Día de la Mujer."),
        ("2026", "Seis años juntas", "Mujer Referente de Santomera, Zionic, Muse con exosomas y un equipo que no deja de crecer."),
    ]
    linea = "".join(f'<li class="reveal"><span class="hito-a">{e(a)}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for a, t, d in hitos)
    valores = [
        ("Diagnóstico antes que tratamiento", "Analizamos tu piel y tu cuerpo gratis para recomendarte solo lo que necesitas."),
        ("Formación constante", "Nos actualizamos cada temporada en nuevas técnicas y protocolos de cabina."),
        ("Cosmética de primera", "Firmas profesionales con ingredientes de calidad, muchas sin parabenos ni sulfatos."),
        ("Puntualidad y cercanía", "Tu tiempo importa: sin esperas y con un trato que te hace sentir en casa."),
    ]
    vals = "".join(f'<div class="valor reveal"><span>{ico("chispa")}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in valores)
    cuerpo = f"""
<main id="main">
{hero}
<section class="sec intro">
  <div class="wrap intro-grid">
    <div class="intro-fotos reveal">
      <div class="intro-f1">{foto('rocio-retrato', 'Rocío Castelló')}</div>
      <div class="intro-f2">{foto('rocio-referente', 'Rocío, Mujer Referente de Santomera')}</div>
    </div>
    <div class="intro-txt reveal">
      <p class="eyebrow">La fundadora</p>
      <h2 class="h2">Rocío <em>Castelló</em></h2>
      <p class="lead">Esteticista, emprendedora y la mirada detrás de cada detalle del centro. Creó Rocío Castelló Estética Avanzada para ofrecer en Santomera la tecnología y el mimo que antes había que buscar lejos.</p>
      <p>“Cierro cada año con el corazón lleno y la satisfacción de haber visto tantas miradas de felicidad frente al espejo.” Ha sido nombrada <strong>Mujer Referente de Santomera</strong> por su liderazgo y su apuesta por el talento femenino.</p>
      <div class="firma"><span class="script">Rocío</span><small>Fundadora</small></div>
    </div>
  </div>
</section>
{sec_equipo()}
<section class="sec valores-sec">
  <div class="wrap">
    <div class="sec-cab reveal"><div><p class="eyebrow">Cómo trabajamos</p><h2 class="h2">Lo que <em>nos define</em></h2></div></div>
    <div class="valores">{vals}</div>
  </div>
</section>
<section class="sec referente-sec">
  <div class="wrap referente-grid">
    <div class="referente-fotos reveal">
      <div class="ref-f1">{foto('rocio-referente', 'Rocío en la gala Mujeres Referentes de Santomera')}</div>
      <div class="ref-f2">{foto('fb-referentes', 'Las homenajeadas como Mujeres Referentes de Santomera')}</div>
    </div>
    <div class="reveal">
      <p class="eyebrow">Reconocimiento</p>
      <h2 class="h2">Mujer Referente <em>de Santomera</em></h2>
      <p class="lead">El Ayuntamiento de Santomera y Business Women Región de Murcia nombraron a Rocío Mujer Referente de Santomera, y el Ayuntamiento ya la había homenajeado en el Día de la Mujer por su esfuerzo y dedicación al mundo de la estética.</p>
      <blockquote class="cita">“Fue un privilegio compartir espacio con mujeres tan brillantes y aportar mi visión sobre el emprendimiento y el liderazgo.” <cite>— Rocío Castelló</cite></blockquote>
    </div>
  </div>
</section>
<section class="sec linea-sec">
  <div class="wrap linea-grid">
    <div class="reveal"><p class="eyebrow">Nuestra historia</p><h2 class="h2">Creciendo <em>contigo</em></h2><p class="lead">De un pequeño centro en Santomera a dos espacios de referencia en estética avanzada.</p></div>
    <ol class="linea">{linea}</ol>
  </div>
</section>
{galeria(['sala-espera', 'logo-dorado', 'cabina-verde', 'recepcion', 'cafe', 'cabina', 'velas', 'equipo-navidad', 'rocio-bambu', 'rocio-estanteria'], 'Nuestros <em>espacios</em>', 'Las instalaciones')}
{sec_centros()}
{sec_resenas()}
</main>
"""
    return head("El centro y el equipo | Rocío Castelló Estética Avanzada", "Conoce a Rocío Castelló, a su equipo y los dos centros de estética avanzada en Santomera y Murcia.", "centro") + menu() + cuerpo + pie()


def pagina_resultados():
    hero = hero_split("Antes y después", "Resultados", "que hablan solos", "Casos reales de nuestras clientas, publicados con su permiso. Sin filtros y sin cirugía: diagnóstico, constancia y la tecnología adecuada para cada piel y cada cuerpo.",
                      "hero-resultados", "Cabina de tratamiento", "", (("Casos", "+20"), ("Filtros", "ninguno"), ("Cirugía", "no")),
                      btn_reserva() + '<a class="btn btn-linea" href="#galeria-res">Ver casos</a>', ("Resultados",))
    cats = ["Rostro", "Cuerpo", "Mirada", "Micropigmentación"]
    filtros = '<button class="filtro on" data-f="todo">Todos</button>' + "".join(f'<button class="filtro" data-f="{e(c)}">{e(c)}</button>' for c in cats)
    items = "".join(comparador(n, cat=c) for n, _, _, c in COMPARA)
    montajes = resultados_grid(["018", "098", "106", "014", "135", "079", "042", "059"], "res-ancho")
    cuerpo = f"""
<main id="main">
{hero}
<section class="sec" id="galeria-res">
  <div class="wrap">
    <div class="filtros reveal">{filtros}</div>
    <p class="cmp-ayuda reveal">{ico('chevi')} Arrastra la línea de cada foto para ver el antes y el después {ico('chev')}</p>
    <div class="cmp-grid cmp-grid-res">{items}</div>
  </div>
</section>
<section class="sec res-home">
  <div class="wrap"><div class="sec-cab reveal"><div><p class="eyebrow">Tal y como los publicamos</p><h2 class="h2">Nuestros <em>casos</em> en Instagram</h2></div></div></div>
  <div class="res-pista" data-arrastre>{montajes}</div>
</section>
{sec_resenas()}
{sec_reels()}
</main>
"""
    return head("Resultados antes y después | Rocío Castelló Estética Avanzada", "Antes y después reales de tratamientos faciales, corporales, pestañas y micropigmentación en Santomera y Murcia.", "resultados") + menu() + cuerpo + pie()


def pagina_tarifas():
    hero = hero_split("Tarifas", "Precios claros", "sin sorpresas", "Todos nuestros servicios con su precio por sesión. Busca el tratamiento que te interesa y resérvalo por WhatsApp en un momento. Pregúntanos por bonos y promociones de temporada.",
                      "hero-tarifas", "Cabina preparada", "", (("Servicios", "+120"), ("IVA", "incluido"), ("Bonos", "consultar")),
                      btn_reserva(), ("Tarifas",))
    bloques = ""
    for s in SERVICIOS:
        if not s["tarifas"]:
            continue
        bloques += f"""
      <section class="tf-bloque reveal" data-tf>
        <div class="tf-cab"><img src="{img(s['hero'], True)}" alt="" loading="lazy"><div><small>{s['num']}</small><h2 class="h3">{e(s['menu'])}</h2></div><a class="enlace" href="{s['slug']}.html">Ver servicio {ico('flecha')}</a></div>
        {tabla_tarifas(s['tarifas'], True)}
      </section>"""
    indice = "".join(f'<a href="#" data-ir="{e(s["menu"])}">{e(s["corto"])}</a>' for s in SERVICIOS if s["tarifas"])
    cuerpo = f"""
<main id="main">
{hero}
<section class="sec tf-sec">
  <div class="wrap">
    <div class="tf-buscar reveal">
      <label>{ico('buscar')}<input type="search" placeholder="Busca un tratamiento: lifting, axilas, gel, Zionic…" aria-label="Buscar tratamiento" data-buscar></label>
      <div class="tf-indice">{indice}</div>
    </div>
    <p class="tf-vacio" hidden>No encontramos ese servicio. <button class="enlace" data-reserva>Pregúntanos por WhatsApp {ico('flecha')}</button></p>
    <div class="tf-bloques">{bloques}</div>
    <p class="tf-nota">Precios orientativos por sesión, IVA incluido. Algunos tratamientos requieren valoración previa gratuita. Rituales: peeling, envoltura, ducha y masaje completo de 1 h.</p>
  </div>
</section>
{sec_regalo()}
</main>
"""
    return head("Tarifas y precios | Rocío Castelló Estética Avanzada", "Precios de faciales, corporales, láser de diodo, cera, pestañas, uñas y rituales en Santomera y Murcia.", "tarifas") + menu() + cuerpo + pie()


def pagina_regalo():
    hero = hero_split("Tarjeta regalo", "Regala", "un momento para ella", "Totalmente personalizada: tú eliges el importe, el tratamiento o el ritual. La preparamos con mimo en cualquiera de nuestros dos centros, lista para sorprender.",
                      "hero-regalo", "Equipo con tarjetas regalo", "", (("Importe", "a elegir"), ("Validez", "flexible"), ("Diseño", "a medida")),
                      '<a class="btn btn-tinta" href="#disena">' + ico("regalo") + ' Diseñar mi tarjeta</a>', ("Tarjeta regalo",))
    opciones = [("Ritual de relajación 90 min", "65"), ("Masaje relajante 1 h", "48"), ("Higiene facial profunda", "48"),
                ("Tratamiento facial personalizado", "65"), ("Lifting de pestañas y tinte", "45"), ("Manicura + pedicura spa", "54")]
    ops = "".join(f'<button class="tg-op{" on" if i == 0 else ""}" data-t="{e(t)}" data-p="{p}">{e(t)}<small>{p} €</small></button>' for i, (t, p) in enumerate(opciones))
    importes = "".join(f'<button class="tg-imp" data-p="{p}">{p} €</button>' for p in ("30", "50", "75", "100", "150"))
    cuerpo = f"""
<main id="main">
{hero}
<section class="sec tg-sec" id="disena">
  <div class="wrap tg-grid">
    <div class="tg-form reveal">
      <p class="eyebrow">Diséñala en 1 minuto</p>
      <h2 class="h2">Tu tarjeta, <em>a tu manera</em></h2>
      <p class="q-paso">1 · Elige un tratamiento</p>
      <div class="tg-ops">{ops}</div>
      <p class="q-paso">… o un importe libre</p>
      <div class="tg-imps">{importes}</div>
      <p class="q-paso">2 · Personalízala</p>
      <label class="campo"><span>Para</span><input type="text" maxlength="28" placeholder="Nombre de quien la recibe" data-tg="para"></label>
      <label class="campo"><span>De parte de</span><input type="text" maxlength="28" placeholder="Tu nombre" data-tg="de"></label>
      <label class="campo"><span>Mensaje</span><textarea maxlength="120" rows="2" placeholder="Feliz cumpleaños, te mereces este momento…" data-tg="msg"></textarea></label>
      <p class="q-paso">3 · Centro de recogida</p>
      <div class="tg-centros">{''.join(f'<button class="tg-centro{" on" if i == 0 else ""}" data-wa="{c["wa"]}" data-c="{e(c["nombre"])}">{e(c["nombre"])}</button>' for i, c in enumerate(CENTROS))}</div>
      <a class="btn btn-oro tg-enviar" href="#" target="_blank" rel="noopener">{ico('wa')} Pedir esta tarjeta por WhatsApp</a>
    </div>
    <div class="tg-vista reveal">
      <div class="tarjeta" data-tarjeta>
        <div class="tarjeta-marmol"></div>
        <img class="tarjeta-rc" src="assets/img/rc-oro.png" alt="">
        <p class="tarjeta-eyebrow">Tarjeta regalo</p>
        <p class="tarjeta-trat" data-v="trat">Ritual de relajación 90 min</p>
        <p class="tarjeta-para">Para <span data-v="para">ti</span></p>
        <p class="tarjeta-msg" data-v="msg">Te mereces este momento.</p>
        <div class="tarjeta-pie"><span>De <b data-v="de">alguien que te quiere</b></span><span class="tarjeta-precio" data-v="precio">65 €</span></div>
        <p class="tarjeta-marca">Rocío Castelló · Estética Avanzada</p>
      </div>
      <p class="tg-nota">Vista previa orientativa. Te entregamos la tarjeta impresa en el centro, en un sobre a juego.</p>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap fotos-dos">
    <figure class="reveal">{foto('tarjeta-mostrador', 'Tarjeta regalo en recepción')}</figure>
    <figure class="reveal">{foto('regalo-madre', 'Regalo para el Día de la Madre')}</figure>
    <figure class="reveal">{foto('fb-gold', 'Tarjeta regalo Gold')}</figure>
  </div>
</section>
{sec_resenas()}
</main>
"""
    return head("Tarjeta regalo personalizada | Rocío Castelló Estética Avanzada", "Regala un ritual, un masaje o un tratamiento facial con una tarjeta regalo personalizada en Santomera o Murcia.", "tarjeta-regalo") + menu() + cuerpo + pie()


def pagina_contacto():
    hero = hero_split("Contacto", "Estamos", "muy cerca de ti", "Dos centros, un mismo cuidado. Escríbenos por WhatsApp, llámanos o pásate a vernos: te asesoramos sin compromiso y te ayudamos a elegir el tratamiento perfecto.",
                      "hero-contacto", "Fachada del centro de Santomera", "", (("Santomera", SANTO["tel"]), ("Murcia", MURCIA["tel"])),
                      btn_reserva("", "Escribir por WhatsApp"), ("Contacto",))
    mapas = "".join(f"""
      <article class="mapa-c reveal">
        <div class="mapa"><iframe src="{c['mapa']}" title="Mapa del centro de {e(c['nombre'])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="mapa-txt">
          <p class="eyebrow">{e(c['etiqueta'])}</p>
          <h2 class="h3">{e(c['nombre'])}</h2>
          <p>{ico('pin')} {e(c['direccion'])}<br>{e(c['cp'])}</p>
          <p>{ico('tel')} <a href="tel:+34{c['tel'].replace(' ', '')}">{e(c['tel'])}</a></p>
          <div class="centro-btns">
            <a class="btn btn-tinta btn-sm" href="{wa(c['wa'], 'Hola, me gustaría pedir cita.')}" target="_blank" rel="noopener">{ico('wa')} WhatsApp</a>
            <a class="btn btn-linea btn-sm" href="{c['como']}" target="_blank" rel="noopener">{ico('pin')} Cómo llegar</a>
          </div>
        </div>
      </article>""" for c in CENTROS)
    horario = "".join(f"<li><span>{e(d)}</span><strong>{e(h)}</strong></li>" for d, h in HORARIO)
    cuerpo = f"""
<main id="main">
{hero}
<section class="sec">
  <div class="wrap mapas">{mapas}</div>
</section>
<section class="sec horario-sec">
  <div class="wrap horario-grid">
    <div class="reveal"><p class="eyebrow">Horario</p><h2 class="h2">Cuando <em>tú</em> puedas</h2><p class="lead">Abrimos de lunes a viernes de forma ininterrumpida para que encuentres hueco antes o después del trabajo.</p></div>
    <div class="reveal"><ul class="horario" data-horario>{horario}</ul><p class="horario-nota">{e(HORARIO_VERANO)}</p><p class="ahora" data-abierto></p></div>
  </div>
</section>
{sec_redes()}
</main>
"""
    return head("Contacto y ubicación | Rocío Castelló Estética Avanzada", "Centros de estética en C/ de la Gloria 20, Santomera (669 024 902) y Av. Libertad 7, Barrio del Progreso, Murcia (623 510 014).", "contacto") + menu() + cuerpo + pie()


def main():
    paginas = {"index.html": pagina_inicio(), "centro.html": pagina_centro(), "resultados.html": pagina_resultados(),
               "tarifas.html": pagina_tarifas(), "tarjeta-regalo.html": pagina_regalo(), "contacto.html": pagina_contacto()}
    for s in SERVICIOS:
        paginas[f"{s['slug']}.html"] = pagina_servicio(s)
    for nombre, html in paginas.items():
        (ROOT / nombre).write_text(html, encoding="utf-8")
    print(f"{len(paginas)} páginas generadas")


if __name__ == "__main__":
    main()
