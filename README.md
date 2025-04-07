# Task Manager Application

Project URL: https://roadmap.sh/projects/task-tracker
This is an app to manage task, it allows users to add, update, delete and list tasks. The aplication saves the tasks in a JSON file and supports operations to update the status of each one of the tasks. 

## Features

- Add a new task with a description.
- Update tasks information (description/status).
- Delete tasks.
- List tasks according to the filter provided (To-do, In-progress, Done).
- Save the tasks information in a JSON file ('tasks.json').

## Instalation

1. Clone this repository:
   ```bash
   git clone https://github.com/GuidoBitti/TaskTrackerApp.git
   cd taskTracker

2. Install dependences:
   ```bash
   pip install tabulate

## JSON Structure
Every task has the following fields:
  ```json
  [
    {
      "id": 1,
      "description": "Buy milk",
      "status": "To-do",
      "created-at": "2024-12-17 10:00:00",
      "updated-at": "2024-12-17 10:00:00"
    },
    {
      "id": 2,
      "description": "Go to the GYM",
      "status": "In-progress",
      "created-at": "2024-12-16 14:30:00",
      "updated-at": "2024-12-17 10:05:00"
    }
]

  ```

## Usage

This application is used by line commands and it supports the following commands:

1. Add a new task:
   ```bash
   python taskTracker.py add <description of the task>
   ```
2. Update the name of a task:
  ```bash
  python taskTracker.py update <id of the task> <new description of the task>
  ```
3. Delete a task:
  ```bash
   python taskTracker.py delete <id of the task>
  ```
4. Change the status of a task to in-progress
  ```bash
  python taskTracker.py mark-in-progress <id of the task>
  ```
6. Change the status of a task to in-progress
  ```bash
  python taskTracker.py mark-in-progress <id of the task>
  ```
7. Change the status of a task to done
  ```bash
   python taskTracker.py mark-done <id of the task>
  ```
8. List all tasks or filter them by status (to-do, in-progress, done)
  ```bash
   python taskTracker.py list <status filter(blank for all)>
  ```