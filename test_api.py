import requests

BASE_URL = "http://127.0.0.1:8000"

# Create a new task
task = {"id": 1, "title": "Learn FastAPI", "description": "Deep dive into FastAPI", "completed": False}
response = requests.post(f"{BASE_URL}/tasks/", json=task)
print("POST Response:", response.json())

# Get all tasks
response = requests.get(f"{BASE_URL}/tasks/")
print("GET All Tasks:", response.json())

# Get a specific task
response = requests.get(f"{BASE_URL}/tasks/1")
print("GET Task 1:", response.json())

# Update task
updated_task = {"id": 1, "title": "FastAPI Mastery", "description": "Learn FastAPI deeply", "completed": True}
response = requests.put(f"{BASE_URL}/tasks/1", json=updated_task)
print("PUT Response:", response.json())

# Delete task
# response = requests.delete(f"{BASE_URL}/tasks/1")
# print("DELETE Response:", response.json())
