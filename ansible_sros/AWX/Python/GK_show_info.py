import requests
import pprint
import json
from requests.auth import HTTPBasicAuth

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
auth = HTTPBasicAuth('api', 'pop4aN94')
print(requests.get('http://awx.bovre.net:30080/api/login', auth=auth))


url = "http://awx.bovre.net:30080/api/v2/job_templates/"
#"name": "templates",

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = requests.get(url, auth = ('admin', 'pop4aN94'))
print(x.status_code)
print(x.text)
obj = json.loads(x.text)
json_formatted_str = json.dumps(obj, indent=4)
print(json_formatted_str)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#https://www.askpython.com/python/api-calls-bearer-token-authentication
#url = 'https://api.example.com/resource'
headers = {
    'Authorization': 'Bearer vSmeC2edaNaOviDbVFnHHoAOReUQOl',
    'Content-Type': 'application/json'
}
response = requests.get(url, headers=headers)
print(response.text)