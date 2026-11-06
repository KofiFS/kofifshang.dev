# Local stand-in for Cloudflare's asset handler: /x serves x.html, unknown paths serve 404.html with status 404.
import http.server, os, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "public"))

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def send_head(self):
        path = self.path.split("?")[0].split("#")[0]
        fs = os.path.join(ROOT, path.lstrip("/").replace("/", os.sep))
        if path != "/" and not os.path.isfile(fs) and os.path.exists(fs.rstrip(os.sep) + ".html"):
            path = path.rstrip("/")
            self.path = path + ".html"
        elif path != "/" and not os.path.exists(fs):
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            body = open(os.path.join(ROOT, "404.html"), "rb").read()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            import io
            return io.BytesIO(body)
        return super().send_head()
    def log_message(self, *a):
        pass

http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 8787), H).serve_forever()
