# Time module

import time

print(time.time())

# This will output the time in a human-readable format
print(time.ctime())

# ---------------------------------

# Calculate product of first 100,000 numbers


def calcProd():
    product = 1

    for i in range(1, 100000):
        product = product * i

    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print(f'Result is {len(str(prod))} digits long')

# Get how long this took to happen
print(f'This took {endTime - startTime} seconds to calculate')

# ----------------------------
