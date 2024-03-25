#!/usr/bin/python3
'''Python script that returns information about his todo list progress in JSON format.'''

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    # Get user ID from argument
    user_id = argv[1]

    # Build URLs for user and todos data
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    url_todo = f'{url_user}/todos'

    # Fetch user data
    response_name = requests.get(url_user)
    name = response_name.json()['username']

    # Fetch and process todo data
    response_todos = requests.get(url_todo)
    tasks = response_todos.json()

    # Prepare data structure for JSON
    user_data = {
        user_id: []
    }

    for task in tasks:
        # Add each task to user data structure
        user_data[user_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": name
        })
    with open(f"{user_id}.json", "w") as file:
        json.dump(user_data, file)

