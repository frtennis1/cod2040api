import requests
import api_tools
from dateutil.parser import parse
from datetime import datetime, timedelta

url = api_tools.base_url + 'dating'
data = {'token' : api_tools.token}

r = requests.post(url, data)
values = r.json()
dt = parse(values['datestamp'])
dt = dt + timedelta(seconds=values['interval'])

# the hacky replace makes me sad for timezone format, too, 
# but haven't gotten around to making a clean solution
dt_str = dt.isoformat().replace('+00:00', 'Z')

data.update({'datestamp': dt_str})
validate_url = url + '/validate'
r_validate = requests.post(validate_url, data)

print r_validate.text