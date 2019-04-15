#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/15 20:41
import socket

def service_client(new_socket):
    request = new_socket.recv(1024)
    print(request)
    response = "HTTP/1.1 200 OK\r\n"
    response+= "\r\n"
    response+= "<h1>hello</h1>"
    new_socket.send(response.encode('utf-8'))
    new_socket.close()

def main():
    """用来完成整体控制"""
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(('',7890))

    tcp_server_socket.listen(128)

    while True:
        newsocket,client_addr = tcp_server_socket.accept()
        service_client(newsocket)

    tcp_server_socket.close()

if __name__ == '__main__':
    main()