import requests
import sys
import json
''' This module allows us to interact with APIs'''
id = sys.argv[1]
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
data = json.loads(response.text)
todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
result = json.loads(todos.text)
done = 0
total = 0
itemArr = []
for item in result:
    if (data['id'] == item['userId']):
        total = total + 1
        if (item['completed'] == True):
            done = done + 1
            itemArr.append(item['title'])
print(f"Employee {data['name']} is done with ({done}/{total})")
for item in itemArr:
    print(f'\t {item}')
