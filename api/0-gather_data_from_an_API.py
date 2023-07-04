#!/usr/bin/python3
"""This script retrieves todos for a specific user."""

import json
import requests
import sys

"""Imported modules to be used by the program"""

__author__ = "Junior"

if __name__ == '__main__':
    """Scripts to be executed"""
    id = sys.argv[1]
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    data = json.loads(response.text)
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    result = json.loads(todos.text)
    done = 0
    total = 0
    itemArr = []

    for item in result:
        if data['id'] == item['userId']:
            total += 1
            if item['completed']:
                done += 1
                itemArr.append(item['title'])

    print(f"Employee {data['name']} is done with ({done}/{total})")
    for item in itemArr:
        print(f"\t {item}")
