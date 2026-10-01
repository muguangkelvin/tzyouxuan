import os
import http.server
import socketserver

PORT = 1313
DIRECTORY = "public"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Normalize request path
        path = self.path.split('?')[0].split('#')[0]
        full_path = os.path.join(DIRECTORY, path.lstrip('/'))
        
        # If path is a directory and index.html exists, serve index.html
        if os.path.isdir(full_path):
            index_path = os.path.join(full_path, "index.html")
            if os.path.exists(index_path):
                if not self.path.endswith('/') and not self.path.endswith('.html'):
                    self.send_response(301)
                    self.send_header('Location', self.path + '/')
                    self.end_headers()
                    return
        elif not os.path.exists(full_path) and not path.endswith('.html'):
            # Try appending .html or /index.html
            if os.path.exists(full_path + '.html'):
                self.path = path + '.html'
            elif os.path.exists(os.path.join(full_path, 'index.html')):
                self.path = path + '/index.html'

        return super().do_GET()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {PORT} (http://localhost:{PORT}/)...")
        httpd.serve_forever()
