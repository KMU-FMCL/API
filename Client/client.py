import json

import requests

url = "http://210.123.37.88:65535/gpu_calculate"
headers = {"Content-Type": "application/json"}
data = {"a_list": [1, 2, 3], "b_list": [4, 5, 6]}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("API call success!")
    print(response.json())

else:
    print(f"API call failure. Status code: {response.status_code}")
    print(response.text)
