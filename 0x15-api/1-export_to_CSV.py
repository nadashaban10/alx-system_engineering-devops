#!/usr/bin/python3
'''Python script that
returns information about his todo list progress.
'''
if __name__ == "__main__":
    import requests
    from sys import argv

    urlUser = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_name = requests.get(urlUser)
    name = response_name.json()['username']

    urlTodo = urlUser + '/todos'
    response_todos = requests.get(urlTodo)
    tasks = response_todos.json()
    total_task = len(tasks)
    with open(f"{argv[1]}.csv", "w") as file:
        for task in tasks:
            file.write(f'"{argv[1]}","{name}","{task["completed"]}","{task["title"]}"\n')
