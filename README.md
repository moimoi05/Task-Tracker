# Task Tracker

A robust Python-based Task Tracker application for efficient task management. This tool allows you to add, update, delete, and view tasks with detailed properties such as ID, description, status, and timestamps.

## Features

- **Add Tasks**: Create tasks with unique IDs and descriptions.
- **Update Tasks**: Modify task details including description and status.
- **Delete Tasks**: Remove tasks by ID.
- **Mark Tasks**: Set tasks as todo, in-progress, or done.
- **List Tasks**: Display all tasks or filter by specific statuses.
- **Automatic File Creation**: Generates `task.json` if it does not exist.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

### File Structure
Task_Tracker/
│
├── task.json # Stores task data
├── Task_Tracker.py # Main application script
└── README.md # Documentation

### Installation

1. Clone this repository or download the source files.
2. Ensure the `Task_Tracker.py` script and `task.json` file are in the same directory.

## How to Use

### 1. Run the Script

Execute the script using Python:

sh
python Task_Tracker.py

2. Choose an Option from the Menu
After running the script, you will see a menu like this:
CHOOSE YOUR OPTION BELOW:
1. ADD TASK
2. UPDATE TASK
3. DELETE TASK
4. MARK TASK
5. LIST ALL TASKS
6. LIST TASKS BY STATUS (DONE)
7. LIST TASKS BY STATUS (TODO)
8. LIST TASKS BY STATUS (IN PROGRESS)
9. EXIT
3. Options Breakdown
1	Add a new task by specifying a unique ID and description.
2	Update an existing task's description or status.
3	Delete a task by its ID.
4	Mark a task with a specific status (todo, in-progress, or done).
5	List all tasks, displaying ID, description, status, createdAt, and updatedAt details.
6	List all tasks with the status done.
7	List all tasks with the status todo.
8	List all tasks with the status in-progress.
9	Exit the program.

Example Walkthrough
Adding a Task
Choose option 1.
Enter a unique task ID (e.g., 1).
Enter a description (e.g., Buy groceries).
The task will be saved with the default status: todo and timestamps.
Updating a Task
Choose option 2.
Enter the task ID (e.g., 1).
Update the description (optional) and/or status (e.g., done).
Deleting a Task
Choose option 3.
Enter the task ID to delete.
JSON Data Format
The tasks are saved in a file named task.json with the following structure:
{
    "1": {
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2024-11-29T10:00:00",
        "updatedAt": "2024-11-29T10:00:00"
    },
    "2": {
        "description": "Clean the house",
        "status": "done",
        "createdAt": "2024-11-29T09:30:00",
        "updatedAt": "2024-11-29T10:15:00"
    }
}
Customization
You can modify the default statuses or additional task properties by editing the script directly.

License
This project is released under the MIT License. Feel free to use and modify it as needed.

This README ensures a smooth introduction to the project and provides clear guidance for end-users. Save it as README.md in your project directory.
