#!/usr/bin/python3
"""Export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open(f"{user_id}.csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    user_id,
                    user.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )
