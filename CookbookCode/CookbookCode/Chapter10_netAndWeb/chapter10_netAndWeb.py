#####################################################
## file name:chapter10_netAndWeb
## create time:2016/7/25 7:50:03
## email:coderling@gmail.com
#####################################################

#sample TCP server
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


def StartSampleTCPServer():
    srv = TCPServer(('', 20000), EchoHandler)
    print("Sampler Server Start...");
    srv.serve_forever()
    

if __name__ == '__main__':
    StartSampleTCPServer()

