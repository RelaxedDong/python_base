#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/15 20:41
import socket,re
def service_client(new_socket):
    request = new_socket.recv(1024)
    path = re.findall('GET (.*?) HTTP', request.decode('utf-8'))
    response = "HTTP/1.1 200 OK\r\n"
    response+= "\r\n"
    try:
        with open("templates%s" % path[0], 'r') as f:
            response += f.read()
            print(response)
    except Exception as e:
        response+="<h1>资源没找到</h1>"
    new_socket.send(response.encode('utf-8'))
    new_socket.close()

def main():
    """用来完成整体控制"""
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(('',7890))
    tcp_server_socket.listen(128)

    while True:
        newsocket,client_addr = tcp_server_socket.accept()
        service_client(newsocket)

    tcp_server_socket.close()

if __name__ == '__main__':
    main()