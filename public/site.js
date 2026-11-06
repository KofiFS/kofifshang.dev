/* kofifshang.dev — the only script on the site.
   Everything here is an enhancement: with JavaScript off, every page still
   reads, links and submits (the contact form falls back to the email address). */
(function () {
  'use strict';

  var doc = document;
  var root = doc.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };

  /* ---------- Navigation ---------- */

  var nav = $('.nav');
  if (nav && !nav.classList.contains('nav--solid')) {
    var onScroll = function () { nav.classList.toggle('is-scrolled', window.scrollY > 12); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // A pill that glides to whichever link is hovered.
  var links = $('.nav__links');
  var pill = $('.nav__pill');
  if (links && pill) {
    var moveTo = function (a) {
      var lr = links.getBoundingClientRect(), ar = a.getBoundingClientRect();
      pill.style.width = ar.width + 'px';
      pill.style.setProperty('--x', (ar.left - lr.left) + 'px');
      pill.classList.add('is-ready');
    };
    $$('.nav__link', links).forEach(function (a) {
      a.addEventListener('mouseenter', function () { moveTo(a); });
      a.addEventListener('focus', function () { moveTo(a); });
    });
  }

  // Mobile menu: a full-screen sheet with focus kept inside while open.
  var toggle = $('.nav__toggle');
  var menu = $('#menu');
  if (toggle && menu) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      menu.classList.toggle('is-open', open);
      menu.setAttribute('aria-hidden', String(!open));
      doc.body.classList.toggle('menu-open', open);
      $$('main, .foot').forEach(function (el) { el.inert = open; });
      if (open) { var list = $('.menu__links', menu); list.setAttribute('tabindex', '-1'); list.focus({ preventScroll: true }); }
    };
    toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) { setOpen(false); toggle.focus(); }
    });
    window.matchMedia('(min-width: 861px)').addEventListener('change', function (m) { if (m.matches) setOpen(false); });
  }

  /* ---------- Reveal on scroll ---------- */

  var revealables = $$('[data-reveal]');
  if (reduce.matches || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Hero ---------- */

  var hero = $('.hero');
  if (hero) {
    var loaded = function () { hero.classList.add('is-loaded'); };
    requestAnimationFrame(function () { requestAnimationFrame(loaded); });
    setTimeout(loaded, 120); // in case animation frames are throttled (background tabs)

    // The layered composition leans a few pixels toward the cursor.
    var stage = $('.stage');
    if (stage && finePointer.matches && !reduce.matches) {
      var tx = 0, ty = 0, cx = 0, cy = 0, raf = 0;
      var tick = function () {
        cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
        stage.style.setProperty('--px', cx.toFixed(3));
        stage.style.setProperty('--py', cy.toFixed(3));
        raf = (Math.abs(tx - cx) > 0.001 || Math.abs(ty - cy) > 0.001) ? requestAnimationFrame(tick) : 0;
      };
      hero.addEventListener('pointermove', function (e) {
        var r = hero.getBoundingClientRect();
        tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
        ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
        if (!raf) raf = requestAnimationFrame(tick);
      });
      hero.addEventListener('pointerleave', function () { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(tick); });
    }
  }

  /* ---------- Gentle parallax on full-bleed imagery ---------- */

  var bleeds = $$('[data-parallax]');
  if (bleeds.length && !reduce.matches) {
    var pending = false;
    var update = function () {
      pending = false;
      if (window.innerWidth <= 600) return;
      var vh = window.innerHeight;
      bleeds.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var progress = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2); // -1 … 1
        el.style.setProperty('--parallax', (progress * -36).toFixed(1) + 'px');
      });
    };
    window.addEventListener('scroll', function () { if (!pending) { pending = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }

  /* ---------- Catalogue preview that follows the cursor ---------- */

  var ledger = $('.ledger');
  if (ledger && finePointer.matches) {
    var preview = doc.createElement('div');
    preview.className = 'preview';
    preview.setAttribute('aria-hidden', 'true');
    preview.innerHTML = '<img alt="">';
    doc.body.appendChild(preview);
    var pimg = $('img', preview);
    var px = 0, py = 0, qx = 0, qy = 0, praf = 0;
    var follow = function () {
      qx += (px - qx) * 0.18; qy += (py - qy) * 0.18;
      preview.style.setProperty('--x', qx.toFixed(1) + 'px');
      preview.style.setProperty('--y', qy.toFixed(1) + 'px');
      praf = requestAnimationFrame(follow);
    };
    var place = function (e) { px = e.clientX + 28; py = e.clientY - 150; };
    $$('.ledger__row', ledger).forEach(function (row) {
      var thumb = $('.ledger__thumb img', row);
      row.addEventListener('mouseenter', function (e) {
        if (!thumb) return;
        pimg.src = thumb.currentSrc || thumb.src;
        place(e);
        if (!preview.classList.contains('is-on')) { qx = px; qy = py; }
        preview.classList.add('is-on');
        if (!praf) praf = requestAnimationFrame(follow);
      });
      row.addEventListener('mousemove', place);
    });
    ledger.addEventListener('mouseleave', function () {
      preview.classList.remove('is-on');
      setTimeout(function () { if (!preview.classList.contains('is-on')) { cancelAnimationFrame(praf); praf = 0; } }, 400);
    });
  }

  /* ---------- Games filters ---------- */

  var filterBar = $('.filters');
  var shelf = $('.shelf');
  if (filterBar && shelf) {
    filterBar.hidden = false;
    var items = $$('.title', shelf);
    var count = $('.filters__count', filterBar);
    var buttons = $$('.filter', filterBar);
    buttons.forEach(function (b) {
      var key = b.dataset.filter;
      var n = key === 'all' ? items.length : items.filter(function (it) { return (' ' + it.dataset.tags + ' ').indexOf(' ' + key + ' ') > -1; }).length;
      var small = $('small', b); if (small) small.textContent = n;
    });
    var apply = function (key, fromUrl) {
      var shown = 0;
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.filter === key)); });
      items.forEach(function (it) {
        var match = key === 'all' || (' ' + it.dataset.tags + ' ').indexOf(' ' + key + ' ') > -1;
        it.hidden = !match;
        it.classList.remove('is-entering');
        if (match) {
          it.style.setProperty('--n', shown);
          if (!fromUrl && !reduce.matches) { void it.offsetWidth; it.classList.add('is-entering'); }
          shown++;
        }
      });
      var extras = $('[data-extras]', shelf); if (extras) extras.hidden = key !== 'all';
      if (count) count.textContent = shown + (shown === 1 ? ' title' : ' titles');
      if (!fromUrl) {
        var url = new URL(location.href);
        if (key === 'all') url.searchParams.delete('type'); else url.searchParams.set('type', key);
        history.replaceState(null, '', url);
      }
    };
    buttons.forEach(function (b) { b.addEventListener('click', function () { apply(b.dataset.filter); }); });
    var initial = new URLSearchParams(location.search).get('type');
    apply(buttons.some(function (b) { return b.dataset.filter === initial; }) ? initial : 'all', true);
  }

  /* ---------- Copy email ---------- */

  $$('[data-copy]').forEach(function (btn) {
    var label = $('span', btn);
    var original = label ? label.textContent : '';
    btn.addEventListener('click', function () {
      var text = btn.dataset.copy;
      var done = function () {
        btn.classList.add('is-done');
        if (label) label.textContent = 'Copied';
        setTimeout(function () { btn.classList.remove('is-done'); if (label) label.textContent = original; }, 1800);
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(done, function () { location.href = 'mailto:' + text; });
      } else {
        location.href = 'mailto:' + text;
      }
    });
  });

  /* ---------- Lightbox ---------- */

  var shots = $$('[data-full]');
  if (shots.length && 'HTMLDialogElement' in window) {
    var dlg = doc.createElement('dialog');
    dlg.className = 'lightbox';
    dlg.innerHTML =
      '<img alt="">' +
      '<button class="lightbox__close" type="button" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
      '<div class="lightbox__bar"><span class="lightbox__cap"></span><span class="lightbox__pos"></span></div>';
    doc.body.appendChild(dlg);
    var limg = $('img', dlg), lcap = $('.lightbox__cap', dlg), lpos = $('.lightbox__pos', dlg);
    var current = 0;
    var show = function (i) {
      current = (i + shots.length) % shots.length;
      var s = shots[current], im = $('img', s);
      limg.src = s.dataset.full;
      limg.alt = im ? im.alt : '';
      lcap.textContent = s.dataset.caption || (im ? im.alt : '');
      lpos.textContent = (current + 1) + ' / ' + shots.length + ' · use ← → to browse';
    };
    shots.forEach(function (s, i) {
      s.addEventListener('click', function () { show(i); dlg.showModal(); });
    });
    $('.lightbox__close', dlg).addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') show(current + 1);
      if (e.key === 'ArrowLeft') show(current - 1);
    });
  }

  /* ---------- Videos: play only while visible, never for reduced motion ---------- */

  $$('video[data-autoplay]').forEach(function (v) {
    var btn = v.parentElement && v.closest('figure') ? $('[data-video-toggle]', v.closest('figure')) : null;
    var userPaused = reduce.matches;
    var setLabel = function () { if (btn) $('span', btn).textContent = v.paused ? 'Play the tour' : 'Pause'; };
    if (btn) {
      btn.hidden = false;
      btn.addEventListener('click', function () {
        if (v.paused) { userPaused = false; v.play(); } else { userPaused = true; v.pause(); }
      });
      v.addEventListener('play', setLabel); v.addEventListener('pause', setLabel); setLabel();
    }
    if (!('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && !userPaused) {
          if (v.preload === 'none') v.preload = 'auto';
          var p = v.play(); if (p && p.catch) p.catch(function () {});
        } else if (!entry.isIntersecting) {
          v.pause();
        }
      });
    }, { threshold: 0.35 }).observe(v);
  });

  /* ---------- Clutch version, kept current from GitHub releases ---------- */

  var versionEls = $$('[data-clutch-version]');
  if (versionEls.length && window.fetch) {
    var paint = function (tag) { versionEls.forEach(function (el) { el.textContent = tag; }); };
    var cached = null;
    try { cached = sessionStorage.getItem('clutch-version'); } catch (e) {}
    if (cached) { paint(cached); }
    else {
      fetch('https://api.github.com/repos/KofiFS/clutch/releases/latest', { headers: { Accept: 'application/vnd.github+json' } })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (d) {
          if (d && typeof d.tag_name === 'string' && /^v?\d+\.\d+\.\d+$/.test(d.tag_name)) {
            var tag = d.tag_name.charAt(0) === 'v' ? d.tag_name : 'v' + d.tag_name;
            paint(tag);
            try { sessionStorage.setItem('clutch-version', tag); } catch (e) {}
          }
        })
        .catch(function () {});
    }
  }

  /* ---------- Contact form (/start) ---------- */

  var form = $('#brief');
  if (form) {
    var TO = 'kofifshang@gmail.com';
    var EMAIL_OK = /^[^\s@<>(),;:"\[\]\\]+@[^\s@<>(),;:"\[\]\\]+\.[^\s@<>(),;:"\[\]\\]{2,}$/;
    var t0 = Date.now();
    var status = $('.form__status', form);
    var submit = $('button[type="submit"]', form);
    var submitLabel = $('.btn__label', submit);
    var sent = $('#sent');
    var defaultHint = status.textContent;

    var fieldErr = function (name, msg) {
      var input = form.elements[name];
      var err = $('#' + name + '-err');
      if (input && input.setAttribute) input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (err) err.textContent = msg || '';
    };
    var setStatus = function (msg, isError) {
      status.textContent = msg;
      status.classList.toggle('is-error', !!isError);
    };
    var validate = function () {
      var bad = null;
      var v = function (n) { return (form.elements[n].value || '').trim(); };
      fieldErr('name', ''); fieldErr('email', ''); fieldErr('detail', '');
      if (!v('detail')) { fieldErr('detail', 'A few sentences about the problem, please.'); bad = 'detail'; }
      if (!v('email')) { fieldErr('email', 'I need somewhere to reply.'); bad = 'email'; }
      else if (!EMAIL_OK.test(v('email'))) { fieldErr('email', 'That email address doesn’t look right.'); bad = 'email'; }
      if (!v('name')) { fieldErr('name', 'What should I call you?'); bad = 'name'; }
      return bad;
    };

    // Validate a field once the visitor leaves it, not while they type.
    ['name', 'email', 'detail'].forEach(function (n) {
      form.elements[n].addEventListener('blur', function () {
        if (form.elements[n].getAttribute('aria-invalid') === 'true') validate();
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (submit.getAttribute('aria-busy') === 'true') return;
      var bad = validate();
      if (bad) {
        setStatus('Name, email and a description of the problem, please. The rest is optional.', true);
        form.elements[bad].focus();
        return;
      }
      var data = {};
      ['name', 'email', 'company', 'timeline', 'budget', 'detail', 'website'].forEach(function (k) {
        data[k] = (form.elements[k] && form.elements[k].value) || '';
      });
      var kind = form.querySelector('input[name="kind"]:checked');
      data.kind = kind ? kind.value : '';
      data.elapsed = Date.now() - t0;

      submit.setAttribute('aria-busy', 'true');
      submitLabel.textContent = 'Sending…';
      setStatus('Sending your brief…', false);

      fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (res) {
        return res.json().catch(function () { return {}; }).then(function (body) { return { ok: res.ok && body.ok, body: body }; });
      }).then(function (r) {
        submit.removeAttribute('aria-busy');
        submitLabel.textContent = 'Send to Kofi';
        if (r.ok) {
          var first = data.name.trim().split(/\s+/)[0];
          $('#sent-title').textContent = first ? 'Thanks, ' + first + '. It’s in my inbox.' : 'Thanks. It’s in my inbox.';
          form.hidden = true;
          sent.hidden = false;
          sent.focus();
        } else {
          var why = r.body && r.body.error ? r.body.error + ' ' : 'Something went wrong on my end. ';
          setStatus(why + 'You can also write to ' + TO + '.', true);
        }
      }).catch(function () {
        submit.removeAttribute('aria-busy');
        submitLabel.textContent = 'Send to Kofi';
        setStatus('Couldn’t reach the server. Check your connection, or write to ' + TO + '.', true);
      });
    });

    var again = $('#send-another');
    if (again) again.addEventListener('click', function () {
      form.reset();
      t0 = Date.now();
      setStatus(defaultHint, false);
      sent.hidden = true;
      form.hidden = false;
      form.elements.name.focus();
    });
  }

  /* ---------- Small things ---------- */

  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
