These scripts demonstrate how the client-server model works 
but with the help poll.The client socket is checked if an event has
happened ,data is ready or a change has occured


NOTE: Make sure you have python installed on your machine,
             you can download python by typing python into the terminal
             which will redirect you to microsoft store to download python 

Run the server before the client

You first execute the server by running python SELECTORS_SERVER.py,
specify the host and port number the server will listen and monitor.At this
point the server will be listing for any connection a client,when a client
connection is made,the server will be prompt.The server is designed to 
echo back data sent by the client

Secodly,you run the client,run python  SELECTORS_CLIENT.py,specify the 
host to connect to and the port number,when the connection is successful
you will be promt,you then type the data to be sent to the server,the data
sent to the server must be received because the server echoes data back 
unless you change the code  

The server and client will run untill interrupted,the client will keep 
asking for data if the server sends data

[I am just practicing so I don't forget how to write it]
