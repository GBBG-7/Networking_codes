#!/bin/python3 
import socket , selectors

#This script is built to demonstrate the select() system works
#The select system involves monitoring when data is ready for 
#reading and writing
#
#A server socket is created to listen on PORT and HOSTNAME,
#now the selector object is created to monitors the server socket 
#for readiness which is data to be received and data to be sent  



try:
      
      #hostname and port the server will listen on
      HOSTNAME = input('Hostname: ')  
      PORT = int(input('Port: '))

except KeyboardInterrupt:
      
      #if keyboard in interrupted,set the arguments to  None 
      HOSTNAME = None
      PORT = None


except Exception :
      
      #if an error occurs set  
      HOSTNAME = None
      PORT = None


def server_socket_object():
       """This is a simple function that returns the server socket, 
             selector will monitor this this socket object         
       """       
       
       #if HOSTNAME and PORT unavailable,return None
       try:   
          
          if HOSTNAME and PORT: #a condition to check if HOSTNAME and PORT is true(which means there is data)  
             
             #create a socket server with the appropriate arguments
             sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)   
             sock.setblocking(False) #set to non_blocking
             sock.bind((HOSTNAME , PORT)) #bind to hostname and port
             sock.listen(2) #listen for only two connection
             print('\nListing and Monitoring ...')
             
             return sock #return the socket 
          
          else: #else clause
                  
                  print('\nInvalid Arguments') 
                  return None #return None is the socket failed 
       
       except KeyboardInterrupt: #catching the keyboard
                  print('\nKeyboard Interrupted')
       except Exception as exc: #catching an error
                  print(exc)     


def selector_event():
  
  try:
       
       """
       This function monitors the socket,it monitors if 
       data is to be sent and received
       
       """
       #socket object returned from the function 
       server_sock = server_socket_object()
       
       #if the object return by the function  is not None 
       if server_sock is not None: 
            
            #the selector objecta 
            selector = selectors.DefaultSelector()
            selector.register(server_sock , selectors.EVENT_READ , data='Non_connected_server')
            
            #Tracking the data received
            Payload = {}  
       
            #A loop that that runs the process continueously 
            while True:
             
                  #This is the function that returns selector key object and the events reagistered 
                  select_process = selector.select()
                  
                  #the selector key object and event returned by the function,it hepls monitor the socket
                  for  selector_key , events in select_process: 
                         
                         #This dose a comparison,it checks if the key object's file descriptor is the same as the socket file descriptor'
                         # It checks the events registered,it monitors if data is available for reading and also check the data that was
                         #registered        
                         
                         if selector_key.fileobj.fileno() == server_sock.fileno() and events & selectors.EVENT_READ and selector_key.data=='Non_connected_server':
                            
                           try:
                                sock = selector_key.fileobj #return the socket object
                          
                                connection , address = sock.accept() #accept every connection a client make 
                                print(f'{address} connected to the server')
                                
                                connection.setblocking(False) #set the socket to non-blocking
                          
                                selector.unregister(sock) #unregister the unconnected sock
                                selector.register(connection , selectors.EVENT_READ , data='Connected_Server') #register the client connection 
                           except Exception as exc: #catching an exception 
                                print(exc)
                           except KeyboardInterrupt: #catching the keyboard 
                                print('\nKeyboard Interrupt')   
                                
                         #This is another condition that verifies the file descriptor of both the socket and the selector key object , the event
                         #registered and the arbituary data registered
                         
                         elif selector_key.fileobj.fileno() is not server_sock.fileno() and events & selectors.EVENT_READ and selector_key.data =='Connected_Server':
                    
                           try:  
                             sock = selector_key.fileobj #return the socket object
                             data_received = sock.recv(4096) #receive 1024 bytes from the socket
                        
                             if data_received: #cross check if data was received 
                        
                                 Payload['Received_data'] = data_received #add the data received as a dictionary to Payload 
                            
                                 decoded_data = data_received.decode() #decode the data received 
                                 print(f'\nServer recieved: {decoded_data}')
                            
                                 selector.modify(sock , selectors.EVENT_WRITE , data='Write_to_server') #modify the event and the data of the socket registered
                           
                           #catching errors
                           except ConnectionError as exc: 
                                 print(f'\n[{address}] closed its connection')
                           except ConnectionRefusedError as exc:
                                 print(exc , 'b')
                           except BrokenPipeError as exc:
                                 print(exc , 'c')      
                           except Exception as exc:
                                 print(exc , 'd')
                           except KeyboardInterrupt:
                                 print('\nKeyboard Interruped')
                    
                         #similar to the previouse one compares the file descriptor ,the events and the data registered   
                         elif selector_key.fileobj.fileno() is not server_sock.fileno() and events & selectors.EVENT_WRITE and selector_key.data == 'Write_to_server':
                        
                             try:   
                                sock = selector_key.fileobj #return the socket object 
                                data = Payload['Received_data'] #get the received data from the Payload  
                         
                                if data: #cross check if data was retrieved
                               
                                    no_bytes = sock.send(data) #echo back the data to the client and return the number of bytes sent 
                                    print(f'{no_bytes} bytes echoed back')
                                    selector.modify(sock , selectors.EVENT_READ , data='Connected_Server' ) #alter the event and data of he socket with selector  
                        
                             #Catching errors and Keyboard Interruption
                             except ConnectionError as exc:
                                    print(exc , 'e')
                             except ConnectionRefusedError as exc:  
                                    print(exc , 'f')
                             except BrokenPipeError as exc:
                                    print(exc , 'g')
                             except Exception as exc:
                                    print(exc , 'h') 
                             except KeyboardInterrupt: 
                                    print('\nKeyboard Interrupt')
       else: #else clause that dose nothing
            ...
                 
               
  except Exception as exc: #catching an error 
        print(exc , 'i')
  except KeyboardInterrupt: #catching keyboard Interruption
        print('\nKeyboard Interrupted')                              
                         
try:                       
      selector_event() #run the function
#catchinh errors and keyboard Interruption
except KeyboardInterrupt:
      print('\nKeyboard Interrupted')
except Exception as exc:
      print(exc , 'j')     
                       
       
       
