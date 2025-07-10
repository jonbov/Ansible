import requests
import pprint
from requests.auth import HTTPBasicAuth
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
auth = HTTPBasicAuth('api', 'pop4aN94')
print(requests.get('http://awx.bovre.net:30080/api/login', auth=auth))


url = "http://awx.bovre.net:30080/api/v2/job_templates/24/"
#"name": "templates",
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = requests.get(url)
print(x.status_code)
print(x.text)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = requests.get(url, auth = ('admin', 'pop4aN94'))
print(x.status_code)
print(x.text)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



url = "http://awx.bovre.net:30080/api/v2/job_templates/24/launch/"
#"name": "Show info 200""
x = requests.get(url, auth = ('admin', 'pop4aN94'))
print(x.status_code)
print(x.text)
pprint.pprint(x.text)
pretty_json_str = pprint.pformat(x.text, compact=True).replace("'",'"')

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

