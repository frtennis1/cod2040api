import requests
import api_tools

url = api_tools.base_url + 'haystack'
data = {'token' : api_tools.token}

r = requests.post(url, data)
values = r.json()

needle_index = values['haystack'].index(values['needle'])

data.update({'needle': needle_index})
validate_url = url + '/validate'

r_validate = requests.post(validate_url, data)