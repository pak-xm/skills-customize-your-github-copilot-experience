# 📘 Assignment: Database Integration with SQLAlchemy

## 🎯 Objective

Take your FastAPI task management API and add persistent database storage using SQLAlchemy ORM. You'll learn how to define database models, establish connections, and replace in-memory data with real database operations—transforming your API from a prototype into a fully functional application.

## 📝 Tasks

### 🛠️ Task 1: Set Up Database Models

#### Description
Define SQLAlchemy models to represent tasks in your database. You'll create a Task model that maps Python objects to database tables.

#### Requirements
Completed program should:

- Define a Task model with fields: id, title, description, completed, created_at
- Configure SQLAlchemy to use SQLite as the database
- Create a database session factory for handling connections
- Set up the database tables (use `Base.metadata.create_all()`)
- Ensure the API still starts without errors


### 🛠️ Task 2: Replace In-Memory Storage with Database Queries

#### Description
Update all GET and POST endpoints to use the database instead of the in-memory list. This makes data persist across server restarts.

#### Requirements
Completed program should:

- Modify the GET `/tasks` route to fetch tasks from the database
- Modify the GET `/tasks/{task_id}` route to query by ID
- Modify the POST `/tasks` route to create and save new tasks to the database
- Return appropriate status codes and error responses when tasks are not found


### 🛠️ Task 3: Implement Database Updates and Deletions

#### Description
Complete the CRUD cycle by updating your PUT and DELETE endpoints to modify and remove database records.

#### Requirements
Completed program should:

- Implement PUT `/tasks/{task_id}` to update tasks in the database
- Implement DELETE `/tasks/{task_id}` to remove tasks from the database
- Commit changes to the database after each operation
- Handle errors gracefully when a task ID doesn't exist


### 🛠️ Task 4: (Stretch) Add Advanced Queries and Relationships

#### Description
Enhance your API with more sophisticated database queries and optional data relationships.

#### Requirements
Completed program should:

- Add query filters (e.g., filter tasks by completed status, sort by creation date)
- Implement pagination for the GET `/tasks` route to handle large datasets
- (Optional) Add a Category model and define relationships between tasks and categories
- Return filtered or paginated results appropriately
