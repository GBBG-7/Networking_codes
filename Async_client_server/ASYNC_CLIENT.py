#!/bin/python3
#-*-coding : utf-8-*-
import asyncio , socket

#This is a simple asyncronouse client that sends data to an
#asyncronouse server listing on HOST and PORT and
#wait for data to be sent form the server


#These are the host  and port the client will connect to 
try:
     #the requirments
     HOST = input('HOST : ') #host for the connection
     PORT = int(input('PORT : ')) #port for the connection
     DATA = input('DATA : ') #data to be sent 

except Exception as exc: #catching an Exception 
    #set all the requirments to None
    HOST = None
    PORT = None
    DATA = None
    print('INVALID ARGUMENTS')    

except KeyboardInterrupt: #catching an exception 
    # set all the requirements to None 
    HOST = None
    PORT = None
    DATA = None
    print('\nkeyboard Interrupted')

#The asyncronouse functoin that will connect to the server i.e HOST and PORT 
async def Client_connection():
        """
             This is a simple asyncronouse client that sends data to
             the host : HOST listening an port :PORT ,this is possible
             if all the guards are true,if not the else condition will be 
             executed.After sending the data is wait for data to be 
             sent fron the server  
                
        """

     

        #Firstly ,it starts with checking if data is available in the requirements and
        #if not the instructions in the else clause will be executed.
        #The next thing it dose is another cross check if the requirements 
        #are not empty,it also has an else clause to be excuted when 
        #there is no data
        #On the third  clause,it checks if data in HOST has a dot in it (IP address) 
        #and excete the else clause if the condion failes.
        #The last thing it dose is the it gets the hostname of HOST and if DATA is 
        #an instance of string (which obviously it is ) ,if the condition fails it falls 
        #back to the else clause            
        try:   
              if HOST and PORT and DATA: #data availability
                   if HOST is not None and PORT is not None and DATA is not None: #data availability(cross check)
                        if '.'  in HOST: # a dot HOST
                             if socket.gethostbyname(HOST) and isinstance(DATA , str):  #verifying  HOST and DATA
                                          
                                          #asyncronouse code for the client                                      
                                          reader , writer = await asyncio.open_connection(HOST , PORT)
                                          
                                          #Data to be sent
                                          s_data = DATA.encode()
                                          
                                          #sending data to the server 
                                          writer.write(s_data)
                                          await writer.drain()
                                          
                                          #print out received data
                                          r_data = await reader.read(1024)
                                          d_data = r_data.decode()
                                          print(f'Cient received : {d_data}')
                                          
                            
                             else:#if data is unavailable
                                     print('Connection failed ')

                        else:#if data is unavailable
                                print('Connection failed') 

                   elif HOST is not None and PORT is not None and DATA is None: #a condition to be check
                          print('Connection failed')  

                   else: #if  none of the conditions succeeds 
                           print('Connection failed')              

              else: #if condition failes
                      print('Connection failed')  

        except KeyboardInterrupt:
           print('Keybaord Interrupted')

        except Exception as exc: 
           print(exc)

try:  
      asyncio.run(Client_connection()) #running the function
except KeyboardInterrupt: 
      print('Keyboard Interrupted')
except Exception as exc: 
     print(exc)
