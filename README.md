# kofifshang.dev

Personal site for Kofi Shang / Shangko Co, live at **https://kofifshang.dev**.

Hosted on **Cloudflare Workers**. Every push to `main` redeploys automatically.

```
public/                      everything visitors can load (and nothing else is)
  index.html                 /                 homepage
  work.html                  /work             case-study index + tools
  work/clutch.html           /work/clutch      case studies, one per major project
  work/juicicora.html        /work/juicicora
  work/i-cant-see-you.html   /work/i-cant-see-you
  work/forest-quest-88.html  /work/forest-quest-88
  games.html                 /games            full Steam catalogue with filters
  about.html                 /about
  start.html                 /start            contact form (posts to /api/contact)
  404.html                   served for unknown paths (not_found_handling in wrangler.jsonc)
  styles.css                 the whole design system
  site.js                    the only script: nav, reveals, filters, lightbox, form
  assets/work/<project>/     case-study screenshots (WebP, 960 + 1440/1600 wide) and the Clutch tour loop
  assets/games/*.jpg         Steam capsule art, one per title
  assets/og.jpg              social preview image
src/worker.js                handles POST /api/contact and emails the brief
tools/site/                  page templates (Python) that generate the HTML above
wrangler.jsonc               Worker name, asset folder, email binding, 404 page
```

## Editing pages

The HTML in `public/` is **generated** from the templates in `tools/site/` so the header, footer and
case-study layout stay identical on every page. Edit the templates, then rebuild:

```bash
python tools/site/build.py        # rewrites public/*.html, sitemap.xml and robots.txt
python tools/site/serve.py 8787   # preview at http://127.0.0.1:8787
```

`serve.py` mimics Cloudflare's routing (`/work` serves `work.html`, unknown paths get `404.html`). It does
not run the Worker, so the contact form shows its error message locally; that is expected.

Where things live:

| Change | File |
|---|---|
| Nav, footer, `<head>`, contact band | `tools/site/parts.py` |
| Homepage and the game list (used by `/games` too) | `tools/site/home.py` |
| Work, Games, About, Start, 404 | `tools/site/pages.py` |
| The four case studies | `tools/site/cases.py` |

Cloudflare serves the committed files as they are. There is no build step on deploy and no npm dependency.

## Design system

Tokens are at the top of `styles.css`: colour, a fluid type scale, a 4px spacing scale, radii, easing and
z-index layers. The identity comes from the Shangko mark: a near-black ground, bone text and one electric
blue. `--accent` is for fills and rules, and `--accent-lit` is for accent **text**, because the fill blue
fails contrast on the dark ground. Each case study sets its own `--tint` (Clutch blue, Juicicora sky,
I Can't See You red, Forest Quest phosphor green), used sparingly for labels, glows and selection.

Type: Zen Old Mincho for display, Archivo for text, JetBrains Mono for labels and metadata.

Breakpoints: 1100px (two-column layouts stack), 860px (menu button, single-column sections), 600px (phone).

Motion: scroll reveals, a hero entrance, a pointer-follow tilt on the hero composition, gentle parallax on
the Juicicora panel, a cursor-follow cover preview on the catalogue, and cross-page view transitions where
the browser supports them. Everything is off under `prefers-reduced-motion`, and every page is fully readable
with JavaScript disabled (reveals only hide content once `site.js` has added the `js` class).

The Clutch version shown on the site is written into the HTML and then refreshed from the GitHub releases
API in the visitor's browser, so it stays current without a rebuild.

## Adding things

- **A game:** add a row to `GAMES` in `tools/site/home.py` and drop its capsule art in `public/assets/games/`.
  Capsule art comes from `https://store.steampowered.com/api/appdetails?appids=APPID` (`header_image`).
  Its `tags` drive the filters on `/games` (`multiplayer`, `comedy`, `action`, `upcoming`).
- **Screenshots:** save WebP at 960 and 1600 (or 1440) wide as `name-960.webp` / `name-1600.webp` in
  `public/assets/work/<project>/`, then reference `name` with `img()` or `shot()` in the templates.

## The Start a project form

`start.html` is a plain HTML form; `site.js` validates it and posts the brief as JSON to `/api/contact`,
where the Worker:

1. Rejects cross-site posts, oversized bodies, missing fields and malformed email addresses.
2. Quietly drops likely bots: anything that fills the hidden `website` field, or submits within 2.5 seconds of the page opening.
3. Emails the brief through **Cloudflare Email Routing**, from `form@kofifshang.dev` to `kofifshang@gmail.com`, with Reply-To set to the visitor.

The email binding can only ever deliver to that one verified address, so the form cannot be used to email anyone else.
Without JavaScript the form shows the email address instead.

## Cloudflare setup (already done)

Email Routing is enabled on the zone and `kofifshang@gmail.com` is a verified destination address. Without both, submissions fail and the form shows the email address as a fallback.

## Still to do

- **Missing assets.** I Can't See You has key art but no gameplay screenshots on the site, the portrait is
  only 400×400 (it is shown at up to ~420px), and there is no public résumé to link. Add them and the
  templates will pick them up.
- Add the remaining social links. The site links GitHub, Steam and LinkedIn only; YouTube and the short-form accounts are not recorded anywhere in this repo.

Never commit the Claude Design project's `uploads/` folder. It holds working files, including a resume with a phone number.
