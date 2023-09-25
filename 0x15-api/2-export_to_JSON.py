#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open(f"{user_id}.json", "w") as f:
        json.dump(
            {
                user_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username"),
                    }
                    for task in todos
                ]
            },
            f,
        )
