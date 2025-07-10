import requests
import pprint
from requests.auth import HTTPBasicAuth
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
auth = HTTPBasicAuth('api', 'a4068becs')
print(requests.get('http://awx.nrslab.eu:30080/api/login', auth=auth))


url = "http://awx.nrslab.eu:30080/api/v2/job_templates/18/"
#"name": "Configure G.8275.2 sync",
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = requests.get(url)
print(x.status_code)
print(x.text)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = requests.get(url, auth = ('admin', 'a4068becs'))
print(x.status_code)
print(x.text)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



url = "http://awx.nrslab.eu:30080/api/v2/job_templates/10/launch/"
#"name": "Show info 200""
x = requests.get(url, auth = ('admin', 'a4068becs'))
print(x.status_code)
print(x.text)
pprint.pprint(x.text)
pretty_json_str = pprint.pformat(x.text, compact=True).replace("'",'"')

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

