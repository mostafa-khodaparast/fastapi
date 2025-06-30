from fastapi import FastAPI

api = FastAPI()

all_todos = [
   {'todo_id': 1, 'todo_name': 'sports', 'todo_description': 'go to the gym'},
   {'todo_id': 2, 'todo_name': 'read', 'todo_description': 'go to the gym'},
   {'todo_id': 3, 'todo_name': 'shop', 'todo_description': 'go to the gym'},
   {'todo_id': 4, 'todo_name': 'study', 'todo_description': 'go to the gym'},
   {'todo_id': 5, 'todo_name': 'meditate', 'todo_description': 'go to the gym'}, 
]

#pass parameter
@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return { 'result': todo}

#query parameter    
#fastapi use pydantic, so type should be given to variables    
@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos