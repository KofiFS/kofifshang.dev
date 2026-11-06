"""Regenerates every page in public/ from the Python templates in this folder.

    python tools/site/build.py         # write the pages
    python tools/site/serve.py 8787    # preview at http://127.0.0.1:8787 (mimics Cloudflare's routing)

The output is plain static HTML that is committed and served as-is; Cloudflare runs no build step.
Edit the templates here rather than the generated HTML, or your edits will be overwritten next build.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import home, pages, cases
from parts import SITE

OUT = os.path.normpath(os.path.join(HERE, "..", "..", "public"))
files = {
    "index.html": home.page(),
    "work.html": pages.work(),
    "games.html": pages.games(),
    "about.html": pages.about(),
    "start.html": pages.start(),
    "404.html": pages.notfound(),
    "work/clutch.html": cases.clutch(),
    "work/juicicora.html": cases.juicicora(),
    "work/i-cant-see-you.html": cases.icsy(),
    "work/forest-quest-88.html": cases.fq(),
}
routes = ["/", "/work", "/work/clutch", "/work/juicicora", "/work/i-cant-see-you", "/work/forest-quest-88", "/games", "/about", "/start"]
files["sitemap.xml"] = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                        + "".join(f"  <url><loc>{SITE}{r}</loc></url>\n" for r in routes) + "</urlset>\n")
files["robots.txt"] = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n"

for name, text in files.items():
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"{name:32} {len(text):>7,} bytes")
