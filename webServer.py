# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024)
      filename = message.split()[1]
      
      #opens the client requested file. 
      f = open(filename[1:], "rb") #fill in start #fill in end

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      validResponseHeader = b"HTTP/1.1 200 OK\r\n"
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"

      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      for i in f: #for line in file
        #Fill in start - append your html file contents #Fill in end 
        connectionSocket.send(i)

      # Fill in start
      connectionSocket.send(validResponseHeader + outputdata)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      errorResponseHeader = b"HTTP/1.1 404 Not found \r\n"
      connectionSocket.send(errorResponseHeader)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()

      #Fill in end  

if __name__ == "__main__":
  webServer(13331)

