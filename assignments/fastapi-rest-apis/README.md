# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating routes, handling HTTP methods, and returning JSON responses. You'll build a task management API that demonstrates CRUD (Create, Read, Update, Delete) operations.

## 📝 Tasks

### 🛠️ Task 1: Set Up Basic Routes

#### Description
Get familiar with FastAPI by creating a basic API with a few simple GET routes. You'll learn how FastAPI works and how to define endpoints that respond to different paths.

#### Requirements
Completed program should:

- Have a root GET route (`/`) that returns a welcome message
- Have a GET route (`/tasks`) that returns a list of sample tasks
- Have a GET route (`/tasks/{task_id}`) that accepts a path parameter and returns a specific task
- Start the server without errors using `uvicorn main:app --reload`


### 🛠️ Task 2: Handle POST Requests

#### Description
Add functionality to create new tasks. Implement a POST route that accepts JSON data and adds tasks to your list.

#### Requirements
Completed program should:

- Have a POST route (`/tasks`) that accepts task data in JSON format
- Validate that the request includes a task title
- Add the new task to the task list with a unique ID
- Return the newly created task with its ID and a success status code (201)


### 🛠️ Task 3: Implement Update and Delete

#### Description
Complete the CRUD operations by implementing routes to update existing tasks and delete them from your list.

#### Requirements
Completed program should:

- Have a PUT route (`/tasks/{task_id}`) that updates a specific task
- Have a DELETE route (`/tasks/{task_id}`) that removes a task from the list
- Return appropriate status codes (200 for success, 404 if task not found)
- Handle edge cases where a task ID doesn't exist


### 🛠️ Task 4: (Stretch) Add Query Parameters and Filtering

#### Description
Enhance your API by adding optional query parameters to filter tasks. This demonstrates how to handle more complex requests.

#### Requirements
Completed program should:

- Add a query parameter to the GET `/tasks` route to filter by completion status (e.g., `/tasks?completed=true`)
- Support filtering by task priority if applicable
- Return only matching tasks based on the query parameters
