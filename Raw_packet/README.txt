UNIX only

This folder contains a  python scripts that will intercept a network interface
and capture raw packets on the network ,it captures the raw data being transmitted
over the network  


NOTE: Make sure you have python installed on your machine

Because the program will access resources of the operating system,
high privilages will be needed,so you run as root or give the script root
privilages.

When you run the script,you will be prompt to enter  the network 
interface you want intercept , next the protocol that will 
be used to capture the packet,Only available protocols are valid.
Click enter to start accepting the packets 

If the connection  is securely  connected,the data you 
will receive will be encrypted,the data is decoded using
utf-8 and if utf-8 cannot decode the encrypted data a question mark '?'
is replaced  


[I am just practicing so I don't forget how to write it]
