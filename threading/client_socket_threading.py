"""
Python threading with sockets

Socket Programming-> It helps us to connect a client to a server. Client is message sender and receiver and server is just a listener that works on data sent by client.


What is a Thread? 
A thread is a light-weight process that does not require much memory overhead, they are cheaper than processes.


What is Multi-threading Socket Programming? port on your computer
Multithreading is a process of executing multiple threads simultaneously in a single process.


Multi-threading Modules : 
A _thread module & threading module is used for multi-threading in python, these modules help in synchronization and provide a lock to a thread in use. 


from _thread import *
import threading

A lock object is created by ->


print_lock = threading.Lock()

lock has two states, “locked” or “unlocked”. It has two basic methods acquire() and release(). When the state is unlocked print_lock.acquire() is used to change state to locked and print_lock.release() is used to change state to unlock.
The function thread.start_new_thread() is used to start a new thread and return its identifier. The first argument is the function to call and its second argument is a tuple containing the positional list of arguments.
Let’s study client-server multithreading socket programming by code- 
Note:-The code works with python3. 
Multi-threaded Server Code 
"""




#import socket module
import socket

def Main():
    #local host IP: '127.0.0.1'
    host = '127.0.0.1'

    #define the port you want to connect to
    port = 8080

    s = socket.socket(socket.AF_INET, sicket.SOCK_STREAM)

    #connect to server on local computer
    s.connect((host, port))

    #message you send to server
    message = "This is python threading"
    while True:

        #message sent to server
        s.send(message.encode('ascii'))
        
        #message received from server
        data = s.recv

        """
        print the received message here
        it would be a reverse of sent message
        """

        print("Received from the server: ", str(data.decode('ascii')))

        #ask the client if they want to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break

    #close the connection
    s.close()

if __name__ == '__main__':
    Main()