import time
import base64
import json
import requests
from requests.auth import HTTPBasicAuth




amount=12
print('amaount')
phone_number = "254715894072"
print(phone_number)

timestamp = str(time.strftime("%Y%m%d%H%M%S"))
passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

password = base64.b64encode(bytes(u'174379' + passkey + timestamp, 'UTF-8')).decode('UTF-8')

consumer_key = "pWAwGCMTPfZBnumveOYZXdaS3Fxyb1nm"
consumer_secret = "GtJvA8kxZ7qmpI1X"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

y = json.loads(requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret)).text)
access_token = "{}".format(y['access_token'])
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = {"Authorization": "Bearer {}".format(access_token)}
body = {
"BusinessShortCode": "174379",
"Password": "{}".format(password),
"Timestamp": "{}".format(timestamp),
"TransactionType": "CustomerPayBillOnline",
"Amount": "10",
"PartyA": "{}".format(phone_number),
"PartyB": "174379",
"PhoneNumber": "{}".format(phone_number),
"CallBackURL": "https://wammpesa.free.beeceptor.com/my/api/path",
"AccountReference": "account",
"TransactionDesc": "test"
}

response = requests.post(api_url, json=body, headers=headers)
response = json.loads(response.text)
print(response)
  
###not a part of the code
import requests, time
r = requests.post('https://wammpesa.free.beeceptor.com/my/api/path', data={"ts":time.time()})
print(r.status_code)
print(r.content)
