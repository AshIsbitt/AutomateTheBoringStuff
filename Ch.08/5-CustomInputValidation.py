# Custom input validation

import pyinputplus as pyin

def addsUpToTen(numbers):
	numbersList = list(numbers)

	for i, digit in enumerate(numbersList):
		numbersList[i] = int(digit)

	if sum(numbersList) != 10:
		raise Exception('The digits must add up to 10, not %s' % (sum(numbersList)))

	return int(numbers)


response = pyin.inputCustom(addsUpToTen, "Enter a series of numbers: ")
print(response)