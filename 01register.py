import requests

url = "http://challenge.code2040.org/api/register"
token = "1d1cd2dc38460b0cf0b90febecd49b95"
repo_url = "https://github.com/frtennis1/cod2040api.git"

data = {'token': token, 'github': repo_url}

r = requests.post(url, data)

