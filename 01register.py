import requests
import api_tools

url = api_tools.base_url + 'register'
repo_url = "https://github.com/frtennis1/cod2040api.git"
data = {'token': api_tools.token, 'github': repo_url}

r = requests.post(url, data)

