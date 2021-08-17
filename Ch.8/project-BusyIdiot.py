#Project - How to keep an idiot busy for hours
#(Pretty sure the answer is something to do with buying them a python book)

import pyinputplus as pyin

while True:
	prompt = "Want to know how to keep an idiot busy for hours?\n"
	response = pyin.inputYesNo(prompt)

	if response == "no":
		break

print("Thank you. Have a nice day")