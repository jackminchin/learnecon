import http.server
import socketserver

PORT = 8001
DIRECTORY = "_build/dirhtml"

class Server(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def listen():
    with socketserver.TCPServer(("", PORT), Server) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
    

listen()