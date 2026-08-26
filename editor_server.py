# -*- coding: utf-8 -*-
"""
Local editor server for the Historie kronika.

Serves the static site (like `python -m http.server`) and additionally
handles two endpoints used by editor.html:

  POST /api/save-aktuality   body: JSON array  -> writes data/aktuality.json
  POST /api/upload-image     body: multipart/form-data, field "file"
                              -> saves into images/historie/aktuality/
                                 returns {"path": "images/historie/aktuality/<name>"}

Run from the project root:
    python editor_server.py [port]
Default port is 8347 (same as the plain dev server) unless already in use,
in which case pick a free one with: python editor_server.py 8400
"""
import http.server
import json
import os
import re
import socketserver
import sys
import unicodedata
import uuid

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT, "data", "aktuality.json")
CONTENT_PATH = os.path.join(ROOT, "data", "site-content.json")
UPLOAD_DIR = os.path.join(ROOT, "images", "historie", "aktuality")


def safe_filename(name):
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-")
    if not name:
        name = "photo"
    base, ext = os.path.splitext(name)
    if ext.lower() not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
        ext = ".jpg"
    return base[:60], ext.lower()


def parse_multipart(body, boundary):
    boundary_bytes = ("--" + boundary).encode("utf-8")
    parts = body.split(boundary_bytes)
    for part in parts:
        part = part.strip(b"\r\n")
        if not part or part == b"--":
            continue
        if b"\r\n\r\n" not in part:
            continue
        headers_raw, content = part.split(b"\r\n\r\n", 1)
        content = content.rstrip(b"\r\n")
        headers_raw = headers_raw.decode("utf-8", errors="replace")
        if 'name="file"' not in headers_raw:
            continue
        m = re.search(r'filename="([^"]*)"', headers_raw)
        filename = m.group(1) if m else "upload.jpg"
        return filename, content
    return None, None


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def address_string(self):
        # avoid the default reverse-DNS lookup, which can block for tens of
        # seconds per request when there's no reachable DNS server
        return self.client_address[0]

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send_json(self, status, obj):
        payload = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/save-aktuality":
            return self._handle_save(DATA_PATH)
        if self.path == "/api/save-content":
            return self._handle_save(CONTENT_PATH)
        if self.path == "/api/upload-image":
            return self._handle_upload()
        self._send_json(404, {"error": "not found"})

    def _handle_save(self, path):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            entries = json.loads(raw.decode("utf-8"))
            if not isinstance(entries, list):
                raise ValueError("expected a JSON array")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(entries, f, ensure_ascii=False, indent=2)
            self._send_json(200, {"ok": True, "count": len(entries)})
        except Exception as e:
            self._send_json(400, {"error": str(e)})

    def _handle_upload(self):
        try:
            content_type = self.headers.get("Content-Type", "")
            m = re.search(r"boundary=(.+)", content_type)
            if not m:
                raise ValueError("missing multipart boundary")
            boundary = m.group(1).strip('"')
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            filename, content = parse_multipart(body, boundary)
            if content is None:
                raise ValueError("no file field found")
            base, ext = safe_filename(filename)
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            out_name = f"{base}-{uuid.uuid4().hex[:6]}{ext}"
            out_path = os.path.join(UPLOAD_DIR, out_name)
            with open(out_path, "wb") as f:
                f.write(content)
            rel_path = "images/historie/aktuality/" + out_name
            self._send_json(200, {"ok": True, "path": rel_path})
        except Exception as e:
            self._send_json(400, {"error": str(e)})


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8347
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Editor server running at http://localhost:{port}/editor.html")
        print(f"(saving to {DATA_PATH})")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
