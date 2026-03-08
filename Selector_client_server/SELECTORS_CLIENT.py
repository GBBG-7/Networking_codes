#!/bin/python3
import socket , selectors

#This python script just follow the client-server model
#but i used setectors to monitor ther client  socket. 
#It monitors if data is to be sent on to be received

#catching exception and keyboard Interruption
try:

      HOST = input('Hostname: ') #host to connect to
      PORT = int(input('Port: ')) #port number to connect to

except KeyboardInterrupt: #catching the keyboard
      
      HOST = None #set host to None if keyboard Interrupted
      PORT = None #set port to None if Keyboard Interrupted
      
      print('\n')
      
except Exception as exc:  #catching an error
      
      HOST = None #set host to None if an error occurs
      PORT = None #set host to None if error occurs
      print('\nInvalid Auguments')
      


def client_socket_object():
      """
            This function returns the socket object that wil connect to the server
            It connect  to the host and port provided 
     """
     
      #catching exception and keyboard Interruption
      try: 
            #condition to verify if there are legit values in host and port     
            if HOST and PORT is not None and '.' in HOST  : 
            
                 address_family = socket.AF_INET #specify the address faimily
                 transport_type = socket.SOCK_STREAM #specify the transport type 
       
                 sock = socket.socket( address_family , transport_type ) #create the socket function 
                 sock.connect((HOST , PORT)) #connect to host and port 
                 print(f'Connected to [{HOST}:{PORT}]\n')
       
                 return sock #return the socket after creation    
            
            else:
                 return None   #if the condition failes return None  
      except ConnectionError: # catching ConnectionError exception 
                 print(f'Unable to connect to [ {HOST}:{PORT} ]')
      except ConnectionRefusedError: #catching ConnectionRefusedError
                 print('Connection Refused')
      except Exception as exc: #catching any other exception that occcurs
                 print(exc)
      except KeyboardInterrupt: #catching the keyboard 
                 print('\n')
                
def selector_events():
    """
         This is where the setector process happens(The monitoring).
         The client socket is retrieved and a setector object is also created
         that registers the client socket with the approriate events   
    
    """
    #catching exception and Keybaord Interruption 
    try:   
          client_socket = client_socket_object()  #retrieving the socket object     
          
          if client_socket is not None: #verifying if the client socket was retrieved
               client_socket_fd = client_socket.fileno() #the file descriptor of the client socket 
       
               selector_obj = selectors.DefaultSelector() #the selector object  for the monitoring 
               selector_obj.register(client_socket_fd , selectors.EVENT_WRITE , data= 'Write_to_server') #register the client socket with a write event and an additional data        
       

               while True: #a loop to run the client socket unit interrupted
               
                          selector_process = selector_obj.select() #a select object that returns a selector key object and the events registered  
        

               
                          for selector_key , event in selector_process: #using the selector key object and events
                                 
                                 #a condition to verify  the event and the additional data registered   
                                 if event & selectors.EVENT_WRITE and selector_key.data=='Write_to_server': 
                                    
                                    #return the client socket
                                    sock = client_socket
                                    
                                    
                                    message = input('Data: ') #ask for the data to be sent
                                    encoded_message = message.encode() #encode the data to sent
                                    n_bytes = sock.send(encoded_message) #send the data
                                    print(f'Sent: [{n_bytes} bytes]') 
                       
                                    selector_obj.modify(sock , selectors.EVENT_READ , data='Read_from_server') #modify the socket after sending the data
                                 
                                 #another condition to verify the event and additional data registered
                                 elif  event & selectors.EVENT_READ and selector_key.data=='Read_from_server':
                                    
                                    #return the client socket
                                    sock = client_socket
                                    received_data = sock.recv(4096) #receive data sent by the server  

                                    if received_data: #verify if data was received 
                                         decoded_data = received_data.decode() #decode the data 
                                         print(f'Received: [{decoded_data}]\n') 
                                         selector_obj.modify(sock , selectors.EVENT_WRITE , data='Write_to_server') #modify the socket after receiving the data
          else:
               print('[Could not connect to server]')                       
    
    #catching exception and keyboard Interruption         
    except Exception as exc:
               print(exc)
    except KeyboardInterrupt:
               print('\n')         

#catching exception and keyboard Interruption
try:
      selector_events() #run the function
except Exception as exc:
      print(exc)
except KeyboardInterrupt:
      print('\n')                         
                      
