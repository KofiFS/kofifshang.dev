from parts import *

def cs_hero(crumb, label, title, lede, buttons, meta, tags):
    m = "\n".join(f'          <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in meta)
    tg = "".join(f'<span class="tag">{t}</span>' for t in tags)
    return f'''
<section class="cs-hero">
  <div class="hero__guides" aria-hidden="true"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb" data-reveal="fade"><a href="/work">Work</a><span aria-hidden="true">/</span><span aria-current="page">{crumb}</span></nav>
    <div class="cs-hero__grid">
      <div class="cs-hero__title">
        <p class="label label--tint" data-reveal="fade">{label}</p>
        <h1 data-reveal>{title}</h1>
        <p class="cs-hero__lede" data-reveal style="--i:1">{lede}</p>
        <div class="btn-row" data-reveal style="--i:2">{buttons}</div>
      </div>
      <div class="cs-hero__side" data-reveal style="--i:2">
        <dl class="meta">
{m}
        </dl>
        <div class="tags">{tg}</div>
      </div>
    </div>'''

def block(num, label, title, inner, hid):
    return f'''
<section class="section" aria-labelledby="{hid}">
  <div class="wrap cs-block">
    <div class="cs-block__rail" data-reveal="fade"><span class="shead__num">{num}</span><span class="label">{label}</span></div>
    <div class="cs-block__body">
      <h2 id="{hid}" data-reveal>{title}</h2>
      {inner}
    </div>
  </div>
</section>'''

def decisions(items):
    out = []
    for i, (title, paras) in enumerate(items):
        ps = "".join(f"<p>{p}</p>" for p in paras)
        out.append(f'''
      <div class="decision" data-reveal><span class="decision__num">{i + 1:02d}</span><h3>{title}</h3><div class="decision__body">{ps}</div></div>''')
    return '<div class="decisions">' + "".join(out) + "\n    </div>"

def feats(items):
    return '<div class="feats">' + "".join(
        f'<div data-reveal style="--i:{i % 3}"><span>{i + 1:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(items)) + "</div>"

def numbers(items, note=None):
    n = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items)
    cap = f'<p class="cs-media__cap" style="margin-top:.75rem"><span>{note}</span></p>' if note else ""
    return f'<div data-reveal><div class="numbers">{n}</div>{cap}</div>'

def links_block(items):
    a = "".join(f'<a href="{h}"{" rel=noopener" if h.startswith("http") else ""}><span>{k}</span><b>{t} {icon("out", "")}</b></a>' for k, t, h in items)
    return f'<div class="cs-links" data-reveal>{a}</div>'

def next_block(slug, title, text, image):
    return f'''
<a class="next" href="/work/{slug}">
  <div class="next__img" aria-hidden="true"><img src="{image}" alt="" width="1600" height="900" loading="lazy" decoding="async"></div>
  <div class="wrap next__inner">
    <span class="label">Next case study</span>
    <h2>{title} <svg viewBox="0 0 48 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h42M34 3l10 9-10 9"/></svg></h2>
    <p>{text}</p>
  </div>
</a>'''

def gallery(shots):
    return '<div class="gallery">' + "".join(shots) + "</div>"

def page(path, title, desc, tint, og, body):
    return head(title, desc, path, image=og, tint=tint) + nav("work") + '\n<main id="main">\n' + body + "\n</main>\n" + foot()

ARROW = '<svg class="pipe__arrow" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14h20M17 7l7 7-7 7"/></svg>'

# ================================================================= CLUTCH

def clutch():
    btns = (f'<a class="btn btn--primary" href="{CLUTCH_DL}">Download for Windows {icon("download")}</a>'
            f'<a class="btn btn--ghost" href="{CLUTCH_REPO}" rel="noopener">Source on GitHub {icon("out")}</a>')
    hero = cs_hero("Clutch", "Desktop app · Out now", "Clutch",
                   "The game clip recorder you can tell what to clip. Free and open source, for Windows.", btns,
                   [("Role", "Design, engineering and release. Sole maintainer"),
                    ("Status", 'Out now · <span data-clutch-version>v0.1.8</span>'),
                    ("Platform", "Windows 10 and 11"),
                    ("License", "GPL-3.0")],
                   ["Electron 37", "React 19", "TypeScript", "Tailwind CSS 4", "electron-vite", "FFmpeg", "electron-updater", "Node.js"])
    media = f'''
    <figure class="cs-media" data-reveal="scale">
      <div class="frame frame--glow glow-host">
        <video data-autoplay muted loop playsinline preload="none" poster="/assets/work/clutch/library-1440.webp" width="1280" height="720" aria-label="Clutch tour: the clip library, the player and the 9:16 editor">
          <source src="/assets/work/clutch/tour.mp4" type="video/mp4">
        </video>
      </div>
      <figcaption class="cs-media__cap">
        <span>From the one-minute tour: the library, the player and the 9:16 editor.</span>
        <span style="display:flex;gap:1.25rem;align-items:center">
          <button type="button" data-video-toggle hidden>{icon("play", "")}<span>Play the tour</span></button>
          <a href="{CLUTCH_REPO}/blob/main/docs/media/clutch-demo.mp4" rel="noopener">Full tour on GitHub</a>
        </span>
      </figcaption>
    </figure>
  </div>
</section>'''

    overview = block("01", "Overview", "Medal is social. NVIDIA’s recorder is light. Clutch sets out to be both.", '''
      <div class="cs-prose" data-reveal style="--i:1">
        <p>It sits in the tray running an always-on replay buffer. Press the hotkey and it keeps the last few seconds plus a few after, and you can change that length mid-game. Or press nothing: it can clip when you and your friends suddenly get loud, keep every stretch of conversation, or, with an optional AI step, watch for whatever you describe in plain English, like <em>“my kills and goals, never menus”</em>.</p>
        <p>Around that sits everything that makes clips worth keeping: a library with hover previews, search and tags, a viewer with trim handles, a 9:16 / 1:1 / 16:9 editor for Shorts and TikTok, Discord posting through a webhook, and YouTube uploads now or on a schedule.</p>
        <p><strong>Everything that runs on your PC is free, with no limits.</strong> An optional account adds cloud share links and storage, and an optional Pro tier pays for that cloud. Sponsored cards can be switched off in one place and never appear in game.</p>
      </div>''', "cs-overview")

    nums = f'''
<section class="section" aria-label="Clutch by the numbers">
  <div class="wrap">
    {numbers([("0.8%", "CPU for the whole Clutch app, all five processes"), ("0.7%", "CPU for the FFmpeg recording process"), ("2 s", "Segment length in the replay ring buffer"), ("8", "Tagged releases in the first ten days")],
             "Reference run from the README, measured with the bundled benchmark script: RTX 5090, 32 threads, 5120×1440 at 60 fps, main window open, plus a Discord-only audio track.")}
  </div>
</section>'''

    features = block("02", "Features", "What it does.", feats([
        ("Replay buffer and hotkeys", "Save the seconds before and after with one key. Alt+PageUp / PageDown change the length in game, and extra hotkeys can have their own lengths."),
        ("Clips that make themselves", "Hype moments and conversation triggers, both with no AI. Game detection starts recording on launch and tags each clip with the game’s icon."),
        ("Bring your old library", "Medal, OBS, NVIDIA or any folder shows up next to Clutch’s own clips, read where it already is. Nothing is copied, moved or deleted."),
        ("An editor for vertical video", "Crops to 9:16, 1:1 or 16:9 with speed, volume, captions and joining clips, plus a viewer with drag-to-scrub and trim handles."),
        ("Sharing built in", "Discord posting with automatically shrunk copies that play inline, YouTube uploads now or scheduled, and share links anyone can open."),
        ("Audio like OBS, made simple", "Several mics or virtual cables plus game audio, each with its own volume, and optional separate tracks in every clip."),
    ]), "cs-features")

    pipe = f'''
      <div class="pipe" data-reveal role="img" aria-label="Capture pipeline: screen, microphones, system audio and one app's audio all feed a single FFmpeg process, which writes two-second MPEG-TS segments into a ring buffer. Saving stitches segments with stream copy.">
        <div class="pipe__col">
          <div class="pipe__node"><b>Screen</b>ddagrab, stays on the GPU</div>
          <div class="pipe__node"><b>Mics and virtual cables</b>dshow</div>
          <div class="pipe__node"><b>System audio</b>WASAPI loopback</div>
          <div class="pipe__node"><b>One app, e.g. Discord</b>per-process loopback, own track</div>
        </div>
        {ARROW}
        <div class="pipe__node pipe__node--core"><b>One FFmpeg process</b>GPU encode: NVENC, AMF or Quick Sync</div>
        {ARROW}
        <div class="pipe__col">
          <div class="pipe__node"><b>Ring buffer</b>2-second MPEG-TS segments</div>
          <div class="pipe__node"><b>Save a clip</b>stitch segments by stream copy: instant, no re-encode</div>
        </div>
        <p class="pipe__note">Track 1 is always the mix; separate tracks follow it and are named in the MP4. The optional AI step reads small frames from finished segments in a separate process.</p>
      </div>'''

    eng = f'''
<section class="section" aria-labelledby="cs-eng">
  <div class="wrap">
    {shead("03", "Engineering", "The decisions that matter.", "A recorder has one job it must never fail at: stay out of the way of the game. Most of the interesting work follows from that.", hid="cs-eng")}
    {pipe}
    <div style="height:var(--s-7)"></div>
    {decisions([
        ("Capture on the GPU, save without re-encoding", [
            "Frames go from screen to encoder without leaving the GPU. Screen, microphones, system audio and a single app’s audio all go into <strong>one FFmpeg process</strong> that writes two-second MPEG-TS segments into a ring buffer.",
            "Saving a clip stitches the segments it needs by stream copy, so a save is instant and costs nothing extra while you play. On screens wider than 4096 px, Clutch picks HEVC or AV1 automatically."]),
        ("Background work never competes with the game", [
            "Exports, Discord copies, thumbnails, text reading and game detection all run <strong>below normal priority</strong>. Only the live recording stays at normal, so it never drops frames.",
            "The same rule covers updates: Clutch updates itself from GitHub releases, and it never restarts in the middle of a game."]),
        ("AI is optional, and asked only when something happens", [
            "For “watch the screen” you describe what to clip in plain English. Clutch watches locally for big changes on screen and loud moments, and <strong>only then</strong> asks the model whether the moment matches your rules. Calm stretches cost nothing.",
            "It runs on your own Anthropic API key or a Clutch account, and nothing is sent while the feature is off."]),
        ("Import nothing, read everything", [
            "People switching from Medal have years of clips. Instead of a migration, Clutch reads existing libraries <strong>in place</strong> and shows them in the same library, with nothing copied, moved or deleted.",
            "It can also import settings from Medal or OBS, so switching takes minutes."]),
        ("Private by default", [
            "Clips are recorded and stored on your PC. Clutch talks to the network only for features you turn on: Discord, YouTube, share links, AI, and update checks against the GitHub repository. There is <strong>no telemetry</strong>.",
            "The optional cloud server is small, has almost no dependencies, and can be self-hosted from Settings."]),
    ])}
  </div>
</section>'''

    gal = f'''
<section class="section" aria-labelledby="cs-gal">
  <div class="wrap">
    {shead("04", "Screens", "Inside the app.", "Click any screen to see it larger.", hid="cs-gal")}
    {gallery([
        shot("/assets/work/clutch/home", "Clutch home screen: recording status, triggers, setup checklist and clip of the day", "Home", "g-wide", widths=(960, 1440), w=1440, h=810),
        shot("/assets/work/clutch/editor", "The 9:16 editor cropping a clip for vertical video", "9:16 editor", "", widths=(960, 1440), w=1440, h=810),
        shot("/assets/work/clutch/player", "The clip player with details, tags and share actions", "Player", "", widths=(960, 1440), w=1440, h=810),
        shot("/assets/work/clutch/triggers", "What to clip: hype moments and conversation triggers with their thresholds", "Triggers, no AI", "g-half", widths=(960, 1440), w=1440, h=810),
        shot("/assets/work/clutch/rules", "Watch the screen: plain-English rules for the optional AI step", "Plain-English rules", "g-half", widths=(960, 1440), w=1440, h=810),
    ])}
  </div>
</section>'''

    links = f'''
<section class="section" aria-labelledby="cs-links">
  <div class="wrap">
    {shead("05", "Links", "Try it.", "Windows 10 or 11. The installer needs no admin rights, and updates install themselves after that.", hid="cs-links")}
    {links_block([("Download", "Clutch for Windows", CLUTCH_DL), ("Source", "GitHub repository", CLUTCH_REPO), ("History", "All releases", CLUTCH_REPO + "/releases")])}
  </div>
</section>'''

    body = hero + media + overview + nums + features + eng + gal + links + next_block(
        "juicicora", "Juicicora", "A cosy co-op adventure in Unreal Engine 5.6, and the deepest systems work I have going.", "/assets/work/juicicora/g-square-1600.webp")
    return page("/work/clutch", "Clutch case study — Kofi Shang",
                "How Kofi Shang built Clutch, a free open-source game clip recorder for Windows: GPU capture into a ring buffer, instant saves by stream copy, and clipping triggers that need no AI.",
                ("#26BBFF", "#7CD6FF", "rgba(38,187,255,.3)"), "/assets/work/clutch/home-1440.webp", body)

# ================================================================= JUICICORA

def juicicora():
    btns = (f'<a class="btn btn--primary" href="{JUICI_STEAM}" rel="noopener">Wishlist on Steam {icon("out")}</a>'
            f'<a class="btn btn--ghost" href="#cs-gal">See the island {icon("down")}</a>')
    hero = cs_hero("Juicicora", "Game · In development", "Juicicora",
                   "A cosy co-op adventure: play a Soul on the island of Elyndor.", btns,
                   [("Role", "Creator and lead developer"), ("Status", "Steam Early Access, December 2027"),
                    ("Players", "1 to 5, online co-op"), ("Engine", "Unreal Engine 5.6, C++")],
                   ["Unreal Engine 5.6", "C++", "Replicated multiplayer", "Steamworks", "Data-driven tuning"])
    media = f'''
    <figure class="cs-media" data-reveal="scale">
      <div class="frame frame--glow glow-host">{img("/assets/work/juicicora/home", "The village of Elyndor: a stone tower among autumn trees under a bright sky", 1600, 900, sizes="(max-width: 1320px) 100vw, 1200px", widths=(960, 1600), priority=True)}</div>
      <figcaption class="cs-media__cap"><span>Elyndor, in-engine.</span><span>Work in progress: everything here can still change.</span></figcaption>
    </figure>
  </div>
</section>'''

    overview = block("01", "Overview", "A bright little island, and you are a Soul on it.", '''
      <div class="cs-prose" data-reveal style="--i:1">
        <p class="big">You play a small, glossy, jelly-bodied Juicicoran with two simple eyes and a lot of opinions.</p>
        <p>You bounce, double jump, hover and ground pound your way around Elyndor: ruined arches, an orchard, flower meadows, a pond, waterfalls and a beach. Above it floats a piece of Aetheron, the sky village, reached by jump pads.</p>
        <p>Twenty souls live there, each with a home, a job and a day of their own. Trouble keeps turning up beyond the horizon, so you set sail to deal with it, alone or with up to four friends. Then you come home to your own house for the night.</p>
      </div>''', "cs-overview")

    nums = f'''
<section class="section" aria-label="Juicicora by the numbers">
  <div class="wrap">
    {numbers([("25", "Fruits, each one a power"), ("20", "Souls with their own homes, jobs and days"), ("12", "Missions on the Windward Spire, plus Challenge Mode"), ("5", "Players in online co-op")])}
  </div>
</section>'''

    press = f'''
<section class="section" aria-labelledby="cs-press">
  <div class="wrap">
    {shead("02", "Core system", "Every fruit is a power. The press makes it juice.", hid="cs-press")}
    <div class="case" style="pointer-events:none">
      <div class="case__media" data-reveal="scale">{img("/assets/work/juicicora/press", "A Soul next to the stone juice press", 1600, 900, sizes="(max-width: 860px) 100vw, 60vw", widths=(960, 1600))}</div>
      <div class="case__body cs-prose" data-reveal style="--i:1">
        <p>Shake fruit from the trees, pick berries off the bushes, drop them in a juice press, set a bottle on the stone and ground pound it. Drink the juice and its power runs on you: speed, spikes, webs to swing on, lightning steps, bombs, a burrow underground, or a split into several of you.</p>
        <p>Mix fruits in one bottle and their powers run together. <strong>Some pairs clash, and a clash costs you a heart.</strong></p>
        <p>Under the hood this is a power matrix whose fill curves are tuned from a CSV, so balancing twenty-five powers and their combinations is a data change, not a code change.</p>
      </div>
    </div>
  </div>
</section>'''

    seasons = block("03", "World clock", "A month on Elyndor is twenty-five days.", f'''
      <div class="seasons" data-reveal role="img" aria-label="Four seasons: Bloom, days 1 to 7; Blaze, days 8 to 13; Frost, days 14 to 19; Storm, days 20 to 25.">
        <div class="bloom"><span>Days 1–7</span><b>Bloom</b></div>
        <div class="blaze"><span>Days 8–13</span><b>Blaze</b></div>
        <div class="frost"><span>Days 14–19</span><b>Frost</b></div>
        <div class="storm"><span>Days 20–25</span><b>Storm</b></div>
      </div>
      <div class="cs-prose" data-reveal style="--i:1">
        <p>The world runs on a persistent clock with day and night. Each season changes the trees, the weather and which fruit grow; rain, fog, snow and thunderstorms roll in. On trade days the market sets up in the plaza, and on some nights a shooting star falls and leaves something rare where it lands.</p>
        <p>The souls live on the same clock. Each keeps their own hours, works their own counter, goes home to their own bed, and warms up to you as you run their errands and bring gifts they like.</p>
      </div>''', "cs-seasons")

    eng = f'''
<section class="section" aria-labelledby="cs-eng">
  <div class="wrap">
    {shead("04", "Engineering", "What it takes to build.", "Juicicora is a replicated multiplayer game in Unreal Engine 5.6 C++, which means every system has to work for up to five players at once.", hid="cs-eng")}
    {decisions([
        ("Co-op that holds together", [
            "Friends join through Steam invites and share one island: exploring together, giving gifts, duelling, and sailing out as one crew. Before the boat leaves, <strong>everyone votes</strong> on the mission.",
            "Missions earn a rank from F to J, and the rank decides the haul: gems, building materials, fruit, dyes, flowers, cosmetics and Glass Hearts."]),
        ("Enemies with rules, not just health bars", [
            "Plant Golems and Floaty Spirits hold the high rock tops; Sand Spirits slide under the dunes and Electric Golems crackle between the rocks. Each has a full set of moves: boulders built from flying pebbles, dashes that blink through you, beams from the sky, cyclones of sand.",
            "Elemental enemies follow <strong>counter rules</strong>, so water beats fire, and two boss birds, the Gale Mother and the Gale Father, guard the Windward Spire."]),
        ("A living village", [
            "Twenty souls each have a home, a job, a schedule and a story told in pieces. Players buy and upgrade houses with gathered sand, stone and wood, take a room at the inn, and keep gems at the bank.",
            "A night in your own bed brings every heart back, which ties the economy, the clock and survival together."]),
        ("Making collaboration cheap", [
            "Tuning lives in data where it can, like the power matrix’s CSV-driven curves. A one-click setup script writes a full log, so a collaborator’s broken setup can be diagnosed from a single file."]),
    ])}
  </div>
</section>'''

    gal = f'''
<section class="section" id="cs-gal" aria-labelledby="cs-gal-t">
  <div class="wrap">
    {shead("05", "Screens", "Around Elyndor and the Spire.", "Click any screen to see it larger.", hid="cs-gal-t")}
    {gallery([
        shot("/assets/work/juicicora/g-square", "Souls in the stone plaza with a ruined arch behind", "The plaza", "g-wide"),
        shot("/assets/work/juicicora/soul-close", "A Soul wearing wings and a chain beside a crate and a clay pot in the plaza", "Fits and cosmetics"),
        shot("/assets/work/juicicora/c-floaty", "Floaty Spirits glowing teal above a meadow", "Floaty Spirits"),
        shot("/assets/work/juicicora/v-spire", "The Windward Spire: rock tops over a sea of fog", "The Windward Spire", "g-half"),
        shot("/assets/work/juicicora/hero", "The portal warp between worlds, streaks of light against space", "Travelling by portal", "g-half"),
        shot("/assets/work/juicicora/g-drip", "Two Souls in a golden autumn meadow under red trees", "Blaze season", "g-wide g-right"),
        shot("/assets/work/juicicora/g-orchard", "A Soul by a red bush in the orchard", "The orchard"),
        shot("/assets/work/juicicora/seasons", "A Soul in a frosty meadow at the edge of the village", "Frost season"),
    ])}
  </div>
</section>'''

    links = f'''
<section class="section" aria-labelledby="cs-links">
  <div class="wrap">
    {shead("06", "Links", "Follow along.", "Wishlisting is the simplest way to hear first: Steam tells you the day Early Access goes live.", hid="cs-links")}
    {links_block([("Steam", "Wishlist Juicicora", JUICI_STEAM), ("Studio", "More ShangkoStudio games", STEAM_PUB), ("Questions", "Talk to me about it", "/start")])}
  </div>
</section>'''

    body = hero + media + overview + nums + press + seasons + eng + gal + links + next_block(
        "i-cant-see-you", "I Can't See You", "A multiplayer shooter in total darkness, and the server-side hearing system that makes it work.", "/assets/work/i-cant-see-you/ragdoll.webp")
    return page("/work/juicicora", "Juicicora case study — Kofi Shang",
                "Juicicora is a cosy co-op adventure for up to five players in Unreal Engine 5.6 by Kofi Shang: fruit powers from a juice press, twenty villagers with their own days, and missions at sea.",
                ("#5EC8F2", "#9BE0FF", "rgba(94,200,242,.3)"), "/assets/work/juicicora/home-1600.webp", body)

# ================================================================= I CAN'T SEE YOU

def icsy():
    btns = f'<a class="btn btn--primary" href="{ICSY_STEAM}" rel="noopener">View on Steam {icon("out")}</a>'
    hero = cs_hero("I Can't See You", "Game · Launched 10 October 2026", "I Can’t See You",
                   "A multiplayer shooter played in total darkness, where sound is the only thing that finds you.", btns,
                   [("Role", "Developer and publisher"), ("Status", "Early Access · $5.99"),
                    ("Players", "2 to 8 online, with proximity voice"), ("Engine", "Unreal Engine 5.5, C++")],
                   ["Unreal Engine 5.5", "C++", "Steam sessions", "Opus voice", "Unreal Python"])
    media = f'''
    <figure class="cs-media" data-reveal="scale">
      <div class="frame frame--glow glow-host" style="background:#000"><img src="/assets/work/i-cant-see-you/header.webp" alt="I Can't See You key art: a robot with a head torch lighting a pitch-black corridor while another lurks in the dark" width="1024" height="384" fetchpriority="high"></div>
      <figcaption class="cs-media__cap"><span>Key art. In the game itself, the darkness is the point.</span></figcaption>
    </figure>
  </div>
</section>'''

    overview = block("01", "Overview", "In the dark, every sound is a confession.", '''
      <div class="cs-prose" data-reveal style="--i:1">
        <p class="big">Every footstep, reload, shot and spoken word gives your position away.</p>
        <p>Two to eight players hunt each other with almost no light. You carry a pistol with a torch, flashbangs, a tape recorder that replays sounds and voices from wherever you throw it, a walkie talkie that keeps transmitting where it lands, and a dummy that drops a ragdoll copy of you to draw fire. The lobby sets the match, down to how many of each item everyone carries.</p>
        <p>Because sight is nearly useless, <strong>hearing is the game</strong>, and that put the hardest engineering in the networking layer rather than the renderer.</p>
      </div>''', "cs-overview")

    pipe = f'''
      <div class="pipe" data-reveal role="img" aria-label="Hearing pipeline: footsteps, shots, bangs, voices and recorder playback post noise events to a server-side noise bus. The server filters by hearing radius scaled by loudness and muffles through walls, then sends each client only what it can hear. The client lights the matching screen edge.">
        <div class="pipe__col">
          <div class="pipe__node"><b>Movement</b>walk 0.6 · crouch 0.25 · sprint 1.0</div>
          <div class="pipe__node"><b>Shots, bangs, impacts</b>from anyone</div>
          <div class="pipe__node"><b>Voice</b>a noise every 0.4 s while talking</div>
          <div class="pipe__node"><b>Recorders and radios</b>replayed sound counts too</div>
        </div>
        {ARROW}
        <div class="pipe__node pipe__node--core"><b>Noise bus, on the server</b>radius × loudness, muffled through walls</div>
        {ARROW}
        <div class="pipe__col">
          <div class="pipe__node"><b>Per-player replication</b>each client gets only what it hears</div>
          <div class="pipe__node"><b>HUD</b>screen edge by bearing, with a blip at the exact angle</div>
        </div>
        <p class="pipe__note">Distant sounds still show at a minimum strength so they read, and a noise within 1.5 m pulses all four edges with no bearing.</p>
      </div>'''

    eng = f'''
<section class="section" aria-labelledby="cs-eng">
  <div class="wrap">
    {shead("02", "Engineering", "Making sound the only sight.", "Built in Unreal Engine 5.5 C++ on the community Advanced Locomotion System, with Steam sessions, invites and voice.", hid="cs-eng")}
    {pipe}
    <div style="height:var(--s-7)"></div>
    {decisions([
        ("The server decides who hears what", [
            "Every footstep, shot, bang, impact and voice posts a noise event to a <strong>server-side noise bus</strong>. A component on each player’s controller drops anything outside their hearing radius, which scales with loudness, muffles sounds through walls, and sends that client only what it actually hears.",
            "On screen, the edge of the display lights in the direction of the sound, with a small blip at the exact bearing. Your own noises are hidden; your own speech isn’t, so you know when you’re giving yourself away."]),
        ("A tape recorder that records real voices", [
            "Throw a recorder and it keeps looping its tape from where it lands. The tape holds two things: every noise event within 22 m, replayed through the matching sounds, and <strong>the holder’s actual voice</strong>.",
            "While a take rolls, the holder’s machine captures the chosen microphone, resamples it to the voice-chat rate and Opus-encodes it <strong>one 20 ms frame per packet</strong>, because the engine’s codec wrapper corrupts multi-frame packets that contain a silent frame. Packets stream to the server, which relays them to every client; playback decodes into a procedural sound, up to 60 seconds."]),
        ("Speech is a noise too", [
            "Voice chat alone wasn’t enough: talking had to show up on enemies’ screens. The controller meters the chosen microphone itself and, when the level passes a threshold, posts a voice noise at the speaker’s body every 0.4 seconds.",
            "It also reads the voice engine’s talker record, because the built-in local-talking check is broken for the first local player. Replayed voices from recorders and radios post noises the same way."]),
        ("A project that rebuilds itself", [
            "The game’s input actions, character and item Blueprints, controllers, game modes and test map are <strong>generated by an idempotent Python script</strong> run headless through the editor. Re-running it after a pull restores anything missing.",
            "Weapons from a newer engine version couldn’t open in 5.5, so they were exported as FBX and re-imported by the same script with generated materials and a muzzle socket."]),
    ])}
  </div>
</section>'''

    art = f'''
<section class="section" aria-labelledby="cs-art">
  <div class="wrap">
    {shead("03", "Art", "The look.", "Stark black and white, so the torch and the red title are the only colour that matters.", hid="cs-art")}
    <div class="gallery">
      <figure class="g-half" data-reveal="scale"><div class="shot" style="cursor:default;background:#000;aspect-ratio:3/2"><img src="/assets/work/i-cant-see-you/ragdoll.webp" alt="A robot sprawled flat as a ragdoll" width="1200" height="800" loading="lazy" decoding="async" style="object-fit:contain"></div></figure>
      <figure data-reveal="scale" style="--i:1"><div class="shot" style="cursor:default;background:#000;aspect-ratio:3/2"><img src="/assets/work/i-cant-see-you/robot.webp" alt="A robot with a head torch running" width="442" height="442" loading="lazy" decoding="async" style="object-fit:contain"></div></figure>
      <figure class="g-full" data-reveal="scale"><div class="shot" style="cursor:default;background:#000;aspect-ratio:auto;padding:clamp(1.5rem,5vw,4rem)"><img src="/assets/work/i-cant-see-you/logo.webp" alt="The I Can't See You logo: white scratched letters with a red dripping 'See You'" width="900" height="450" loading="lazy" decoding="async" style="max-width:34rem;margin-inline:auto"></div></figure>
    </div>
  </div>
</section>'''

    links = f'''
<section class="section" aria-labelledby="cs-links">
  <div class="wrap">
    {shead("04", "Links", "Play it.", "In Early Access on Steam. Invite friends straight from Steam to join a lobby.", hid="cs-links")}
    {links_block([("Steam", "I Can’t See You", ICSY_STEAM), ("Studio", "More ShangkoStudio games", STEAM_PUB), ("Questions", "Talk to me about it", "/start")])}
  </div>
</section>'''

    body = hero + media + overview + eng + art + links + next_block(
        "forest-quest-88", "Forest Quest ’88", "A comedy text adventure that shipped as a 372-node story graph, with no AI at runtime.", "/assets/work/forest-quest-88/journey-1600.webp")
    return page("/work/i-cant-see-you", "I Can't See You case study — Kofi Shang",
                "I Can't See You is a multiplayer shooter in total darkness by Kofi Shang, built in Unreal Engine 5.5 C++ around a server-side noise bus, proximity voice and a tape recorder that records real voices.",
                ("#E5322D", "#FF7A75", "rgba(229,50,45,.28)"), "/assets/work/i-cant-see-you/header.webp", body)

# ================================================================= FOREST QUEST

def fq():
    btns = f'<a class="btn btn--primary" href="{FQ_STEAM}" rel="noopener">View on Steam {icon("out")}</a>'
    hero = cs_hero("Forest Quest '88", "Game · Launched 1 October 2026", "Forest Quest ’88",
                   "A deadpan comedy text adventure on a green CRT. You wake in a forest and just want to get home to bed.", btns,
                   [("Role", "Developer and publisher"), ("Price", "$1.99 on Steam"),
                    ("Built with", "Vite, vanilla JavaScript and Tauri"), ("Builds", "Windows, macOS and Linux")],
                   ["JavaScript", "Vite", "Canvas", "Web Audio", "Tauri", "Rust", "Steamworks", "GitHub Actions"])
    media = f'''
    <figure class="cs-media" data-reveal="scale">
      <div class="frame frame--glow glow-host" style="background:#000;position:relative">{img("/assets/work/forest-quest-88/opening", "Forest Quest '88: the opening scene in green CRT text with five numbered choices below a pixel-art viewport", 1600, 900, sizes="(max-width: 1320px) 100vw, 1200px", widths=(960, 1600), priority=True)}<span aria-hidden="true" style="position:absolute;inset:0;background:repeating-linear-gradient(to bottom,rgba(0,0,0,.22) 0 1px,transparent 1px 3px);pointer-events:none"></span></div>
      <figcaption class="cs-media__cap"><span>The opening. Five choices every turn, or type your own.</span></figcaption>
    </figure>
  </div>
</section>'''

    overview = block("01", "Overview", "The forest has one rule.", '''
      <div class="cs-prose" data-reveal style="--i:1">
        <p class="big">Do anything, and it rearranges itself around you.</p>
        <p>Home is in there somewhere. Every turn offers five actions, from weird and funny to normal, boring and outright negative; pick one with a click or a number key, or type your own. The journey is randomised, items drop into your inventory, a map and a journey log keep track, and there are three save slots with autosave.</p>
        <p>The comedy is dry on purpose. It works because the game is confident, consistent and completely unhelpful, which turned out to be an engineering constraint as much as a writing one.</p>
      </div>''', "cs-overview")

    nums = f'''
<section class="section" aria-label="Forest Quest '88 by the numbers">
  <div class="wrap">
    {numbers([("372", "Story nodes in the shipped graph"), ("95", "Endings, most of them bad"), ("11", "Cryptids to meet, or not survive"), ("10", "Steam achievements")])}
  </div>
</section>'''

    eng = f'''
<section class="section" aria-labelledby="cs-eng">
  <div class="wrap">
    {shead("02", "Engineering", "Funny is not a model’s job.", "The prototype and the shipped game are very different programs, and the difference is the most useful thing this project taught me.", hid="cs-eng")}
    {decisions([
        ("Models understand; authored content performs", [
            "The prototype used a small embedding model, MiniLM through Transformers.js, <strong>only to understand</strong> what the player typed, by matching it to the nearest option. An optional local narrator ran through Ollama.",
            "The rule I settled on: understanding the player is a model’s job, but being funny is not. A generative model tries to be coherent and helpful, which is exactly what kills the joke."]),
        ("Ship the story, not the model", [
            "For release, the story was baked into a fixed graph: <strong>372 nodes, 95 endings, 11 cryptids and 8 enemies</strong>, with no AI at runtime. Players install nothing extra, it runs fully offline, and every run reads the way it was meant to.",
            "The pixel viewport is pure JavaScript, so the whole game works the same everywhere."]),
        ("A web game that ships like a desktop game", [
            "The game is Vite and vanilla JavaScript inside a <strong>Tauri</strong> shell. Pushing a version tag makes GitHub Actions build installers for Windows, macOS and Linux, plus the three raw archives that go to Steam’s depots. No Rust toolchain is needed on the development machine."]),
        ("Achievements that survive being offline", [
            "Unlocks are saved locally first, then forwarded to Steamworks through a Tauri command backed by the <code>steamworks</code> Rust crate, compiled in only behind a cargo feature.",
            "On every launch the game re-sends every achievement it has earned. Steam ignores repeats, so <strong>nothing is lost</strong> if Steam wasn’t reachable the first time, and without Steam both commands are harmless no-ops."]),
    ])}
  </div>
</section>'''

    gal = f'''
<section class="section" aria-labelledby="cs-gal">
  <div class="wrap">
    {shead("03", "Screens", "On the CRT.", "Click any screen to see it larger.", hid="cs-gal")}
    {gallery([
        shot("/assets/work/forest-quest-88/journey", "A run in progress: the story so far and the next five choices", "A run in progress", "g-wide"),
        shot("/assets/work/forest-quest-88/cryptid", "A cryptid encounter: Mothman looms in red", "Cryptid encounter"),
        shot("/assets/work/forest-quest-88/ending", "An ending: the living room was home all along", "An ending"),
        shot("/assets/work/forest-quest-88/map", "The map of neighbourhoods between the forest and home", "The map", "g-half"),
        shot("/assets/work/forest-quest-88/inventory", "The inventory panel listing found items", "Inventory", "g-half"),
    ])}
  </div>
</section>'''

    links = f'''
<section class="section" aria-labelledby="cs-links">
  <div class="wrap">
    {shead("04", "Links", "Play it.", "$1.99 on Steam. It takes about as long as you can stand.", hid="cs-links")}
    {links_block([("Steam", "Forest Quest ’88", FQ_STEAM), ("Studio", "More ShangkoStudio games", STEAM_PUB), ("Questions", "Talk to me about it", "/start")])}
  </div>
</section>'''

    body = hero + media + overview + nums + eng + gal + links + next_block(
        "clutch", "Clutch", "Back to the start: an open-source clip recorder that stays out of the game’s way.", "/assets/work/clutch/home-1440.webp")
    return page("/work/forest-quest-88", "Forest Quest '88 case study — Kofi Shang",
                "Forest Quest '88 is a deadpan comedy text adventure by Kofi Shang: a 372-node story graph with 95 endings and no AI at runtime, built with Vite and shipped through Tauri to Steam.",
                ("#3DFF6E", "#8DFFA8", "rgba(61,255,110,.22)"), "/assets/work/forest-quest-88/opening-1600.webp", body)
