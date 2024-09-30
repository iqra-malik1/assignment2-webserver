# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen()
  
  while True:
    #Establish the connection
    
    connectionSocket, addr = serverSocket.accept() #are you accepting connections?
    
    try:
       #a client is sending you a message 
      message = connectionSocket.recv(1024)
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    

      validResponseHeader = "HTTP/1.1 200 OK\r\n"
            
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
    
               
      for i in f: #for line in file
        outputdata = f.read()
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      
      connectionSocket.sendall((validResponseHeader + outputdata).encode())

      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block

      errorResponseHeader = "HTTP/1.1 404 Not Found\r\n"
      connectionSocket.send(errorResponseHeader.encode())

      #Close client socket
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)
