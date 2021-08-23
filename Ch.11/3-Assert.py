#Assertions

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]

ages.sort()

#This returns true
assert ages[0] <= ages[-1]

#This will return an AssertionError
ages.reverse()
assert ages[0] <= ages[-1]