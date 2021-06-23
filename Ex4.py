import requests

request = requests.get('https://playground.learnqa.ru/api/get_text')

print(request.text)