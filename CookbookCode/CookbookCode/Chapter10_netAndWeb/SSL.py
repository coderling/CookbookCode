#####################################################
## file name:SSL
## create time:2016/7/26 23:49:44
## email:coderling@gmail.com
#####################################################
from socket import socket, AF_INET, SOCK_STREAM
import ssl

KEYFILE = 'server_key.pem'
CERFILE = 'server_cert.pem'

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('connection, closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE,
                            CERFILE=CERFILE,
                            server_side=True)

    while True:
        try:
            c, a = s_ssl.accept()
            print('Got connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{}:{}'.format(echo_client.__class__.__name__, e))

echo_server(('', 20000))


