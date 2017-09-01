import socket 
from threading import Thread 
from socketserver import ThreadingMixIn 
 
# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print("[+] New server socket thread started for " + ip + ":" + str(port) )
 
    def run(self): 
        filename = STATIC_URL + "/uploads/" + str(self.ip) + "/index.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w") as f: 
            data = conn.recv(1024) 
            # data = client.recv(1024)
            while(data):
                f.write(data)
                data = conn.recv(1024)

            # # print("Server received data:", data)
            # # MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            # # if MESSAGE == 'exit':
            #    break
            # # conn.send(MESSAGE)  # echo 
 
# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '192.168.29.121' 
TCP_PORT = 7000 
BUFFER_SIZE = 1024
 
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 

while True: 
    tcpServer.listen(4)
    print("Multithreaded Python server : Waiting for connections from TCP clients..." )
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 
