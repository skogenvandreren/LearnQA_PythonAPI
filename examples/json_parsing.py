import json

json_loads = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"}, \
{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_loads)

print(obj['messages'][1])