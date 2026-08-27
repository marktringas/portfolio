#!/usr/bin/env python3
"""Local test server for the love.js build.
Run: python3 serve.py
Then visit: http://localhost:8000
"""
import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        # prevent the browser from caching game.data/love.wasm across rebuilds —
        # love.js caches by filename, not content, so a stale cache silently
        # serves an old build otherwise
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
