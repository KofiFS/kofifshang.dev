# kofifshang.dev

Personal site for Kofi Shang / Shangko Co, live at **https://kofifshang.dev**.

Hosted on **Cloudflare Workers**. Every push to `main` redeploys automatically.

```
public/            everything visitors can load
  index.html       homepage                 /
  start.html       Start a project          /start
  support.js       Claude Design runtime that renders both pages
  assets/          favicon and link-preview image
src/worker.js      handles POST /api/contact and emails the brief
wrangler.jsonc     Worker name, asset folder, email binding
```

Only `public/` is served. The Worker code, config and this README are not reachable on the site.

## How the Start a project form works

1. The page posts the brief as JSON to `/api/contact`.
2. The Worker rejects cross-site posts, oversized bodies, missing fields and malformed email addresses.
3. It quietly drops likely bots: anything that fills the hidden `website` field, or submits within 2.5 seconds of the page opening.
4. It emails the brief through **Cloudflare Email Routing**, from `form@kofifshang.dev` to `kofifshang@gmail.com`. Reply-To is the visitor's address, so hitting reply answers them.

The email binding can only ever deliver to that one verified address, so the form can't be abused to email anyone else.

## One-time setup (Cloudflare dashboard)

1. **Email > Email Routing** on kofifshang.dev: enable it and accept the DNS records it adds.
2. **Destination addresses**: add `kofifshang@gmail.com`, then click the verification link Cloudflare emails you.

Until both are done, submissions fail and the form shows the email address as a fallback.

## Updating the site

1. Export `Site.dc.html` from Claude Design and save it as `public/index.html`.
2. Point its `StartAProject.dc.html` links at `/start`.
3. Re-add the `<title>` and link-preview tags in `<head>`. Exports don't carry them.
4. Commit and push to `main`.

**Careful with `start.html`.** A fresh export of `StartAProject.dc.html` brings back the old open-your-email-app logic. Keep the logic in `public/start.html`, or re-apply it after exporting.

Never commit the Claude Design project's `uploads/` folder. It holds working files, including a resume with a phone number.
