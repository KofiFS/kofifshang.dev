# kofifshang.dev

Personal site for Kofi Shang / Shangko Co, live at **https://kofifshang.dev**.

Hosted on **Cloudflare Workers** (static assets). Every push to `main` redeploys automatically.

```
index.html     homepage            -> https://kofifshang.dev/
start.html     Start a project     -> https://kofifshang.dev/start
support.js     Claude Design runtime that renders both pages
*.png, *.jpg   images the pages load
assets/        favicon and link-preview image
```

## How the pages work

Both pages are Claude Design components (`.dc.html` format) served as-is. Each loads `support.js`, which renders the page in the browser. The same runtime powers the Juicicora site.

Cloudflare serves `start.html` at the clean URL `/start`, so links between pages use `/` and `/start`.

The Start a project form sends nothing over the network. Submitting opens a pre-filled email to kofifshang@gmail.com, or copies the brief to the clipboard.

## Updating the site

1. In Claude Design, export `Site.dc.html` and `StartAProject.dc.html`.
2. Save them as `index.html` and `start.html`.
3. Point links at the live URLs: `StartAProject.dc.html` becomes `/start`, and `Site.dc.html` becomes `/`.
4. Re-add the `<title>` and link-preview tags in `<head>`. Exports don't carry them.
5. Commit and push to `main`.

Never commit the project's `uploads/` folder. It holds working files, including a resume with a phone number.
