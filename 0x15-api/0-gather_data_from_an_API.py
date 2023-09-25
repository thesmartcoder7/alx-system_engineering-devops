#!/usr/bin/python3
"""Return Employee todo list progress for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    dts = [task for task in todos if task.get("completed")]
    print(
        f"Employee {user['name']} is done with tasks({len(dts)}/{len(todos)}):"
    )
    for task in dts:
        print(f"\t {task.get('title')}")
