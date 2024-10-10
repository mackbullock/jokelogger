#!/usr/bin/python3

import requests
import json
import logging


url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

#print(response)
#gives you 200 instead


#load the text into json
#over writes prev response var
response = json.loads(response.text)

id = response['id']
setup = response['setup']
punchline = response['punchline']

print(id, setup, punchline)
