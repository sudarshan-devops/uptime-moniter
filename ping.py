from sms import SMS
import requests
try:
    r = requests.head("https://google.com")
    print(r.status_code)
except requests.ConnectionError:
    print("failed to connect")
    SMS("enter your number","body of the msg")

