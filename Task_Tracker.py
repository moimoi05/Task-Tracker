import json
import os
from datetime import datetime
file_path = r"D:\code\roadmap project py\Task_Tracker\task.json"

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        json.dump({}, file, indent=4)  # Tạo tệp với dictionary rỗng
    print(f"File '{file_path}' created.")

with open(file_path,"r") as file :
      data = json.load(file)

def get_current_time():
    return datetime.now().isoformat()

def ADD_Task(task_id,description):
      if task_id in data:
            print(f"Task with ID '{task_id}' already exists!")
            return
      new_task = {
            "description" : description,
            "status": "NOT DONE",
            "createdAt": get_current_time(),
            "updatedAt": get_current_time()
      }
      data[task_id]=new_task
      with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
      print(f"Task '{task_id}' and description '{description}' was add to list")


def MARK_Task(task_id,status):
      if task_id in data:
            data[task_id]["status"] = status
            data[task_id]["updatedAt"] = get_current_time()
            with open(file_path, "w") as file:
                  json.dump(data, file, indent=4)
            print(f"Task with ID '{task_id}' was marked as '{status}'.")
      else:
        print(f"Task with ID '{task_id}' was not found.")

def UPDATE(task_id,new_description=None,new_status=None):
      if task_id in data:
            if new_description:
                  data[task_id]["description"]=new_description
            if new_status:
                  data[task_id]["status"]=new_status
            data[task_id]["updatedAt"] = get_current_time()
            with open(file_path, "w") as file:
                        json.dump(data, file, indent=4)
            print(f"Task with ID '{task_id}' was updated.")
      else:
            print(f"Task '{task_id}' was not found in list")

def DELETE(task_id):
      if task_id in data:
            del(data[task_id])
            with open(file_path, "w") as file:
                        json.dump(data, file, indent=4)
            print(f"Task '{task_id}' was deleted in list'")
      else:
            print(f"Task '{task_id}' was not found in list")

def LIST_ALL_TASKS():
    print(f"{'Task ID':<10} {'Description':<20} {'Status':<15} {'Created At':<25} {'Updated At':<25}")
    print("-" * 95)
    for task_id, task_details in data.items():
        print(f"{task_id:<10} {task_details['description']:<20} {task_details['status']:<15} {task_details['createdAt']:<25} {task_details['updatedAt']:<25}")

def LIST_TASKS_BY_STATUS(target_status):
    print(f"{'Task ID':<10} {'Description':<20} {'Status':<15}")
    print("-" * 45)
    for task_id, task_details in data.items():
        if task_details["status"] == target_status:
            print(f"{task_id:<10} {task_details['description']:<20} {task_details['status']:<15}")

# menu

while True:
      print("CHOOSE YOUR OPTION BELOW: ")
      print("1. ADD TASK")
      print("2. UPDATE TASK")
      print("3. DELETE TASK")
      print("4. MARK TASK")
      print("5. LIST ALL TASKS")
      print("6. LIST ALL TASKS ARE DONE")
      print("7. LIST ALL TASKS ARE NOT DONE")
      print("8. LIST ALL TASKS ARE IN PROGRESS")
      print("9. EXIT")

      choice = input("Enter your choice: ")
      if choice == "1":
        task_id = input("Enter task ID: ")
        description = input("Enter task description: ")
        ADD_Task(task_id, description)
      elif choice == "2":
            task_id = input("Enter task ID to update: ")
            new_description = input("Enter new description (or press Enter to skip): ")
            new_status = input("Enter new status (todo/in-progress/done or press Enter to skip): ")
            UPDATE(task_id, new_description if new_description else None, new_status if new_status else None)
      elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            DELETE(task_id)
      elif choice == "4":
            task_id = input("Enter task ID to mark: ")
            status = input("Enter status (todo/in-progress/done): ")
            MARK_Task(task_id, status)
      elif choice == "5":
            LIST_ALL_TASKS()
      elif choice == "6":
            LIST_TASKS_BY_STATUS("DONE")
      elif choice == "7":
            LIST_TASKS_BY_STATUS("NOT DONE")
      elif choice == "8":
            LIST_TASKS_BY_STATUS("IN PROGRESS")
      elif choice == "9":
            print("Exiting program.")
            break
      else:
            print("Invalid choice, please try again.")