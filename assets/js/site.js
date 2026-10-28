/* Rocío Castelló · interacción de la web */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const body = document.body;
  const pagina = body.dataset.pagina;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // enlace activo
  $$(`.nav [data-nav="${pagina}"]`).forEach((a) => a.classList.add("activo"));

  // cabecera: sólida al bajar, la cinta se oculta
  const cab = $("#cab");
  const wa = $(".wa-flot");
  let ultimo = 0;
  const onScroll = () => {
    const y = scrollY;
    cab.classList.toggle("solida", y > 40);
    cab.classList.toggle("oculta", y > 200 && y > ultimo);
    wa && wa.classList.toggle("ver", y > 500);
    ultimo = y;
  };
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // mega menú
  const megaBtn = $(".nav-btn");
  const mega = $("#mega");
  if (megaBtn) {
    const abrir = (v) => { mega.classList.toggle("abierto", v); megaBtn.setAttribute("aria-expanded", v); };
    const zona = $(".nav-mega");
    let t;
    zona.addEventListener("mouseenter", () => { clearTimeout(t); abrir(true); });
    zona.addEventListener("mouseleave", () => { t = setTimeout(() => abrir(false), 180); });
    megaBtn.addEventListener("click", () => abrir(!mega.classList.contains("abierto")));
    document.addEventListener("keydown", (e) => e.key === "Escape" && abrir(false));
    const prev = $(".mega-img img");
    $$(".mega-col a").forEach((a) => a.addEventListener("mouseenter", () => { prev.src = a.dataset.img; }));
    zona.addEventListener("mouseleave", () => { prev.src = prev.dataset.def; });
  }

  // menú móvil
  const movil = $("#movil");
  const burger = $(".burger");
  const cerrarMovil = () => { movil.classList.remove("abierto"); burger.setAttribute("aria-expanded", "false"); body.style.overflow = ""; setTimeout(() => (movil.hidden = true), 600); };
  burger.addEventListener("click", () => {
    movil.hidden = false;
    requestAnimationFrame(() => movil.classList.add("abierto"));
    burger.setAttribute("aria-expanded", "true");
    body.style.overflow = "hidden";
    $$(".mov-big, .mov-g", movil).forEach((el, i) => (el.style.transitionDelay = `${0.15 + i * 0.04}s`));
  });
  $(".movil-x").addEventListener("click", cerrarMovil);

  // modal de reserva por WhatsApp
  const dlg = $("#reserva");
  $$("[data-reserva]").forEach((b) => b.addEventListener("click", (ev) => {
    if (b.tagName === "A") return;
    ev.preventDefault();
    const serv = b.dataset.servicio || "";
    const p = $(".res-serv", dlg);
    p.hidden = !serv;
    $("strong", p).textContent = serv;
    $$(".res-centro", dlg).forEach((a) => {
      const txt = `Hola, me gustaría pedir cita en ${a.dataset.centro}${serv ? ` para ${serv}` : ""}. ¿Qué disponibilidad tenéis?`;
      a.href = `https://wa.me/${a.dataset.wa}?text=${encodeURIComponent(txt)}`;
    });
    if (!movil.hidden) cerrarMovil();
    dlg.showModal();
  }));
  dlg.addEventListener("click", (e) => { if (e.target === dlg) dlg.close(); });

  // aparición al hacer scroll
  const io = new IntersectionObserver((ents) => ents.forEach((en) => {
    if (en.isIntersecting) { en.target.classList.add("visto"); io.unobserve(en.target); }
  }), { rootMargin: "0px 0px -8% 0px" });
  $$(".reveal").forEach((el) => io.observe(el));

  // vídeos: carga diferida y reproducción sólo en pantalla
  const vio = new IntersectionObserver((ents) => ents.forEach((en) => {
    const v = en.target;
    if (en.isIntersecting) {
      if (v.dataset.src && !v.src) v.src = v.dataset.src;
      if (!reduce) v.play().catch(() => {});
    } else v.pause();
  }), { threshold: 0.25 });
  $$("video").forEach((v) => vio.observe(v));

  // parallax suave en imágenes de bloques
  const par = $$(".bloque-img img");
  if (par.length && !reduce) {
    const mover = () => par.forEach((im) => {
      const r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) return;
      const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
      im.style.transform = `translateY(${-7 + p * -10}%)`;
    });
    addEventListener("scroll", () => requestAnimationFrame(mover), { passive: true });
    mover();
  }

  // pistas horizontales arrastrables
  $$("[data-arrastre]").forEach((el) => {
    let x0, s0, mov = false;
    el.addEventListener("pointerdown", (e) => { if (e.pointerType !== "mouse") return; x0 = e.clientX; s0 = el.scrollLeft; mov = false; el.style.scrollSnapType = "none"; el.setPointerCapture(e.pointerId); });
    el.addEventListener("pointermove", (e) => { if (x0 == null) return; const d = e.clientX - x0; if (Math.abs(d) > 4) mov = true; el.scrollLeft = s0 - d; });
    const fin = () => { x0 = null; el.style.scrollSnapType = ""; };
    el.addEventListener("pointerup", fin);
    el.addEventListener("pointercancel", fin);
    el.addEventListener("click", (e) => { if (mov) { e.preventDefault(); e.stopPropagation(); } }, true);
  });

  // carrusel de reseñas
  $$("[data-carrusel]").forEach((c) => {
    const pista = $(".carrusel-pista", c);
    const paso = () => pista.firstElementChild.getBoundingClientRect().width + 20;
    $(".c-next", c).addEventListener("click", () => {
      const fin = pista.scrollLeft + pista.clientWidth >= pista.scrollWidth - 10;
      pista.scrollTo({ left: fin ? 0 : pista.scrollLeft + paso() });
    });
    $(".c-prev", c).addEventListener("click", () => pista.scrollBy({ left: -paso() }));
  });

  // pestañas de tecnología
  $$(".tec-tab").forEach((t) => t.addEventListener("click", () => {
    $$(".tec-tab").forEach((x) => { x.classList.toggle("on", x === t); x.setAttribute("aria-selected", x === t); });
    $$(".tec-pane").forEach((p) => p.classList.toggle("on", p.dataset.pane === t.dataset.tab));
  }));

  // asistente de tratamiento
  const quiz = $("[data-quiz]");
  if (quiz) {
    const res = $(".q-res", quiz);
    $$(".q-zona", quiz).forEach((z) => z.addEventListener("click", () => {
      $$(".q-zona", quiz).forEach((x) => x.classList.toggle("on", x === z));
      $$(".q-ops", quiz).forEach((o) => o.classList.toggle("on", o.dataset.z === z.dataset.z));
      res.hidden = true;
    }));
    $$(".q-op", quiz).forEach((o) => o.addEventListener("click", () => {
      $$(".q-op", quiz).forEach((x) => x.classList.toggle("on", x === o));
      $(".q-rec", res).textContent = o.dataset.rec;
      $(".q-n", res).textContent = o.dataset.n;
      $(".q-url", res).href = o.dataset.url;
      $(".q-res-btn", res).dataset.servicio = o.dataset.rec;
      res.hidden = false;
    }));
  }

  // visor de imágenes
  const lbItems = $$("[data-lb]");
  if (lbItems.length) {
    const lb = document.createElement("div");
    lb.className = "lb";
    lb.innerHTML = '<img alt=""><button aria-label="Cerrar"><svg class="ico" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></button>';
    body.append(lb);
    const cerrar = () => lb.classList.remove("ver");
    lb.addEventListener("click", cerrar);
    document.addEventListener("keydown", (e) => e.key === "Escape" && cerrar());
    lbItems.forEach((b) => b.addEventListener("click", () => { $("img", lb).src = b.dataset.lb; lb.classList.add("ver"); }));
  }

  // filtros de resultados
  $$(".filtro").forEach((f) => f.addEventListener("click", () => {
    $$(".filtro").forEach((x) => x.classList.toggle("on", x === f));
    $$(".res-masonry .res-item, .cmp-grid-res .cmp").forEach((it) => it.classList.toggle("fuera", f.dataset.f !== "todo" && it.dataset.cat !== f.dataset.f));
  }));

  // buscador de tarifas
  const buscar = $("[data-buscar]");
  if (buscar) {
    const norm = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
    buscar.addEventListener("input", () => {
      const q = norm(buscar.value.trim());
      let total = 0;
      $$("[data-tf]").forEach((b) => {
        const titulo = norm($("h2", b).textContent);
        let n = 0;
        $$("li", b).forEach((li) => { const ok = !q || titulo.includes(q) || norm(li.textContent).includes(q); li.classList.toggle("fuera", !ok); n += ok; });
        b.classList.toggle("fuera", !n);
        total += n;
      });
      $(".tf-vacio").hidden = total > 0;
    });
    $$("[data-ir]").forEach((a) => a.addEventListener("click", (e) => {
      e.preventDefault();
      buscar.value = "";
      buscar.dispatchEvent(new Event("input"));
      const b = $$("[data-tf]").find((x) => $("h2", x).textContent === a.dataset.ir);
      b && scrollTo({ top: b.getBoundingClientRect().top + scrollY - 200, behavior: "smooth" });
    }));
  }

  // tarjeta regalo en vivo
  const tarjeta = $("[data-tarjeta]");
  if (tarjeta) {
    const v = (k) => $(`[data-v="${k}"]`, tarjeta);
    const estado = { trat: "Ritual de relajación 90 min", precio: "65 €", wa: "", centro: "" };
    const campos = { para: $('[data-tg="para"]'), de: $('[data-tg="de"]'), msg: $('[data-tg="msg"]') };
    const enviar = $(".tg-enviar");
    const pinta = () => {
      v("trat").textContent = estado.trat;
      v("precio").textContent = estado.precio;
      v("para").textContent = campos.para.value || "ti";
      v("de").textContent = campos.de.value || "alguien que te quiere";
      v("msg").textContent = campos.msg.value || "Te mereces este momento.";
      const c = $(".tg-centro.on");
      const txt = `Hola, me gustaría pedir una tarjeta regalo en ${c.dataset.c}:\n· ${estado.trat} (${estado.precio})\n· Para: ${campos.para.value || "-"}\n· De: ${campos.de.value || "-"}\n· Mensaje: ${campos.msg.value || "-"}`;
      enviar.href = `https://wa.me/${c.dataset.wa}?text=${encodeURIComponent(txt)}`;
    };
    $$(".tg-op").forEach((o) => o.addEventListener("click", () => {
      $$(".tg-op, .tg-imp").forEach((x) => x.classList.remove("on"));
      o.classList.add("on");
      estado.trat = o.dataset.t; estado.precio = `${o.dataset.p} €`; pinta();
    }));
    $$(".tg-imp").forEach((o) => o.addEventListener("click", () => {
      $$(".tg-op, .tg-imp").forEach((x) => x.classList.remove("on"));
      o.classList.add("on");
      estado.trat = "Un momento de belleza a tu elección"; estado.precio = `${o.dataset.p} €`; pinta();
    }));
    $$(".tg-centro").forEach((o) => o.addEventListener("click", () => { $$(".tg-centro").forEach((x) => x.classList.toggle("on", x === o)); pinta(); }));
    Object.values(campos).forEach((c) => c.addEventListener("input", pinta));
    pinta();
  }

  // comparadores antes / después
  const iniciaCmp = (c) => {
    const marco = $(".cmp-marco", c);
    const rango = $(".cmp-rango", c);
    const pon = (v) => { v = Math.max(0, Math.min(100, v)); c.style.setProperty("--pos", v + "%"); rango.value = v; };
    const desdeX = (x) => { const r = marco.getBoundingClientRect(); pon(((x - r.left) / r.width) * 100); };
    rango.addEventListener("input", () => pon(+rango.value));
    let activo = false, x0 = 0, y0 = 0, decidido = false;
    marco.addEventListener("pointerdown", (e) => {
      activo = true; decidido = e.pointerType === "mouse"; x0 = e.clientX; y0 = e.clientY;
      if (decidido) { c.classList.add("arrastrando"); desdeX(e.clientX); marco.setPointerCapture(e.pointerId); }
    });
    marco.addEventListener("pointermove", (e) => {
      if (!activo) return;
      if (!decidido) {
        const dx = Math.abs(e.clientX - x0), dy = Math.abs(e.clientY - y0);
        if (dx < 6 && dy < 6) return;
        if (dy > dx) { activo = false; return; }
        decidido = true; c.classList.add("arrastrando"); marco.setPointerCapture(e.pointerId);
      }
      desdeX(e.clientX);
    });
    const fin = (e) => { if (activo && !decidido && e.type === "pointerup") desdeX(e.clientX); activo = false; c.classList.remove("arrastrando"); };
    marco.addEventListener("pointerup", fin);
    marco.addEventListener("pointercancel", fin);
    marco.tabIndex = 0;
    marco.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft" || e.key === "ArrowRight") { e.preventDefault(); pon(+rango.value + (e.key === "ArrowLeft" ? -5 : 5)); }
    });
    // pequeño vaivén la primera vez que se ve, para enseñar que se puede arrastrar
    const ob = new IntersectionObserver(([en]) => {
      if (!en.isIntersecting || reduce) return;
      ob.disconnect();
      let t0 = null;
      const anima = (t) => {
        if (t0 === null) t0 = t;
        const p = (t - t0) / 1800;
        if (p >= 1 || activo) return;
        pon(50 + Math.sin(p * Math.PI * 2) * 20);
        requestAnimationFrame(anima);
      };
      setTimeout(() => requestAnimationFrame(anima), 500);
    }, { threshold: 0.6 });
    ob.observe(c);
  };
  $$("[data-cmp]").forEach(iniciaCmp);

  // selector del comparador destacado (inicio)
  const dest = $("[data-cmp-destacado]");
  if (dest) {
    $$(".cmp-chip").forEach((ch) => ch.addEventListener("click", () => {
      $$(".cmp-chip").forEach((x) => x.classList.toggle("on", x === ch));
      const c = $(".cmp", dest);
      c.classList.add("cambia");
      setTimeout(() => {
        const n = ch.dataset.n;
        $(".cmp-d", c).src = "assets/img/ad/" + n + "-d.webp";
        $(".cmp-a img", c).src = "assets/img/ad/" + n + "-a.webp";
        $("figcaption strong", c).textContent = ch.dataset.t;
        $("figcaption span", c).textContent = ch.dataset.d;
        c.style.setProperty("--pos", "50%");
        $(".cmp-rango", c).value = 50;
        setTimeout(() => c.classList.remove("cambia"), 250);
      }, 300);
    }));
  }

  // índice de fichas: resalta el tratamiento visible
  const indice = $$(".fichas-indice a");
  if (indice.length) {
    const porId = Object.fromEntries(indice.map((a) => [a.getAttribute("href").slice(1), a]));
    const fo = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) { indice.forEach((a) => a.classList.remove("activo")); porId[en.target.id]?.classList.add("activo"); }
    }), { rootMargin: "-40% 0px -55% 0px" });
    $$(".ficha").forEach((f) => fo.observe(f));
  }

  // visor de resultados caso a caso
  const visor = $("[data-visor]");
  if (visor) {
    const casos = JSON.parse($("#casos").textContent);
    const cmp = $(".cmp", visor);
    const v = (k) => $(`[data-v="${k}"]`, visor);
    const minis = $$(".visor-mini");
    let lista = casos.map((_, i) => i);
    let pos = 0;
    const dos = (n) => String(n).padStart(2, "0");
    const pinta = (animar = true) => {
      const i = lista[pos], c = casos[i];
      const aplica = () => {
        $(".cmp-d", cmp).src = "assets/img/ad/" + c.n + "-d.webp";
        $(".cmp-a img", cmp).src = "assets/img/ad/" + c.n + "-a.webp";
        $(".cmp-d", cmp).alt = "Después: " + c.t + ", " + c.d.toLowerCase();
        cmp.style.setProperty("--pos", "50%");
        $(".cmp-rango", cmp).value = 50;
        v("i").textContent = dos(pos + 1);
        v("total").textContent = dos(lista.length);
        v("c").textContent = c.c;
        v("t").textContent = c.t;
        v("d").textContent = c.d;
        v("x").textContent = c.x;
        $("[data-v-url]", visor).href = c.u;
        $("[data-v-res]", visor).dataset.servicio = c.t + " (" + c.d + ")";
        $(".visor-barra span", visor).style.width = ((pos + 1) / lista.length) * 100 + "%";
        minis.forEach((m) => m.classList.toggle("on", +m.dataset.i === i));
        const activo = minis.find((m) => +m.dataset.i === i);
        if (activo) activo.parentElement.scrollTo({ left: activo.offsetLeft - activo.parentElement.clientWidth / 2 + activo.clientWidth / 2, behavior: "smooth" });
        setTimeout(() => cmp.classList.remove("cambia"), 60);
      };
      if (!animar) return aplica();
      cmp.classList.add("cambia");
      const pre = new Image();
      pre.src = "assets/img/ad/" + c.n + "-a.webp";
      setTimeout(aplica, 320);
    };
    const mueve = (d) => { pos = (pos + d + lista.length) % lista.length; pinta(); };
    $(".visor-prev", visor).addEventListener("click", () => mueve(-1));
    $(".visor-next", visor).addEventListener("click", () => mueve(1));
    minis.forEach((m) => m.addEventListener("click", () => { pos = Math.max(0, lista.indexOf(+m.dataset.i)); pinta(); }));
    const filtra = (cat) => {
      $$(".visor-filtros button").forEach((b) => b.classList.toggle("on", b.dataset.f === cat));
      lista = casos.map((c, i) => [c, i]).filter(([c]) => cat === "todo" || c.c === cat).map(([, i]) => i);
      minis.forEach((m) => { m.hidden = cat !== "todo" && m.dataset.cat !== cat; });
      pos = 0;
      pinta();
    };
    $$(".visor-filtros button").forEach((b) => b.addEventListener("click", () => filtra(b.dataset.f)));
    $$("[data-ir-cat]").forEach((b) => b.addEventListener("click", () => {
      filtra(b.dataset.irCat);
      $("#visor").scrollIntoView({ behavior: "smooth" });
    }));
    // precarga discreta del siguiente caso
    visor.addEventListener("mouseenter", () => { const c = casos[lista[(pos + 1) % lista.length]]; new Image().src = "assets/img/ad/" + c.n + "-d.webp"; });
  }

  // ¿abierto ahora?
  const ab = $("[data-abierto]");
  if (ab) {
    const d = new Date();
    const dia = d.getDay();
    const h = d.getHours() + d.getMinutes() / 60;
    const abierto = dia >= 1 && dia <= 5 && h >= 9 && h < 21;
    ab.textContent = abierto ? "Abierto ahora · hasta las 21:00" : "Ahora cerrado · escríbenos y te respondemos al abrir";
    ab.classList.toggle("si", abierto);
  }
})();
