from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
   

app = FastAPI()
import os

API_KEY = os.getenv("API_KEY") #or "123456ABCDEF"
@app.middleware("http")
async def check_api_key(request, call_next):
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})

    return await call_next(request)

@app.get("/welcome")
def welcome():
    return {
        "message": "Welcome to the FastAPI application!"
    }


@app.get("/users")
def get_users():
    return {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }

@app.get("/users/{user_id}")
def user_profile(user_id: int):

    if (user_id == 1):
        return {
            "name": "Sanjay Kumar",
            "Channel": "Applied With AI - Tamil",
            "Website": "https://appliedwithai.in/",
            "LinkedIn": "https://www.linkedin.com/in/sanjayssn/"
        }

    else:
        return {
            "name": "John" + str(user_id),
            "Channel": "Applied With AI - English",
            "Website": "https://appliedwithai.in/",
            "LinkedIn": "https://www.linkedin.com/in/sanjayssn/"
        }
    
class User(BaseModel):
    name: str
    age: int
    email: str   

users = [];

@app.post("/user")

def create_user(user: User):
    users.append(user)
    return {
        "message": "User created successfully",
        "total_users": len(users)
    }

