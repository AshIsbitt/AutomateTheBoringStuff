# reading JSON

import json

stringOfData = '{"name": "Zophie", "isCat":true, "miceCaught":0, "felineIQ":null}'

jsonDataAsPythonValue = json.loads(stringOfData)
print(jsonDataAsPythonValue)

'''
{'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIO': None}

Note the difference between the final value of "null" in JSON and "None" in python output
'''
