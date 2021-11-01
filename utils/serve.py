import http.server
import socketserver

PORT = 8001
DIRECTORY = "_build/dirhtml"

class Server(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def listen():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Server) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    listen()
