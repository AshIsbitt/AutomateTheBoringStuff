#Assertions in traffic lights

market_2nd = {'ns': 'g', 'ew': 'r'}
mission_16th = {'ns':'r', 'ew':'g'}

def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'g':
			stoplight[key] == 'y'
		elif stoplight[key] == 'y':
			stoplight[key] = 'r'
		elif stoplight[key] == 'r':
			stoplight[key] = 'g'

	assert 'r' in stoplight.values(), 'neither light is red! ' + str(stoplight)

print(switchLights(market_2nd))