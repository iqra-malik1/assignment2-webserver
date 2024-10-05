from socket import *
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  
  while True:
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024).decode()
      fileName = message.split()[1]
      
      file = open(fileName[1:], 'rb')

      validResponse = b"HTTP/1.1 200 OK\r\n"
      outputMessage = b"Content-Type: text/html; charset=UTF-8\r\n"
      outputMessage += b"Server: MyServer\r\n"
      outputMessage += b"Connection: Done! \r\n\r\n"
               
      for line in file:
        outputMessage += file.read()
      
      connectionSocket.sendall(validResponse + outputMessage + file.read())

      connectionSocket.close() 
      
    except Exception as e:
      errorResponse = b"HTTP/1.1 404 Not Found\r\n"
      errorResponse += b"Content-Type: text/html; charset=UTF-8\r\n"
      errorResponse += b"Server: MyServer\r\n"
      errorResponse += b"Connection: Done! \r\n\r\n"
      errorResponseHTML = b"<html><body><h1>404 Not Found</h1></body></html>\r\n"
      
      connectionSocket.sendall(errorResponse + errorResponseHTML)

      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)
