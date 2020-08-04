import requests

url_auth = 'http://10.132.59.6:25080/auth/realms/OSS/protocol/openid-connect/token'
payload = {
    "username":"ossadmin",
    "password":"insightadmin",
    "grant_type":"password",
    "client_id":"JBossCore"
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url_auth, headers=headers, data=payload)

print(r.status_code)
Auth_reply = r.json()
# print(Auth_reply)
# type(Auth_reply)

token = Auth_reply['access_token']
print(token)
