# kofifshang.dev

Personal site for Kofi Shang / Shangko Co, live at **https://kofifshang.dev**.

Hosted on **Cloudflare Workers**. Every push to `main` redeploys automatically.

```
public/                  everything visitors can load
  index.html             homepage, hand-written        /
  styles.css             the whole design system
  start.html             Start a project form          /start
  support.js             runtime that renders start.html only
  assets/games/*.jpg     Steam capsule art, one per title
  assets/                favicon, portrait, Clutch icon
  logo-white.png         Shangko mark
src/worker.js            handles POST /api/contact and emails the brief
wrangler.jsonc           Worker name, asset folder, email binding
```

Only `public/` is served. The Worker source, config and this README are not reachable on the site.

## The homepage

`index.html` and `styles.css` are hand-written, with no build step and no dependencies. The only JavaScript is about 20 lines inline at the bottom: the mobile menu and a scroll reveal, both of which degrade safely if JS is off or the viewer prefers reduced motion.

Design tokens live at the top of `styles.css`. The palette is taken from the Shangko mark: near-black ground, bone text, one electric blue. `--accent` is for fills and borders; `--accent-lit` is the lighter blue used for accent **text**, because the fill blue does not meet contrast requirements on the dark ground.

Breakpoints: 1040px (grids narrow), 860px (nav collapses to a menu button, cards stack), 560px (single column).

To add a game, copy one `.game` block and drop its capsule art in `public/assets/games/`. Capsule art comes from Steam's app details API:
`https://store.steampowered.com/api/appdetails?appids=APPID` returns a `header_image` URL.

## The Start a project form

`start.html` is still a Claude Design export rendered by `support.js`. It posts the brief as JSON to `/api/contact`, where the Worker:

1. Rejects cross-site posts, oversized bodies, missing fields and malformed email addresses.
2. Quietly drops likely bots: anything that fills the hidden `website` field, or submits within 2.5 seconds of the page opening.
3. Emails the brief through **Cloudflare Email Routing**, from `form@kofifshang.dev` to `kofifshang@gmail.com`, with Reply-To set to the visitor.

The email binding can only ever deliver to that one verified address, so the form cannot be used to email anyone else.

**Careful with `start.html`.** A fresh export from Claude Design brings back the old open-your-email-app behaviour. Keep the logic that is in the file, or re-apply it after exporting.

## Cloudflare setup (already done)

Email Routing is enabled on the zone and `kofifshang@gmail.com` is a verified destination address. Without both, submissions fail and the form shows the email address as a fallback.

## Still to do

- Add the remaining social links. The site currently links GitHub, Steam and LinkedIn only; YouTube and the short-form accounts are not recorded anywhere in this repo.
- Consider rewriting `start.html` by hand to match the new homepage and drop `support.js`.

Never commit the Claude Design project's `uploads/` folder. It holds working files, including a resume with a phone number.
