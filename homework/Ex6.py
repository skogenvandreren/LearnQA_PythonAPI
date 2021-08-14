import requests
method = 'GET'
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', method=method)
print(response.history, response.url)