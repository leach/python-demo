
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(10)
conn,addr = server.accept()
with conn:
    res = conn.recv(1024)
    print(res.decode("utf-8"))
    conn.send(res)

conn.close()