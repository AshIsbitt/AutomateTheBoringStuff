# Creating a multithread code

import time
import threading


def takeANap():
    time.sleep(5)
    print('Wake up')


'''
We tell the thread what function to run, but don't include the brackets takeANap() because we don't just
want the returned value of the function

Note that the 'end of code' print statement will print before the 'wake up' statement in the function
because main thread of the code will keep going line by line when a second thread hits the threading.Thread
line to run the function

Make sure when using multithreading, ALWAYS use local variables
'''
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('end of code')
