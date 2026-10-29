import http.server, socketserver, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
PAGE = "mii-mixer-v6-local.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".wasm": "application/wasm",
        ".js": "text/javascript",
        ".cjs": "text/javascript",
        ".mjs": "text/javascript",
    }

    def end_headers(self):
        # Needed for SharedArrayBuffer, which the FFL WebAssembly renderer uses.
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as server:
    print(f"Open http://localhost:{PORT}/{PAGE}   (Ctrl+C to stop)", flush=True)
    server.serve_forever()
