from parts import *
from home import GAMES, TOOLS

def phero(label, title, text, num=None):
    rail = f'<span class="shead__num">{num}</span>' if num else ""
    return f'''
<section class="phero">
  <div class="hero__guides" aria-hidden="true"></div>
  <div class="hero__light hero__light--a" aria-hidden="true"></div>
  <div class="wrap phero__inner">
    <div class="shead__rail" data-reveal="fade">{rail}<span class="label">{label}</span></div>
    <div class="phero__body">
      <h1 data-reveal>{title}</h1>
      <p data-reveal style="--i:1">{text}</p>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------- /work

CASES = [
    ("clutch", "Clutch", "Desktop app · Out now",
     "A free, open-source game clip recorder for Windows that you can tell what to clip. GPU capture into a ring buffer, clips that save instantly, and triggers that need no AI.",
     ["Electron", "React", "TypeScript", "FFmpeg"], "/assets/work/clutch/library", (960, 1440), 1440, 810,
     "The Clutch library with clips sorted by game", ("#26BBFF", "#7CD6FF", "rgba(38,187,255,.4)")),
    ("juicicora", "Juicicora", "Game · Early Access, Dec 2027",
     "A cosy co-op adventure for up to five players in Unreal Engine 5.6: a juice press that turns fruit into powers, twenty villagers with their own days, and missions out at sea.",
     ["Unreal Engine 5.6", "C++", "Multiplayer"], "/assets/work/juicicora/g-square", (960, 1600), 1600, 900,
     "Juicicora: Souls in the stone plaza under a ruined arch", ("#5EC8F2", "#9BE0FF", "rgba(94,200,242,.4)")),
    ("i-cant-see-you", "I Can't See You", "Game · Launched Oct 2026",
     "A multiplayer shooter in total darkness. The interesting part is the hearing system: a server-side noise bus that decides exactly what each player gets to hear.",
     ["Unreal Engine 5.5", "C++", "Steam networking"], None, None, 1024, 384,
     "I Can't See You key art", ("#E5322D", "#FF7A75", "rgba(229,50,45,.4)")),
    ("forest-quest-88", "Forest Quest '88", "Game · Launched Oct 2026",
     "A comedy text adventure that started with a local AI narrator and shipped as a 372-node story graph with no AI at runtime, wrapped in Tauri for Steam.",
     ["Vite", "JavaScript", "Tauri", "Rust"], "/assets/work/forest-quest-88/journey", (960, 1600), 1600, 900,
     "Forest Quest '88 gameplay on a green CRT", ("#3DFF6E", "#8DFFA8", "rgba(61,255,110,.3)")),
]

def work():
    items = []
    for i, (slug, title, label, text, tags, src, widths, w, h, alt, tint) in enumerate(CASES):
        if src:
            media = img(src, alt, w, h, sizes="(max-width: 860px) 100vw, 60vw", widths=widths)
        else:
            media = f'<img src="/assets/work/i-cant-see-you/header.webp" alt="{alt}" width="1024" height="384" loading="lazy" decoding="async" style="object-fit:contain;background:#000">'
        tg = "".join(f'<span class="tag">{t}</span>' for t in tags)
        items.append(f'''
      <a class="case" href="/work/{slug}" style="--case-tint:{tint[0]};--case-lit:{tint[1]};--case-glow:{tint[2]}">
        <div class="case__media" data-reveal="scale"{' style="background:#000"' if not src else ''}>{media}</div>
        <div class="case__body" data-reveal style="--i:1">
          <span class="case__num">0{i + 1} / 04 · {label}</span>
          <h2>{title}</h2>
          <p>{text}</p>
          <div class="tags">{tg}</div>
          <span class="more">Read the case study {icon("right", "")}</span>
        </div>
      </a>''')
    return head("Work — Kofi Shang",
                "Case studies by Kofi Shang: Clutch, an open-source clip recorder; Juicicora, a co-op adventure in Unreal Engine; and the games I Can't See You and Forest Quest '88.",
                "/work") + nav("work") + f'''
<main id="main">
{phero("Work", "Products, games and the <em>engineering</em> behind them.", "Four case studies: two products in active development and two games launched this October. Each covers what the thing is, what I built, and the decisions I would walk another engineer through.")}

<section class="section section--flush-top" aria-label="Case studies">
  <div class="wrap">
    <div class="cases">{"".join(items)}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="tools-title">
  <div class="wrap">
    {shead("05", "Tools", "Things I built for myself first.", "Not everything needs a case study. These are smaller projects, each written because I needed it.", hid="tools-title")}
    {TOOLS}
    <div class="ledger__foot" style="margin-top:var(--s-7)">
      <a class="more" href="/games">See all nine games on Steam {icon("right", "")}</a>
    </div>
  </div>
</section>

{cta()}
</main>
''' + foot()

# ---------------------------------------------------------------- /games

def games():
    cards = []
    for slug, title, year, genre, price, url, short, tags, cs in GAMES:
        href = cs or url
        rel = "" if cs else ' rel="noopener"'
        go = f'Case study {icon("right", "")}' if cs else f'Steam {icon("out", "")}'
        badge = ""
        if "upcoming" in tags:
            badge = '<span class="title__badge pill">Wishlist now</span>'
        elif year == "2026" and slug in ("i-cant-see-you", "forest-quest-88"):
            badge = '<span class="title__badge pill pill--live"><span class="dot"></span>New</span>'
        feature = slug == "juicicora"
        art = ('<img src="/assets/work/juicicora/g-drip-960.webp" srcset="/assets/work/juicicora/g-drip-960.webp 960w, /assets/work/juicicora/g-drip-1600.webp 1600w" sizes="(max-width: 600px) 100vw, 66vw" alt="Juicicora: two Souls in a golden autumn meadow" width="1600" height="900" loading="lazy" decoding="async">'
               if feature else f'<img src="/assets/games/{slug}.jpg" alt="{title} cover art" width="460" height="215" loading="lazy" decoding="async">')
        cards.append(f'''
      <a class="title{' title--feature' if feature else ''}" href="{href}"{rel} data-tags="{tags}">
        <div class="title__art">{badge}{art}</div>
        <div class="title__body">
          <div class="title__row"><h3>{title}</h3><span class="title__year">{year}</span></div>
          <p>{short}</p>
          <div class="title__foot"><span>{genre} · <b>{price}</b></span><span class="title__go">{go}</span></div>
        </div>
      </a>''')
    filters = [("all", "All"), ("multiplayer", "Multiplayer & co-op"), ("comedy", "Comedy"), ("action", "Action & arcade"), ("upcoming", "In development")]
    fb = "\n".join(f'      <button class="filter" type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t} <small></small></button>' for k, t in filters)
    return head("Games — Kofi Shang",
                "Every game Kofi Shang has developed and published on Steam as ShangkoStudio, from Slimey in 2020 to I Can't See You and Forest Quest '88 in 2026, plus Juicicora in development.",
                "/games", image="/assets/og.jpg") + nav("games") + f'''
<main id="main">
{phero("Games", "Nine games on Steam, and a <em>tenth</em> on the way.", "Everything here was developed and published by me as ShangkoStudio, starting with Slimey in 2020. Filter by type, or open any title on Steam.")}

<section class="section section--flush-top" aria-label="Catalogue">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter games" hidden>
{fb}
      <span class="filters__count" aria-live="polite"></span>
    </div>
    <div class="shelf">{"".join(cards)}
      <div class="extras" data-extras>
        <p class="label">Also on Steam</p>
        <h3>Extras</h3>
        <ul>
          <li>LIGHT FORCE Demo <b>Free</b></li>
          <li>Tiny Man’s Revenge OST <b>$1.99</b></li>
        </ul>
        {ext(STEAM_PUB, "ShangkoStudio on Steam")}
      </div>
    </div>
  </div>
</section>

{cta()}
</main>
''' + foot()

# ---------------------------------------------------------------- /about

def about():
    o = icon("out", "")
    return head("About — Kofi Shang",
                "Kofi Shang is a software engineer with ten years of backend, data and platform work, and the founder of Shangko Co, an independent studio with nine games on Steam.",
                "/about", image="/assets/og.jpg") + nav("about") + f'''
<main id="main">
<section class="phero">
  <div class="hero__guides" aria-hidden="true"></div>
  <div class="hero__light hero__light--a" aria-hidden="true"></div>
  <div class="wrap about-hero">
    <div class="phero__body">
      <p class="label" data-reveal="fade">About</p>
      <h1 data-reveal>Engineer by trade. Game developer by <em>choice</em>.</h1>
      <p data-reveal style="--i:1">I’m Kofi Shang. I spend my days on the parts of software nobody notices until they break, and the rest of my time making things people play and use: nine games on Steam, a clip recorder, and a co-op adventure in Unreal Engine.</p>
      <div class="btn-row" data-reveal style="--i:2">
        <a class="btn btn--primary" href="/start">Get in touch {icon("right")}</a>
        <a class="btn btn--ghost" href="{LINKEDIN}" rel="noopener">LinkedIn {icon("out")}</a>
      </div>
    </div>
    <figure class="portrait" data-reveal="scale" style="--i:1">
      <img src="/assets/portrait.jpg" alt="Portrait of Kofi Shang in round glasses and a grey suit" width="400" height="400" fetchpriority="high">
      <figcaption><span class="pill">Pennsylvania · remote</span></figcaption>
    </figure>
  </div>
</section>

<section class="section" aria-labelledby="story-title">
  <div class="wrap cs-block">
    <div class="cs-block__rail" data-reveal="fade"><span class="shead__num">01</span><span class="label">The short version</span></div>
    <div class="cs-block__body">
      <h2 class="sr-only" id="story-title">The short version</h2>
      <div class="cs-prose" data-reveal>
        <p class="big">For ten years I’ve built backend services, data pipelines and platform software that real organisations run on.</p>
        <p>All of it on contract, across very different domains: security access control, payment processing, energy analytics, real-time spatial systems, and federal statistical work as a subcontractor to the U.S. Census Bureau. Different stacks and different stakes, but the same job each time: understand the system, change it safely, and leave it easier to run.</p>
        <p><strong>Shangko Co</strong> is my studio, and it’s where that discipline goes into work with my own name on it. I’ve shipped games on Steam since 2020, nine of them now, as developer and publisher. In October 2026 I released Clutch, an open-source clip recorder for Windows, and two more games. Juicicora, a co-op adventure in Unreal Engine, is the biggest thing I’ve taken on.</p>
        <p>I hold an M.S. in Software Engineering from Penn State. I’m based in Pennsylvania and work remotely.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="domains-title">
  <div class="wrap">
    {shead("02", "Experience", "Where the ten years went.", "Contract engineering, mostly backend, data and platform work. These are the domains, in the order the work tends to come up in conversation.", hid="domains-title")}
    <ul class="domains">
      <li data-reveal="fade"><span>01</span>Security access control</li>
      <li data-reveal="fade"><span>02</span>Payment processing</li>
      <li data-reveal="fade"><span>03</span>Energy analytics</li>
      <li data-reveal="fade"><span>04</span>Real-time spatial systems</li>
      <li data-reveal="fade"><span>05</span>Federal statistics, as a subcontractor to the U.S. Census Bureau</li>
      <li data-reveal="fade"><span>06</span>Independent games and tools, as Shangko Co</li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="numbers-title">
  <div class="wrap">
    {shead("03", "Selected numbers", "Things I can point to.", "Real counts from shipped work, no vanity metrics.", hid="numbers-title")}
    <div class="numbers" data-reveal>
      <div><b>9</b><span>Games released on Steam, as developer and publisher</span></div>
      <div><b>8</b><span>Tagged Clutch releases in its first ten days, each installing itself</span></div>
      <div><b>95</b><span>Endings in Forest Quest ’88’s 372-node story graph</span></div>
      <div><b>10+</b><span>Years of professional software engineering</span></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="wrap">
    {shead("04", "How I build", "Four habits that show up in everything.", hid="how-title")}
    <div class="principles">
      <div data-reveal><h3>Ship, then keep shipping.</h3><p>Clutch went from first public release to v0.1.8 in under two weeks. Every update installs itself, and it never restarts in the middle of a game.</p></div>
      <div data-reveal style="--i:1"><h3>Measure, don’t guess.</h3><p>Clutch ships a benchmark script that totals CPU, memory and encoder load across every process it runs, so its performance claims come with numbers anyone can reproduce.</p></div>
      <div data-reveal><h3>Local first, honest about the cloud.</h3><p>Clutch records and stores on your PC with no telemetry, and Forest Quest ’88 runs with no AI at all. Anything that touches the network is opt-in and says so.</p></div>
      <div data-reveal style="--i:1"><h3>Tooling is part of the product.</h3><p>I Can’t See You generates its input mappings, Blueprints and test map from an idempotent Python script, so a fresh checkout rebuilds the same project every time. <a href="/work/i-cant-see-you">See how</a>.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="kit-title">
  <div class="wrap">
    {shead("05", "Toolkit", "What I reach for.", "Grouped by the kind of work, drawn from projects on this site.", hid="kit-title")}
    <div class="stack-groups">
      <div data-reveal><h3>Products</h3><div class="tags"><span class="tag">TypeScript</span><span class="tag">React</span><span class="tag">Electron</span><span class="tag">Node.js</span><span class="tag">Tailwind CSS</span><span class="tag">FFmpeg</span></div></div>
      <div data-reveal style="--i:1"><h3>Games</h3><div class="tags"><span class="tag">Unreal Engine 5</span><span class="tag">C++</span><span class="tag">Replicated multiplayer</span><span class="tag">Steamworks</span><span class="tag">Unreal Python</span></div></div>
      <div data-reveal style="--i:2"><h3>Systems and tools</h3><div class="tags"><span class="tag">C# / .NET</span><span class="tag">Python</span><span class="tag">Rust (Tauri)</span><span class="tag">GitHub Actions</span><span class="tag">Cloudflare Workers</span></div></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="else-title">
  <div class="wrap">
    {shead("06", "Elsewhere", "Find me on.", hid="else-title")}
    <div class="profiles" data-reveal>
      <a href="{GITHUB}" rel="noopener"><span>Code</span><b>GitHub {o}</b></a>
      <a href="{LINKEDIN}" rel="noopener"><span>Career</span><b>LinkedIn {o}</b></a>
      <a href="{STEAM_PUB}" rel="noopener"><span>Games</span><b>Steam {o}</b></a>
      <a href="mailto:{EMAIL}"><span>Direct</span><b>Email {o}</b></a>
    </div>
  </div>
</section>

{cta()}
</main>
''' + foot()

# ---------------------------------------------------------------- /start

def start():
    kinds = ["Backend / platform engineering", "Full stack product work", "Game development or release",
             "AI product, end to end", "Full-time role", "Something else"]
    chips = "\n".join(f'            <label class="chip"><input type="radio" name="kind" value="{k}"><span>{k}</span></label>' for k in kinds)
    return head("Start a project — Kofi Shang",
                "Tell Kofi Shang what you are building. Your brief goes straight to his inbox: contract engineering, game development, AI products or a full-time role.",
                "/start", image="/assets/og.jpg") + nav("contact", solid=True) + f'''
<main id="main">
<section class="phero" style="padding-bottom:var(--section)">
  <div class="hero__light hero__light--a" aria-hidden="true"></div>
  <div class="wrap contact-grid">
    <div class="contact-aside">
      <p class="label label--tint" data-reveal="fade">Start a project</p>
      <h1 data-reveal>Tell me what you’re building.</h1>
      <p data-reveal style="--i:1">Six questions. Answer what you know and leave the rest: a paragraph about the actual problem is worth more than a filled-in budget field.</p>
      <ol class="steps" data-reveal style="--i:2">
        <li><span>01</span>Your brief goes straight to my inbox. No email app needed.</li>
        <li><span>02</span>I read every one myself.</li>
        <li><span>03</span>You get a reply within two business days, including the honest no.</li>
      </ol>
      <div class="direct" data-reveal style="--i:3">
        <span class="label">Or skip the form</span>
        {copybox()}
        <span class="cta__note">Remote, United States. Based in Pennsylvania.</span>
      </div>
    </div>

    <div data-reveal="scale" style="--i:1">
      <noscript><p class="form__status" style="margin-bottom:1rem">The form needs JavaScript. You can write to <a href="mailto:{EMAIL}">{EMAIL}</a> instead.</p></noscript>
      <form class="form" id="brief" novalidate aria-describedby="form-status">
        <label class="hp" aria-hidden="true"><span>Leave this field empty</span><input name="website" tabindex="-1" autocomplete="off"></label>

        <div class="form__row">
          <label class="field" for="name">
            <span>Your name <span class="req" aria-hidden="true">*</span></span>
            <input class="input" id="name" name="name" autocomplete="name" placeholder="Jordan Ellis" required maxlength="120" aria-describedby="name-err">
            <span class="field__err" id="name-err" role="alert"></span>
          </label>
          <label class="field" for="email">
            <span>Email <span class="req" aria-hidden="true">*</span></span>
            <input class="input" id="email" name="email" type="email" inputmode="email" autocomplete="email" placeholder="jordan@company.com" required maxlength="254" aria-describedby="email-err">
            <span class="field__err" id="email-err" role="alert"></span>
          </label>
        </div>

        <label class="field" for="company">
          <span>Company or project <span class="opt">(optional)</span></span>
          <input class="input" id="company" name="company" autocomplete="organization" placeholder="Northwind Energy" maxlength="160">
        </label>

        <fieldset class="field">
          <legend>What kind of work <span class="opt">(optional)</span></legend>
          <div class="chips">
{chips}
          </div>
        </fieldset>

        <div class="form__row">
          <label class="field" for="timeline">
            <span>Timeline <span class="opt">(optional)</span></span>
            <input class="input" id="timeline" name="timeline" placeholder="Kick off next month, ship by Q2" maxlength="160">
          </label>
          <label class="field" for="budget">
            <span>Budget range <span class="opt">(optional)</span></span>
            <input class="input" id="budget" name="budget" placeholder="A rough band is fine" maxlength="120">
          </label>
        </div>

        <label class="field" for="detail">
          <span>The problem <span class="req" aria-hidden="true">*</span></span>
          <textarea class="input" id="detail" name="detail" rows="7" required maxlength="8000" aria-describedby="detail-hint detail-err" placeholder="What are you building, what is in the way, and what does done look like?"></textarea>
          <span class="field__hint" id="detail-hint">Your existing stack and team size help too.</span>
          <span class="field__err" id="detail-err" role="alert"></span>
        </label>

        <div class="form__foot">
          <button class="btn btn--primary" type="submit"><span class="btn__label">Send to Kofi</span><span class="spin" aria-hidden="true"></span>{icon("right")}</button>
          <p class="form__status" id="form-status" role="status" aria-live="polite">Fields marked * are required. Goes straight to my inbox.</p>
        </div>
      </form>

      <div class="sent" id="sent" tabindex="-1" hidden>
        <span class="sent__icon">{icon("check", "")}</span>
        <p class="label label--tint">Message sent</p>
        <h2 id="sent-title">Thanks. It’s in my inbox.</h2>
        <p>I read every enquiry myself and reply within two business days, including the honest no. My reply comes from {EMAIL}, so check your spam folder if you don’t see it.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="/">Back to the site {icon("right")}</a>
          <button class="btn btn--ghost" type="button" id="send-another">Send another</button>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
''' + foot()

# ---------------------------------------------------------------- 404

def notfound():
    return head("Page not found — Kofi Shang", "That page doesn't exist on kofifshang.dev.", "/404", extra_head='\n<meta name="robots" content="noindex">') + nav() + f'''
<main id="main">
<section class="phero" style="min-height:80vh">
  <div class="hero__guides" aria-hidden="true"></div>
  <div class="hero__light hero__light--a" aria-hidden="true"></div>
  <div class="wrap phero__inner">
    <div class="shead__rail"><span class="shead__num">404</span><span class="label">Not found</span></div>
    <div class="phero__body">
      <h1>The forest rearranged <em>itself</em>.</h1>
      <p>That page doesn’t exist, or it moved. Everything worth finding is one of these:</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="/">Home {icon("right")}</a>
        <a class="btn btn--ghost" href="/work">Work</a>
        <a class="btn btn--ghost" href="/games">Games</a>
        <a class="btn btn--ghost" href="/start">Contact</a>
      </div>
    </div>
  </div>
</section>
</main>
''' + foot()
