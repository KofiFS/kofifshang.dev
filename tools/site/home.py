from parts import *

GAMES = [
    # slug, title, year, genre, price, steam url, short, tags, case study
    ("juicicora", "Juicicora", "2027", "Co-op adventure", "Coming soon", JUICI_STEAM,
     "A cosy co-op creature adventure on the island of Elyndor, for up to five players.", "multiplayer upcoming", "/work/juicicora"),
    ("i-cant-see-you", "I Can't See You", "2026", "Multiplayer shooter", "$5.99", ICSY_STEAM,
     "Multiplayer shooting in the pitch dark, where sound is the only thing that finds you.", "multiplayer action", "/work/i-cant-see-you"),
    ("forest-quest-88", "Forest Quest '88", "2026", "Comedy text adventure", "$1.99", FQ_STEAM,
     "A text adventure that lies to you, on a green CRT, with 95 ways to end badly.", "comedy", "/work/forest-quest-88"),
    ("light-force", "LIGHT FORCE", "2026", "Arcade physics runner", "$4.99", "https://store.steampowered.com/app/3990550/",
     "An arcade physics runner built on one move: hold to charge, release to dash.", "action", None),
    ("monkey-see", "Monkey See, Monkey Doo, Monkey Kiss You", "2026", "Co-op horror", "$7.99", "https://store.steampowered.com/app/2899880/",
     "First-person horror through a forest, chased by relentlessly amorous monkeys.", "multiplayer comedy", None),
    ("tiny-mans-revenge", "Tiny Man's Revenge Remastered", "2023", "Comedy adventure", "$19.99", "https://store.steampowered.com/app/2349060/",
     "A shrunken billionaire robs a house to fund his beloved soup. Multiple endings.", "comedy", None),
    ("elite-comet", "Elite Comet", "2022", "Multiplayer space combat", "$0.99", "https://store.steampowered.com/app/2154710/",
     "Physics-driven space combat for up to ten players, where mass and momentum decide every collision.", "multiplayer action", None),
    ("meat-beating", "Meat Beating: The Second Coming", "2022", "Comedy clicker", "$0.99", "https://store.steampowered.com/app/2005490/",
     "A deadpan clicker with a robed man waiting to talk at you after every level.", "comedy", None),
    ("juicy-bois", "Juicy Bois: Conflict", "2021", "Online party game", "$0.99", "https://store.steampowered.com/app/1748090/",
     "Gelatinous characters race for gem chests, head to head or together, up to sixteen online.", "multiplayer", None),
    ("slimey", "Slimey", "2020", "Action platformer", "$0.99", "https://store.steampowered.com/app/1216560/",
     "The first one out the door. An action platformer with versus and co-op.", "multiplayer action", None),
]

def ledger():
    rows = []
    for slug, title, year, genre, price, url, short, tags, cs in GAMES:
        rows.append(f'''        <a class="ledger__row" href="{url}" rel="noopener" data-reveal="fade">
          <span class="ledger__thumb"><img src="/assets/games/{slug}.jpg" alt="" width="460" height="215" loading="lazy" decoding="async"></span>
          <span class="ledger__year">{year}</span>
          <span class="ledger__title">{title}</span>
          <span class="ledger__genre">{genre}</span>
          <span class="ledger__price">{price}</span>
          {icon("out", "ledger__arrow")}
          <span class="sr-only">(opens on Steam)</span>
        </a>''')
    return "\n".join(rows)

jsonld = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Kofi Shang",
    "jobTitle": "Software Engineer and Game Developer",
    "email": f"mailto:{EMAIL}",
    "url": SITE + "/",
    "image": SITE + "/assets/portrait.jpg",
    "worksFor": {"@type": "Organization", "name": "Shangko Co"},
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Penn State"},
    "address": {"@type": "PostalAddress", "addressRegion": "PA", "addressCountry": "US"},
    "sameAs": [GITHUB, LINKEDIN, STEAM_PUB],
}

def page():
    return head(
        "Kofi Shang — Software engineer and game developer",
        "Kofi Shang is a software engineer and independent game developer. He builds Clutch, a free open-source clip recorder for Windows, and Juicicora, a co-op adventure in Unreal Engine, with nine games already on Steam.",
        "/", jsonld=jsonld,
        extra_head='\n<link rel="preload" as="image" href="/assets/work/clutch/home-960.webp" fetchpriority="high">',
    ) + nav() + f'''
<main id="main">

<!-- ============================ HERO ============================ -->
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__guides" aria-hidden="true"></div>
  <div class="hero__light hero__light--a" aria-hidden="true"></div>
  <div class="hero__light hero__light--b" aria-hidden="true"></div>

  <div class="wrap hero__inner">
    <div class="hero__copy">
      <p class="label" data-enter style="--i:0">Software engineer · Game developer · Founder of Shangko Co</p>
      <h1 class="hero__name" id="hero-title" data-enter style="--i:1"><span>Kofi</span><span>Shang</span></h1>
      <p class="hero__headline" data-enter style="--i:2">I build real products end to end: <em>Clutch</em>, a clip recorder for Windows, <em>Juicicora</em>, a co-op adventure in Unreal, and nine games already on Steam.</p>
      <p class="hero__lede" data-enter style="--i:3">Ten years of backend and platform engineering inside other people’s production systems. Now the same discipline goes into work with my own name on it.</p>
      <div class="btn-row" data-enter style="--i:4">
        <a class="btn btn--primary" href="#work">Explore my work {icon("down")}</a>
        <a class="btn btn--ghost" href="/start">Get in touch {icon("right")}</a>
      </div>
    </div>

    <div class="stage" aria-hidden="true">
      <div class="stage__mark"><img src="/logo-white.png" alt="" width="320" height="320"></div>
      <div class="stage__card stage__card--back" data-enter style="--i:3">
        <img src="/assets/work/juicicora/home-960.webp" alt="" width="960" height="540" decoding="async">
      </div>
      <div class="stage__card stage__card--front" data-enter style="--i:2">
        <img src="/assets/work/clutch/home-960.webp" alt="" width="960" height="540" fetchpriority="high">
      </div>
      <div class="stage__card stage__card--chip" data-enter style="--i:5">
        <img src="/assets/games/i-cant-see-you.jpg" alt="" width="460" height="215" decoding="async">
      </div>
      <div class="stage__tag stage__tag--a" data-enter style="--i:6"><span class="pill pill--live"><span class="dot"></span>Clutch <span data-clutch-version>v0.1.8</span> · out now</span></div>
      <div class="stage__tag stage__tag--b" data-enter style="--i:7"><span class="pill">Juicicora · Dec 2027</span></div>
    </div>
  </div>

  <div class="wrap">
    <dl class="ledger-strip" data-enter style="--i:6">
      <div><dt>Clutch</dt><dd><span data-clutch-version>v0.1.8</span><small>Free and open source, out now</small></dd></div>
      <div><dt>Juicicora</dt><dd>December 2027<small>Steam Early Access, wishlist now</small></dd></div>
      <div><dt>On Steam</dt><dd>9 games<small>Released since 2020 as ShangkoStudio</small></dd></div>
      <div><dt>Engineering</dt><dd>10+ years<small>Backend, data and platform work</small></dd></div>
    </dl>
  </div>
</section>

<!-- ============================ SELECTED WORK ============================ -->
<section class="section" id="work" aria-labelledby="work-title">
  <span id="products" aria-hidden="true"></span>
  <div class="wrap">
    {shead("01", "Selected work", "Two products I’m building right now.", "One you can download today. The other is the deepest systems work I have going.", hid="work-title")}

    <article class="product" aria-labelledby="clutch-title" style="--tint:#26BBFF;--tint-lit:#7CD6FF;--tint-glow:rgba(38,187,255,.3)">
      <div class="product__head">
        <div class="product__title" data-reveal>
          <p class="label label--tint">Desktop app · Out now</p>
          <h3 id="clutch-title"><img src="/assets/clutch-icon.png" alt="" width="68" height="68" loading="lazy">Clutch</h3>
          <p>The game clip recorder you can tell what to clip. Light like NVIDIA’s recorder, social like Medal, with no ads you can’t turn off.</p>
        </div>
        <dl class="meta" data-reveal style="--i:1">
          <div><dt>Status</dt><dd>Out now · <span data-clutch-version>v0.1.8</span></dd></div>
          <div><dt>Platform</dt><dd>Windows 10 and 11</dd></div>
          <div><dt>Stack</dt><dd>Electron, React, TypeScript, FFmpeg</dd></div>
          <div><dt>License</dt><dd>GPL-3.0, free</dd></div>
        </dl>
      </div>

      <div class="product__media glow-host" data-reveal="scale">
        <div class="frame">
          {img("/assets/work/clutch/library", "The Clutch clip library: clips sorted by game with hover previews, filters by trigger and a search bar", 1440, 810, sizes="(max-width: 1320px) 100vw, 1200px", widths=(960, 1440))}
        </div>
        <div class="product__callout product__callout--a callout"><b>Hype moments</b>Clips when your friends get loud. No AI.</div>
        <div class="product__callout product__callout--b callout"><b>Medal, OBS and NVIDIA</b>Old clips read in place, nothing copied.</div>
      </div>

      <div class="trio">
        <div data-reveal><span>01</span><h4>An always-on replay buffer</h4><p>One FFmpeg process encodes on the GPU into two-second segments. Saving a clip stitches them by stream copy, so it is instant and never re-encodes.</p></div>
        <div data-reveal style="--i:1"><span>02</span><h4>Clips that make themselves</h4><p>Hype and conversation triggers run locally with no AI. If you want, describe what to keep in plain English and Clutch watches for it.</p></div>
        <div data-reveal style="--i:2"><span>03</span><h4>Your library, not a new silo</h4><p>Existing Medal, OBS and NVIDIA clips show up where they already are. A 9:16 editor, Discord posting and scheduled YouTube uploads are built in.</p></div>
      </div>

      <div class="product__foot" data-reveal>
        <div class="btn-row">
          <a class="btn btn--primary" href="{CLUTCH_DL}">Download for Windows {icon("download")}</a>
          <a class="btn btn--ghost" href="/work/clutch">Read the case study {icon("right")}</a>
        </div>
        <span class="label">8 tagged releases in its first 10 days</span>
      </div>
    </article>
  </div>
</section>

<section class="bleed" id="juicicora" aria-labelledby="juici-title" data-parallax style="--tint:#5EC8F2;--tint-lit:#9BE0FF">
  <div class="bleed__img" aria-hidden="true">
    {img("/assets/work/juicicora/home", "", 1600, 900, sizes="100vw", widths=(960, 1600))}
  </div>
  <div class="wrap bleed__content">
    <div class="bleed__copy" data-reveal>
      <p class="label label--tint">Game · Steam Early Access, December 2027</p>
      <h3 id="juici-title">Juicicora</h3>
      <p>A cosy co-op adventure. You are a Soul, a small, glossy, jelly-bodied creature on the island of Elyndor, squeezing fruit into powers and sailing out with friends to deal with whatever threatens home.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{JUICI_STEAM}" rel="noopener">Wishlist on Steam {icon("out")}</a>
        <a class="btn btn--ghost" href="/work/juicicora">Read the case study {icon("right")}</a>
      </div>
    </div>
    <div class="bleed__side" data-reveal style="--i:1">
      <ul class="ticks">
        <li>Online co-op for up to five players</li>
        <li>25 fruits, a juice press, and powers that mix or clash</li>
        <li>20 villagers with their own hours, homes and stories</li>
        <li>12 missions, two boss birds and a Challenge Mode</li>
        <li>A 25-day month with four seasons and weather</li>
      </ul>
      <div class="tags"><span class="tag">Unreal Engine 5.6</span><span class="tag">C++</span><span class="tag">Replicated multiplayer</span><span class="tag">Steamworks</span></div>
    </div>
  </div>
</section>

<div class="wrap" style="--tint-lit:#9BE0FF">
  <div class="strip">
    <figure data-reveal><div class="zoom">{img("/assets/work/juicicora/press", "A Soul standing beside the stone juice press", 1600, 900, sizes="(max-width: 860px) 100vw, 40vw", widths=(960, 1600))}</div><figcaption><b>The juice press</b><span>Fruit in, powers out</span></figcaption></figure>
    <figure data-reveal style="--i:1"><div class="zoom">{img("/assets/work/juicicora/souls", "Souls gathered in the village square among pots and crates", 1600, 900, sizes="(max-width: 860px) 50vw, 30vw", widths=(960, 1600))}</div><figcaption><b>Twenty souls</b><span>Each keeps their own day</span></figcaption></figure>
    <figure data-reveal style="--i:2"><div class="zoom">{img("/assets/work/juicicora/g-boat", "A Soul rowing a small wooden boat across dark water", 1600, 900, sizes="(max-width: 860px) 50vw, 30vw", widths=(960, 1600))}</div><figcaption><b>Sailing with Drip</b><span>Out to the Windward Spire</span></figcaption></figure>
  </div>
</div>

<!-- ============================ ALSO SHIPPING ============================ -->
<section class="section" id="recent" aria-labelledby="recent-title">
  <div class="wrap">
    {shead("02", "Also shipping", "Two launches this October.", "Both developed and published by me, nine days apart: one built on sound, the other on a green screen.", hid="recent-title")}
    <div class="duo">
      <a class="panel panel--icsy" href="/work/i-cant-see-you" data-reveal>
        <div class="panel__media"><img src="/assets/work/i-cant-see-you/header.webp" alt="I Can't See You key art: a robot with a head torch in a pitch-black corridor" width="1024" height="384" loading="lazy" decoding="async"></div>
        <div class="panel__body">
          <div class="panel__top"><p class="label label--tint">Launched 10 Oct 2026 · Early Access</p></div>
          <h3>I Can't See You</h3>
          <p>A multiplayer shooter played in total darkness for two to eight players. Every footstep, reload, shot and spoken word gives your position away.</p>
          <div class="panel__foot"><span class="label">Unreal Engine 5.5 · C++ · $5.99</span><span class="more">Case study {icon("right", "")}</span></div>
        </div>
      </a>
      <a class="panel panel--fq" href="/work/forest-quest-88" data-reveal style="--i:1">
        <div class="panel__media"><img src="/assets/work/forest-quest-88/opening-960.webp" alt="Forest Quest '88 running: green CRT text describing a golf course in the forest, with five numbered choices" width="960" height="540" loading="lazy" decoding="async"></div>
        <div class="panel__body">
          <div class="panel__top"><p class="label label--tint">Launched 1 Oct 2026</p></div>
          <h3>Forest Quest '88</h3>
          <p>A deadpan comedy text adventure on a green CRT. You just want to get home to bed. There are 95 ways that goes wrong.</p>
          <div class="panel__foot"><span class="label">Vite · Tauri · $1.99</span><span class="more">Case study {icon("right", "")}</span></div>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- ============================ CATALOGUE ============================ -->
<section class="section" id="games" aria-labelledby="games-title">
  <div class="wrap">
    {shead("03", "The catalogue", "Nine games on Steam, and a tenth on the way.", "Developed and published as ShangkoStudio, starting with Slimey in 2020. Every title opens its Steam page.", hid="games-title")}
    <div class="ledger">
{ledger()}
    </div>
    <div class="ledger__foot">
      <a class="more" href="/games">Browse them with filters {icon("right", "")}</a>
      <span class="label">Plus a free LIGHT FORCE demo and the Tiny Man’s Revenge soundtrack</span>
    </div>
  </div>
</section>

<!-- ============================ TOOLS ============================ -->
<section class="section" id="also" aria-labelledby="tools-title">
  <div class="wrap">
    {shead("04", "Tools", "Things I built for myself first.", "Smaller projects, each made because I needed it badly enough to write it.", hid="tools-title")}
    {TOOLS}
  </div>
</section>

<!-- ============================ ABOUT ============================ -->
<section class="section" id="about" aria-labelledby="about-title">
  <div class="wrap intro">
    <figure class="portrait" data-reveal="scale">
      <img src="/assets/portrait.jpg" alt="Portrait of Kofi Shang in round glasses and a grey suit" width="400" height="400" loading="lazy" decoding="async">
      <figcaption><span class="pill">Pennsylvania · remote</span></figcaption>
    </figure>
    <div class="intro__body">
      <div class="shead__rail" data-reveal="fade" style="border-top:0;padding-top:0;flex-direction:row;gap:1rem"><span class="shead__num" style="padding-top:0">05</span><span class="label">About</span></div>
      <h2 class="intro__quote" id="about-title" data-reveal>Ten years inside other people’s production systems, and a studio of my <em>own</em>.</h2>
      <p data-reveal style="--i:1">I’ve spent a decade building backend services, data pipelines and platform software on contract: security access control, payment processing, energy analytics, real-time spatial systems, and federal statistical work as a subcontractor to the U.S. Census Bureau. I hold an M.S. in Software Engineering from Penn State.</p>
      <div class="btn-row" data-reveal style="--i:2">
        <a class="btn btn--ghost" href="/about">More about me {icon("right")}</a>
        {ext(LINKEDIN, "LinkedIn")}
        {ext(GITHUB, "GitHub")}
      </div>
    </div>
  </div>
</section>

{cta()}
</main>
''' + foot()

TOOLS = f'''<div class="index">
      <div class="index__item" data-reveal><span class="index__num">01</span><h3>SysMon</h3><p>A dark, card-based replacement for Windows Task Manager that shows real sensors, temperatures, fan speeds and power draw, next to the usual graphs.</p><div class="index__foot"><span class="tag">C#</span><span class="tag">.NET 10</span><span class="tag">LibreHardwareMonitor</span></div></div>
      <div class="index__item" data-reveal style="--i:1"><span class="index__num">02</span><h3>Mirage</h3><p>A call copilot that stays invisible to screen sharing. It transcribes locally, works out who is speaking, and answers from your own notes.</p><div class="index__foot"><span class="tag">Electron</span><span class="tag">Local Whisper</span></div></div>
      <div class="index__item" data-reveal><span class="index__num">03</span><h3>D&amp;D Character Sheet</h3><p>An auto-saving fifth-edition sheet with the official rules built in, so it still works at the table with no signal.</p><div class="index__foot"><a class="more more--out" href="https://kofifs.github.io/DND/" rel="noopener">Open it {icon("out", "")}</a></div></div>
      <div class="index__item" data-reveal style="--i:1"><span class="index__num">04</span><h3>Risk-first trading agent</h3><p>A paper-only bot whose risk engine outranks the model: immutable limits, a daily-loss halt, and no code path that lets model output widen a limit.</p><div class="index__foot"><span class="tag">Python</span><span class="tag">Backtested</span><span class="tag">Paper only</span></div></div>
    </div>'''
