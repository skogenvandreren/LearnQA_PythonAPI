import time
import requests

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

# Дёргаем запрос и переводим его в json
response = requests.get(url)
parsed_response_text = response.json()
print ('Шаг 1: \nЗадача создана\n')

# Вытаскиваем полученные значения из словаря
token = (parsed_response_text['token'])
seconds = (parsed_response_text['seconds'])

# Отправляем запрос до готовности задачи
response = requests.get(url, params={'token': token})
parsed_response_text = response.json()
if parsed_response_text['status'] == 'Job is NOT ready':
    print('Шаг 2: \nЗадача ещё не готова:\n' + response.text + '\n')
else:
    print('Шаг 2: \nЗадача готова:\n' + response.text + '\n')

# Ожидаем готовности задачи
time.sleep(seconds)
print(f'Шаг 3: \nЖдём {seconds} секунд(ы)\n')

# Отправляем запрос после готовности задачи
response = requests.get(url, params={'token': token})
parsed_response_text = response.json()
if parsed_response_text['status'] == 'Job is ready' and parsed_response_text['result'] is not None:
    print('Шаг 4: \nЗадача готова:\n' + response.text + '\n')
else:
    print('Шаг 4: \nЗадача не готова:\n' + response.text + '\n')