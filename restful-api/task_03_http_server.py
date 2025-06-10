#!/usr/bin/python3
import http.server
import json
""""""


class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Home endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # / JSON data endpoint
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "name": "John", 
                "age": 30, 
                "city": "New York"}
            ).encode())

        # / Status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # / Info endpoint
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            }).encode())

        # 404 endpoint
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleRequestHandler):
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on http://localhost:{port}")
    httpd.serve_forever()

run()
