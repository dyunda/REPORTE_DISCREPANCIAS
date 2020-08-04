import requests

url = 'http://10.132.59.6:25080/auth/realms/OSS/protocol/openid-connect/token'
payload = {
    "username":"ossadmin",
    "password":"insightadmin",
    "grant_type":"password",
    "client_id":"JBossCore"
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url, headers=headers, data=payload)

print(r.status_code)
print(r.json())
