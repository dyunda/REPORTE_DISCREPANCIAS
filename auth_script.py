import requests

url_auth = 'http://10.132.59.6:25080/auth/realms/OSS/protocol/openid-connect/token'
payload_auth = {
    "username":"ossadmin",
    "password":"insightadmin",
    "grant_type":"password",
    "client_id":"JBossCore"
}
headers_auth = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

r_auth = requests.post(url_auth, headers=headers_auth, data=payload_auth)

print(r_auth.status_code)
Auth_reply = r_auth.json()
# print(Auth_reply)
# type(Auth_reply)

token = Auth_reply['access_token']
print(token)

GMOC_ID = "145176118"

url_enodeb = 'http://10.132.59.6:25080/rest/radio/4g/enodeb/xid'

params_enodeb = {
    "xid": GMOC_ID,
    "perspective":"NETWORK"
}
headers_enodeb = {
    "Accept": "application/json;charset=utf-8",
    "Authorization" : "Bearer " + token
}

r_enodeb = requests.get(url_enodeb, headers=headers_enodeb, params=params_enodeb)

print("Codigo respuesta enodeb: " + str(r_enodeb.status_code))
print(r_enodeb.json())