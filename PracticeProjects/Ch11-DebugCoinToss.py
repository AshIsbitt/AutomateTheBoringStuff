# Debugging Coin Toss

import random
import logging

logging.basicConfig(level=logging.DEBUG, 
					format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
tossValue = ''

'''
Bugs found:
toss (0, 1) can't equal guess (h, t)
	- Fixed by adding the tossValue var and changed "toss" in second IF statement to tossValue

Added logging code, currently printing to terminal
Reformated main loop of code to run better and be better written
'''

logging.debug('Program start')

toss = random.randint(0,1)
if toss == 0:
	tossValue = 't'
elif toss == 1:
	tossValue = 'h'

logging.info(f'tossValue = {tossValue}')

assert tossValue == 'h' or tossValue == 't'


for i in range(0,2):
	while guess not in ('h', 't'):
		print('Guess the coin toss! Enter heads or tails')
		guess = input()
		logging.info(f'guess = {guess}')

	if tossValue == guess:
		print('You got it!')
	else:
		print('Nope')
		guess = ''
		if i == 1:
			print('You really are bad at this game')

# if tossValue == guess:
# 	print('You got it!')
# else:
# 	print('Nope, guess again')
# 	guess = input()
# 	logging.info(f'guess = {guess}')

# 	if tossValue == guess:
# 		print('You got it!')
# 	else:
# 		print('You really are bad at this game')

logging.debug('Program end')