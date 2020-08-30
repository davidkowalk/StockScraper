class Server(BaseHTTPRequestHandler):

    def __send_headers__(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        if self.path == "/index":
            pass

    def do_POST(self):
        pass
