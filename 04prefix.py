import requests
import api_tools
import json

url = api_tools.base_url + 'prefix'
data = {'token' : api_tools.token}

r = requests.post(url, data)
values = r.json()

lst = filter(lambda s : not s.startswith(values['prefix']), 
    values['array'])

validate_url = url + '/validate'
data.update({'array': lst})
headers = {'content-type': 'application/json'}
r_validate = requests.post(validate_url, json=data, headers=headers)

print r_validate.text