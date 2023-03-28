import requests
import json

GRAFANA_API_URL = 'http://localhost:3000/api/dashboards/db'
GRAFANA_API_KEY = "eyJrIjoicGZSaVAwTEhrM3YwaXBIUkRWUWhjallCQ3lXSTRGYmYiLCJuIjoiYWRtaW4ta2V5IiwiaWQiOjF9"
PANELS = [
    {
    }
]
dashboard= {
    'title': 'Debug Dashboard',
    'panels': [],
    'editable': True,
    'hideControls': False,
    'timezone': 'browser',
    'time': {
        'from': 'now-6h',
        'to': 'now'
    }
}
payload = {
    'dashboard': dashboard,
    'overwrite': True,
}
response = requests.post(
    GRAFANA_API_URL,
    headers={
        'Authorization': 'Bearer {}'.format(GRAFANA_API_KEY),
        'Content-Type': 'application/json',
    },
    json=payload,
)
print(response.text)
