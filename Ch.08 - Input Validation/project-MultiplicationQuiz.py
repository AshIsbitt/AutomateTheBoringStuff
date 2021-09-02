#Project - Multiplication Quiz

import pyinputplus as pyin
import random as r
import time as t

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
	num1 = r.randint(0,9)
	num2 = r.randint(0,9)

	prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

	try:
		pyin.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
						blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)

	except pyin.TimeoutException:
		print("Out of time!")
	except pyin.RetryLimitException:
		print("Out of tries!")
	else:
		print("Correct!")
		correctAnswers +=1

	t.sleep(1)

print("Score: %s/%s" % (correctAnswers, numberOfQuestions))