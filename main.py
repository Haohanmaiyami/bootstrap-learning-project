from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open("templates/contacts.html", "r", encoding="utf-8") as file:
                content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found: contacts.html missing.")

if __name__ == "__main__":
    print(f"Сервер запущен на http://{host}:{port}")
    server = HTTPServer((host, port), SimpleHandler)
    server.serve_forever()
