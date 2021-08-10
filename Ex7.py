import requests

# TASK 1
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print('Вывод первой задачи: ' + response.text)

# TASK 2
response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print('Вывод второй задачи: ' + response.text)

# TASK 3
method = 'POST'
response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": 'POST'})
print('Вывод третьей задачи: ' + response.text + ' ' + response.url)

# TASK 4
methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
requests_methods = [requests.get, requests.post, requests.put, requests.delete]
request_url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

for i in methods:
    if i == 'GET':
        requestGet = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": 'GET'})
        print('Вывод четвертой задачи (GET->GET): ' + requestGet.text)
        requestGet = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": 'POST'})
        print('Вывод четвертой задачи (GET->POST): ' + requestGet.text)
        requestGet = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": 'PUT'})
        print('Вывод четвертой задачи (GET->PUT): ' + requestGet.text)
        requestGet = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                  data={"method": 'DELETE'})
        print('Вывод четвертой задачи (GET->DELETE): ' + requestGet.text + '\n')

    if i == 'POST':
        requestPost = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                    data={"method": 'POST'})
        print('Вывод четвертой задачи (POST->POST): ' + requestPost.text)
        requestPost = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                    params={"method": 'GET'})
        print('Вывод четвертой задачи (POST->GET): ' + requestPost.text)
        requestPost = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": 'PUT'})
        print('Вывод четвертой задачи (POST->PUT): ' + requestPost.text)
        requestPost = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                    data={"method": 'DELETE'})
        print('Вывод четвертой задачи (POST->DELETE): ' + requestPost.text + '\n')

    if i == 'PUT':
        requestPut = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": 'PUT'})
        print('Вывод четвертой задачи (PUT->PUT): ' + requestPut.text)
        requestPut = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": 'GET'})
        print('Вывод четвертой задачи (PUT->GET): ' + requestPut.text)
        requestPut = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": 'POST'})
        print('Вывод четвертой задачи (PUT->POST): ' + requestPut.text)
        requestPut = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                  data={"method": 'DELETE'})
        print('Вывод четвертой задачи (PUT-DELETE): ' + requestPut.text + '\n')

    if i == 'DELETE':
        requestDelete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                        data={"method": 'DELETE'})
        print('Вывод четвертой задачи (DELETE->DELETE): ' + requestDelete.text)
        requestDelete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                        params={"method": 'GET'})
        print('Вывод четвертой задачи (DELETE->GET): ' + requestDelete.text)
        requestDelete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                        data={"method": 'POST'})
        print('Вывод четвертой задачи (DELETE->POST): ' + requestDelete.text)
        requestDelete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                        data={"method": 'PUT'})
        print('Вывод четвертой задачи (DELETE->PUT): ' + requestDelete.text + '\n')

    if i == 'PATCH':
        requestPatch = requests.patch('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                      data={"method": 'PATCH'})
        print('Вывод четвертой задачи (PATCH): ' + requestPatch.text)