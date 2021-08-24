#downloading files from the web

import requests

res = requests.get('https://AutomateTheBoringStuff.com/files/rj.txt')
print(type(res))

#Check if the status of the request is equal to "OK" (or HTTP code 200)
print(res.status_code == requests.codes.ok)

print(len(res.text))
print(res.text[:250])