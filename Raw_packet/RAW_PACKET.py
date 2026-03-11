#!/bin/python3
#-*-coding : utf-8-*-
import socket , codecs 

#function for the socket
def socket_function( interface : str  ,  protocol : str ):
      '''  This is a smple socket object that intercepts a network interface 
            and just print out raw data being transmitted through the network
      '''
      #Dictionary of available protocols 
      Protocol_dict = {'IPV4' : 0x0800 , 'IPV6' : 0x86DD , 'ARP' : 0x0806 , 'ALL' : 0x0003}
    
      if socket.if_nametoindex(interface) and protocol in Protocol_dict:
      
          try:  
             
             proto_num = Protocol_dict.get( protocol , None) #retrieveing the portocol from the dict  
             sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW , socket.htons(proto_num)) #creating the socket
             sock.bind((interface , 0)) #binding to the interface and protocol ( 0 means using the socket protocol)
             
             return sock #return the socket object
             
          except OSError as exc: #catching an exception
             print(f'\nError_B : {exc}')
          except Exception as exc:    
             print(exc)
             
      
      else:

          return None #return None if an invalid protocols are used

def handle_data():
   try:
    
       interface = input('Network interface : ') #Interface for the socket function
       print('Available Protocol : IPv4 | IPv6 | ARP | ALL ') 
       protocol = input('Protocol : ') # protocol for the socket function
       
       s_obj  = socket_function(interface , protocol.upper()) #return the socket object
       
       try:
           
           if s_obj is not None: #a condional statement
              
              while True: # loop
                
                  raw_data = s_obj.recv(1024) #recieveing transmitted data (1024 bytes)
                  d_data = codecs.decode(raw_data , encoding='utf-8' , errors='replace') # Decodeing the data with utf-8 encoding standards 
                  print(d_data)
                                               
           else:
                    print('\nConnection  failed')

       except OSError as exc:
                    print(f'\nError_C: {exc} [{interface}]')
                    
       except Exception as exc:
                    print(f'\n')
   
   except KeyboardInterrupt :
                    print('\nKeyboard Interrupted')
                    
   except Exception as exc:
                    print(f'\nError_D : {exc}')    
                        
try:                           
     handle_data() #calling the function
except KeyboardInterrupt:
     print('\n')             
                
