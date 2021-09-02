#Assertions

#Assertions should NOT use try/except statements, and should crash the code so you can 
#See where the errors are - These are for errors you've made, not for errors in the code (syntax error)


ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]

ages.sort()

#This returns true
assert ages[0] <= ages[-1]

#This will return an AssertionError
ages.reverse()
assert ages[0] <= ages[-1]