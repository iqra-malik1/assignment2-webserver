# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  
  while True:
    connectionSocket, addr = serverSocket.accept() #are you accepting connections?
    
    try:
       #a client is sending you a message 
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    

      responseHeader = "HTTP/1.1 200 OK"
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Server: SimplePythonServer\r\n"
      outputdata += b"Connection: Close \r\n\r\n"
               
      for i in f: #for line in file
        outputdata += f.read()
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      
      fullBodyResponse = responseHeader + outputdata + f.read()
      connectionSocket.sendall(fullBodyResponse)

      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block

      errorResponseHeader = b"HTTP/1.1 404 Not Found\r\n"
      errorResponseHeader += b"Content-Type: text/html; charset=UTF-8\r\n"
      errorResponseHeader += b"Server: SimplePythonServer\r\n"
      errorResponseHeader += b"Connection: Close \r\n\r\n"
      errorResponseBody = b"<html><body><h1>404 Not Found</h1></body></html>\r\n"

      sendFullErrorResponse = errorResponseHeader + errorResponseBody
      
      connectionSocket.sendall(sendFullErrorResponse)

      #Close client socket
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)
