#!/bin/python3
#-*-coding : utf-8-*-
import asyncio , socket

try:
   #host and port for the server to bind and listen
   HOST = input('HOST : ')
   PORT = int(input('PORT : '))

except Exception : #monitors the arguments,if an exception occurs,it catches it and print "INVALID ARGUMENTS"
   HOST = None
   PORT = None
   print('INVALID ARGUMENTS')

except KeyboardInterrupt: #catches keyboard interrupt
   HOST = None
   PORT = None
   print('\nKeyboard Interrupted')

async def client_handler( reader , writer ):

         """
              This simple funciton handle every client that connects to the server,
              it echos data sent from the client back to the client  
              
         """
         #receive data from the client 1024 bytes 
         data = await reader.read(100024)
         d_data = data.decode() #decode the data

         print(f'Server received : {d_data}') #print out the data

         #send the data back to the client 
         writer.write(data)
         await writer.drain() #makes sure data is sent
         writer.close() #close the connection when data is sent  
         await writer.wait_closed() #makes sure connection is closed 

async def server_connection(): 

      """ 
           This is a simple asyncronouse server that is listening on HOST and PORT.
           The function binds to HOST and PORT and listens for connections,when data 
           is sent to the server,the data is echoed back
      """

      try: #for handling exceptions     



           if HOST and PORT: #a condition to check if HOST and PORT have arguments

                  if socket.gethostbyname(HOST): #cross check for valid host

                            server =  await asyncio.start_server(client_handler , HOST , PORT) #asyncronouse server to listen on the Host and port   
                            print(f'Server listening on {HOST} : {PORT}\n')
                            async with server: #context manager for the server
                                        await server.serve_forever()  #server will serve until an error or exception

                  else: #condition if invalid host 
                            print('INVALID ARGUMENTS') 

           else: #condition if no arguments
                            print('Server failed')



      except socket.gaierror as exc: #catching an error
           print(f'Error_B : {exc}')      

      except Exception :# catching an exception 
           print('INVALID ARGUMENTS')

try:                 
     asyncio.run(server_connection()) #running the asyncronouse function 
except KeyboardInterrupt :
     print('\nKeyboard Interrupted')
