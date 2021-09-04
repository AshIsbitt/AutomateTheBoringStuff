# Passing arguements to thread's target functions

import threading

# This is the same as running the below line
# print('cats', 'dogs', 'frogs', sep=' & ')

threadObj = threading.Thread(
    target=print, args=['cats', 'dogs', 'frogs'], kwargs={'sep': ' & '})
threadObj.start()
