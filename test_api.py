import requests

url = 'http://127.0.0.1:8000/api/reminder/'
data = {
    # T is a separator for date and time while z at the last represents UTC time zone.
    "datetime": "2025-05-21T17:00:00Z",
    "message": "attend django webinar by Symplique Solutions!",
    "method": "sms"
}

res = requests.post(url, json=data)
print(res.status_code)
print(res.json())
