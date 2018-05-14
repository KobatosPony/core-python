# 使用 httpserver 创建简单的服务器
from http.server import BaseHTTPRequestHandler,HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:],'rb')
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,'File Not Found:%s' % self.path)

def main():
    server = HTTPServer(('', 80), MyHandler)
    try:
        print('connect...')
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()