import requests

payload = {"name": "Amir"}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
print(response.text)