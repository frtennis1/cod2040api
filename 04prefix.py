import requests
import api_tools

url = api_tools.base_url + 'prefix'
data = {'token' : api_tools.token}

r = requests.post(url, data)
values = r.json()

lst = filter(lambda s : not s.startswith(values['prefix']), 
    values['array'])

print values['prefix']
print values['array']

print lst

data.update({'array': lst})
validate_url = url + '/validate'
r_validate = requests.post(validate_url, data)

print r_validate.text