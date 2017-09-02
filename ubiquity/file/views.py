from django.shortcuts import render
import socket,os 
from threading import Thread
# Create your views here.
class ClientThread(Thread):
    def __init__(self,conn,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        print("[+] New server socket thread started for " + ip + ":" + str(port) )
 
    def run(self): 
        while True : 
            with open(os.getcwd()+'/image', 'wb') as f:
                data = self.conn.recv(1024)
                while(data):
                    f.write(data)
                    data=self.conn.recv(1024)
                MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
                if MESSAGE == 'exit':
                    break
                self.conn.send(bytes(MESSAGE,'utf-8'))  # echo 

def preview(request, ext):
	"""Generates a preview for the file to be streamed by the user; a helper to the showfiles() view function."""
	file = os.getcwd()+'/ubiquity/static/uploads/'+str(request.user.get_username())+'file.'+ext
	if(ext=='pdf'):
		return 'The pdf file text should be displayed here'
	else:
		return 'We are unable to process these files at the moment. You may download it instead.'

def showfiles(request):
	uname = request.user.get_username()
	cwd = os.getcwd()

	fileList = []

	indexFile = cwd+'/ubiquity/static/uploads/'+str(uname)+'/index.txt'

	if request.GET.get('q'):
		query = request.GET['q']
		ext = request.GET['e']
		prev = preview(request, ext)		
		return render(request, 'file/preview.html',{'preview':prev})
	else:
		with open(indexFile) as f:
			c=f.readline()
			while(c):
				fileList.append(c)
				c = f.readline()
	
		return render(request, 'file/contents.html',{'uname':uname, 'fileList':fileList})


def run_socket(request):	 
	# Multithreaded Python server : TCP Server Socket Program Stub
	TCP_IP = '192.168.0.144' 
	TCP_PORT = 5200 
	BUFFER_SIZE = 20  # Usually 1024, but we need quick response 
	 
	tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	tcpServer.bind((TCP_IP, TCP_PORT)) 
	threads = [] 
	 
	while True: 
	    tcpServer.listen(4)
	    print("Multithreaded Python server : Waiting for connections from TCP clients..." )
	    (conn, (ip,port)) = tcpServer.accept() 
	    print("New connection: ",conn)
	    
	    newthread = ClientThread(conn,ip,port) 
	    newthread.start() 
	    threads.append(newthread) 
	 
	for t in threads: 
	    t.join()
