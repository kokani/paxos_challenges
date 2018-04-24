#Code below is deployed on 45.33.71.183


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import hashlib
import json

class Server(BaseHTTPRequestHandler):

    SERVER_CACHE = {}

    def _setHeaders(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        try:
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = json.loads(self.rfile.read(content_len))
        except:
            result = {'err_msg': 'Form data must be valid json'}
            self.wfile.write(json.dumps(result))
            return

        if 'message' not in post_body:
            result = {'err_msg': '"message" must be present in form data"'}
        else:
            message = post_body['message']
            digest = hashlib.sha256(message).hexdigest()
            result = {'digest': digest}
            self.SERVER_CACHE[digest] = message

        self._setHeaders(200)
        self.wfile.write(json.dumps(result))

    def do_GET(self):
        path = self.path[1:]
        splitPath = path.split('/')
        if len(splitPath) != 2 or splitPath[0] != 'messages':
            statusCode = 404
            result = {'err_msg': 'Invalid URL'}
        elif splitPath[1] not in self.SERVER_CACHE:
            statusCode = 404
            result = {'err_msg': 'Message not found'}
        else:
             statusCode = 200
             result = {'message': self.SERVER_CACHE[splitPath[1]]}

        self._setHeaders(statusCode)
        self.wfile.write(json.dumps(result))

def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
