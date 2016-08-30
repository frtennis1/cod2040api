import requests
import api_tools

url = api_tools.base_url + 'reverse'
data = {'token' : api_tools.token}

r = requests.post(url, data)

data.update({'string': r.text[::-1]})
validate_url = url + '/validate'

r_validate = requests.post(validate_url, data)
