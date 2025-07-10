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
x = requests.get(url)
print(x.status_code)
print(x.text)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = requests.get(url, auth = ('admin', 'pop4aN94'))
print(x.status_code)
print(x.text)
obj = json.loads(x.text)
json_formatted_str = json.dumps(obj, indent=4)
print(json_formatted_str)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



url = "http://awx.bovre.net:30080/api/v2/job_templates/24/launch/"
#"name": "Show info 200""
x = requests.post(url, auth = ('admin', 'pop4aN94'))

print(x.text)
obj = json.loads(x.text)
json_formatted_str = json.dumps(obj, indent=4)
print(json_formatted_str)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

