# Shared fragments for kofifshang.dev pages. Output is plain static HTML.
import json

SITE = "https://kofifshang.dev"
EMAIL = "kofifshang@gmail.com"
CLUTCH_DL = "https://github.com/KofiFS/clutch/releases/latest/download/Clutch-Setup.exe"
CLUTCH_REPO = "https://github.com/KofiFS/clutch"
JUICI_STEAM = "https://store.steampowered.com/app/5087380/"
ICSY_STEAM = "https://store.steampowered.com/app/5267160/"
FQ_STEAM = "https://store.steampowered.com/app/4895890/"
STEAM_PUB = "https://store.steampowered.com/search/?publisher=ShangkoStudio"
GITHUB = "https://github.com/KofiFS"
LINKEDIN = "https://www.linkedin.com/in/kofi-shang/"

def icon(name, cls="btn__icon"):
    paths = {
        "right": '<path d="M3 8h10M9 4l4 4-4 4"/>',
        "out": '<path d="M5 11l6-6M6.5 5H11v4.5"/>',
        "down": '<path d="M8 3v10M4 9l4 4 4-4"/>',
        "download": '<path d="M8 2.5v8M4.5 7 8 10.5 11.5 7M3 13.5h10"/>',
        "copy": '<rect x="5.5" y="5.5" width="7.5" height="7.5" rx="1.5"/><path d="M3 10.5V4a1 1 0 0 1 1-1h6.5"/>',
        "up": '<path d="M8 13V3M4 7l4-4 4 4"/>',
        "play": '<path d="M5 3.5v9l7-4.5z"/>',
        "check": '<path d="M3.5 8.5l3 3 6-7"/>',
    }
    extra = {"right": " btn__icon--right", "out": " btn__icon--out", "down": " btn__icon--down"}.get(name, "") if cls == "btn__icon" else ""
    return (f'<svg class="{cls}{extra}" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')

def ext(href, text, cls="more more--out"):
    return f'<a class="{cls}" href="{href}" rel="noopener">{text} {icon("out", "")}</a>'

def head(title, desc, path, image="/assets/og.jpg", tint=None, extra_head="", jsonld=None):
    url = SITE + path
    tint_style = ""
    if tint:
        tint_style = f'\n<style>:root{{--tint:{tint[0]};--tint-lit:{tint[1]};--tint-glow:{tint[2]}}}</style>'
    ld = ""
    if jsonld:
        ld = '\n<script type="application/ld+json">\n' + json.dumps(jsonld, indent=2, ensure_ascii=False) + '\n</script>'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/favicon.png" type="image/png" sizes="180x180">
<link rel="apple-touch-icon" href="/assets/favicon.png">
<meta name="theme-color" content="#08080A">
<meta name="color-scheme" content="dark">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Kofi Shang">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image">

<script>document.documentElement.classList.add('js')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;500&amp;family=Zen+Old+Mincho:wght@400;700&amp;display=swap">
<link rel="stylesheet" href="/styles.css">
<script src="/site.js" defer></script>{tint_style}{extra_head}{ld}
</head>
<body>

<a class="skip" href="#main">Skip to content</a>
'''

NAV_ITEMS = [("work", "/work", "Work"), ("games", "/games", "Games"), ("about", "/about", "About")]

def nav(active=None, solid=False):
    def cur(k):
        return ' aria-current="page"' if k == active else ""
    links = "\n".join(f'      <a class="nav__link" href="{h}"{cur(k)}>{t}</a>' for k, h, t in NAV_ITEMS)
    menu_items = [("home", "/", "Home"), *NAV_ITEMS, ("contact", "/start", "Contact")]
    mlinks = "\n".join(
        f'      <a href="{h}"{cur(k)} style="--i:{i}">{t}<span>0{i + 1}</span></a>' for i, (k, h, t) in enumerate(menu_items))
    return f'''
<header class="nav{' nav--solid' if solid else ''}">
  <div class="wrap wrap--wide nav__inner">
    <a class="brand" href="/" aria-label="Kofi Shang, home">
      <img src="/logo-white.png" alt="" width="30" height="30">
      <span class="brand__name"><b>Kofi Shang</b><span>Shangko Co</span></span>
    </a>
    <nav class="nav__links" aria-label="Primary">
      <span class="nav__pill" aria-hidden="true"></span>
{links}
      <a class="btn btn--light btn--sm nav__cta" href="/start"{cur("contact")}>Get in touch</a>
    </nav>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="menu" aria-label="Open menu"><span></span><span></span></button>
  </div>
</header>

<div class="menu" id="menu" aria-hidden="true">
  <nav class="menu__links" aria-label="Menu">
{mlinks}
  </nav>
  <div class="menu__foot">
    <a class="btn btn--primary" href="/start">Start a project {icon("right")}</a>
    <div class="menu__social">
      <a href="{GITHUB}" rel="noopener">GitHub</a>
      <a href="{STEAM_PUB}" rel="noopener">Steam</a>
      <a href="{LINKEDIN}" rel="noopener">LinkedIn</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</div>
'''

def foot():
    o = icon("out", "")
    return f'''
<footer class="foot">
  <div class="wrap wrap--wide">
    <div class="foot__grid">
      <div class="foot__brand">
        <a class="brand" href="/" aria-label="Kofi Shang, home">
          <img src="/logo-white.png" alt="" width="30" height="30">
          <span class="brand__name"><b>Kofi Shang</b><span>Shangko Co</span></span>
        </a>
        <p>Software engineer and independent game developer, building products and games under Shangko Co from Pennsylvania.</p>
      </div>
      <nav class="foot__col" aria-labelledby="f-site">
        <h2 id="f-site">Site</h2>
        <a href="/">Home</a>
        <a href="/work">Work</a>
        <a href="/games">Games</a>
        <a href="/about">About</a>
        <a href="/start">Contact</a>
      </nav>
      <nav class="foot__col" aria-labelledby="f-work">
        <h2 id="f-work">Case studies</h2>
        <a href="/work/clutch">Clutch</a>
        <a href="/work/juicicora">Juicicora</a>
        <a href="/work/i-cant-see-you">I Can't See You</a>
        <a href="/work/forest-quest-88">Forest Quest '88</a>
      </nav>
      <nav class="foot__col" aria-labelledby="f-else">
        <h2 id="f-else">Elsewhere</h2>
        <a href="{GITHUB}" rel="noopener">GitHub {o}</a>
        <a href="{STEAM_PUB}" rel="noopener">Steam {o}</a>
        <a href="{LINKEDIN}" rel="noopener">LinkedIn {o}</a>
        <a href="mailto:{EMAIL}">Email</a>
      </nav>
    </div>
    <svg class="foot__word" viewBox="0 0 1000 180" aria-hidden="true" focusable="false"><text x="0" y="160" textLength="1000" lengthAdjust="spacingAndGlyphs">Kofi Shang</text></svg>
    <div class="foot__bar">
      <span>© <span data-year>2026</span> Kofi Shang · Shangko Co</span>
      <span>Built by hand: no framework, no build step.</span>
      <a href="#main">Back to top {icon("up", "")}</a>
    </div>
  </div>
</footer>

</body>
</html>
'''

def cta(heading='Tell me what you’re <em>building.</em>'):
    return f'''
<section class="cta" id="contact" aria-labelledby="cta-title">
  <img class="cta__mark" src="/logo-white.png" alt="" aria-hidden="true" width="320" height="320" loading="lazy">
  <div class="wrap">
    <div class="cta__inner">
      <p class="label label--tint" data-reveal>Work with me</p>
      <h2 id="cta-title" data-reveal style="--i:1">{heading}</h2>
      <p data-reveal style="--i:2">I take on contract engineering, game development and release work, and AI products that have to hold up with real users. Send a paragraph about the problem and I’ll tell you honestly whether I’m the right person for it.</p>
      <div class="cta__row" data-reveal style="--i:3">
        <a class="btn btn--primary" href="/start">Start a project {icon("right")}</a>
        {copybox()}
      </div>
      <p class="cta__note" data-reveal style="--i:4">I read every enquiry myself and reply within two business days.</p>
    </div>
  </div>
</section>
'''

def copybox():
    return (f'<div class="copy"><a href="mailto:{EMAIL}">{EMAIL}</a>'
            f'<button type="button" data-copy="{EMAIL}" aria-label="Copy email address">{icon("copy", "")}<span>Copy</span></button></div>')

def img(src, alt, w, h, sizes="100vw", lazy=True, cls="", widths=None, priority=False):
    """src without width suffix, e.g. /assets/work/juicicora/home (expects -960 / -1600 variants) or a full path."""
    attrs = []
    if widths:
        srcset = ", ".join(f"{src}-{x}.webp {x}w" for x in widths)
        attrs.append(f'src="{src}-{widths[-1]}.webp" srcset="{srcset}" sizes="{sizes}"')
    else:
        attrs.append(f'src="{src}"')
    attrs.append(f'alt="{alt}" width="{w}" height="{h}"')
    if lazy and not priority:
        attrs.append('loading="lazy" decoding="async"')
    if priority:
        attrs.append('fetchpriority="high"')
    if cls:
        attrs.append(f'class="{cls}"')
    return "<img " + " ".join(attrs) + ">"

def shot(src, alt, caption, cls="", widths=(960, 1600), w=1600, h=900):
    big = f"{src}-{widths[-1]}.webp"
    return (f'<button class="shot {cls}" type="button" data-full="{big}" data-caption="{caption}" data-reveal="scale">'
            f'{img(src, alt, w, h, sizes="(max-width: 860px) 100vw, 50vw", widths=widths)}'
            f'<span class="shot__cap pill">{caption}</span></button>')

def shead(num, label, title, text=None, tag="h2", hid=None):
    p = f"\n      <p>{text}</p>" if text else ""
    idattr = f' id="{hid}"' if hid else ""
    return f'''
    <header class="shead">
      <div class="shead__rail" data-reveal="fade"><span class="shead__num">{num}</span><span class="label">{label}</span></div>
      <div class="shead__body" data-reveal>
        <{tag}{idattr}>{title}</{tag}>{p}
      </div>
    </header>'''
