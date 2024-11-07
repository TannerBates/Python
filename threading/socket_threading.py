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


#import the socket programming library
import socket

#import thread module
from _thread import *
import threading

print_lock = threading.Lock()


#thread function
def threaded(c):
    while True:
        #data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            #lock released on exit
            print_lock.release()
            break

        #reverse the given string from client
        data = data[::-1]

        #send back reversed sting to client
        c.send(data)
    
    #connection closed
    c.close()


def Main():
    host = ""

    """
    reserve a port on your computer.
    in this case it is 8080
    but it can be anything
    """


    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket binded to port ", port)

    #put the socket into listening mode
    s.listen(5)
    print("Socket is listening")

    #a forever loop until the client wants to exit
    while True:

        #establish connection with client
        c, addr = s.accept()

        #lock acquired by client
        print_lock.acquire()
        print('Connected to: ', addr[0], ':', addr[1])

        #start a new thread and return its identifier
        start_new_thread(threaded, (c, ))
    s.close()

if __name__ == '__main__':
    Main()

