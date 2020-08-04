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

print ("Auth status code: " + str(r_auth.status_code))
Auth_reply = r_auth.json()
# print(Auth_reply)
# type(Auth_reply)

token = Auth_reply['access_token']
# print(token)

GMOC_ID = "145176118"

url_enodeb = 'http://10.132.59.6:25080/rest/radio/4g/enodeb/xid'

params_enodeb_network = {
    "xid": GMOC_ID,
    "perspective":"NETWORK"
}

params_enodeb_live = {
    "xid": GMOC_ID,
    "perspective":"LIVE"
}

headers_enodeb = {
    "Accept": "application/json;charset=utf-8",
    "Authorization" : "Bearer " + token
}

r_enodeb_network = requests.get(url_enodeb, headers=headers_enodeb, params=params_enodeb_network)

print("Codigo respuesta enodeb network: " + str(r_enodeb_network.status_code))

r_enodeb_live = requests.get(url_enodeb, headers=headers_enodeb, params=params_enodeb_live)

print("Codigo respuesta enodeb live: " + str(r_enodeb_live.status_code))