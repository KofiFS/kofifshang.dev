# kofifshang.dev

Personal site for Kofi Shang / Shangko Co. Served by GitHub Pages at **https://kofifshang.dev**.

```
index.html     the whole site (a self-contained Claude Design export)
CNAME          tells GitHub Pages which custom domain to serve
.nojekyll      skip Jekyll processing; serve files as-is
assets/        favicon and link-preview image
```

## How the page works

`index.html` is a single bundled page exported from Claude Design. It carries its own images, fonts reference, and React runtime inline, then unpacks itself with JavaScript on load. Nothing is fetched from a CDN at runtime except Google Fonts.

The outer `<head>` holds the title, description, and Open Graph tags. Link-preview crawlers (LinkedIn, Slack, iMessage) do not run JavaScript, so those tags must live there rather than inside the bundle.

## Updating the site

1. Export the new version from Claude Design.
2. Replace `index.html` with it.
3. Re-add the outer `<head>` tags. A fresh export resets them to a generic "Bundled Page" title.
4. Commit and push to `main`. Pages redeploys in about a minute.

Never delete `CNAME`. Removing it detaches the custom domain.

## DNS (Cloudflare)

The domain's nameservers are on Cloudflare. Add these records in **Cloudflare → kofifshang.dev → DNS → Records**, each with the proxy set to **DNS only** (grey cloud):

| Type  | Name  | Content                |
|-------|-------|------------------------|
| A     | `@`   | `185.199.108.153`      |
| A     | `@`   | `185.199.109.153`      |
| A     | `@`   | `185.199.110.153`      |
| A     | `@`   | `185.199.111.153`      |
| AAAA  | `@`   | `2606:50c0:8000::153`  |
| AAAA  | `@`   | `2606:50c0:8001::153`  |
| AAAA  | `@`   | `2606:50c0:8002::153`  |
| AAAA  | `@`   | `2606:50c0:8003::153`  |
| CNAME | `www` | `kofifs.github.io`     |

**Why DNS only:** GitHub issues the HTTPS certificate itself. With Cloudflare's orange-cloud proxy on, GitHub can't complete that check and the certificate never arrives.

**Why HTTPS matters here:** every `.dev` domain is on the browser HSTS preload list, so browsers refuse plain HTTP outright. The site will not load at all until the certificate exists. After DNS propagates, open the repo's **Settings → Pages** and tick **Enforce HTTPS** once it becomes available.

## Protect the domain

In **GitHub → Settings (account) → Pages → Add a domain**, verify `kofifshang.dev`. GitHub gives you one TXT record to add in Cloudflare. That stops anyone else's repository from claiming your domain.
