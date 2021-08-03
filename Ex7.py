import requests

# TASK 1
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print('Вывод первой задачи: ' + response.text)

# TASK 2
response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print('Вывод второй задачи: ' + response.text)

# TASK 3
method = 'GET'
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=method)
print('Вывод третьей задачи: ' + response.text)

# TASK 4
methods = ['get', 'post', 'put', 'delete']
requests_methods = [requests.get, requests.post, requests.put, requests.delete]
request_url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

for i in methods:
    requestGet = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=i)
    print('Вывод четвертой задачи (GET_URL): ' + requestGet.url)
    print('Вывод четвертой задачи (GET_TEXT): ' + requestGet.text)
    requestPost = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', params=i)
    print('Вывод четвертой задачи (POST_URL): ' + requestPost.url)
    print('Вывод четвертой задачи (POST_TEXT): ' + requestPost.text)
    requestPut = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', params=i)
    print('Вывод четвертой задачи (PUT_URL): ' + requestPut.url)
    print('Вывод четвертой задачи (PUT_TEXT): ' + requestPut.text)
    requestDelete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', params=i)
    print('Вывод четвертой задачи (DELETE_URL): ' + requestDelete.url)
    print('Вывод четвертой задачи (DELETE_TEXT): ' + requestDelete.text)