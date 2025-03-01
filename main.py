from fastapi import FastAPI, HTTPException

app = FastAPI()

users_db = {}
courses_db = {
    "AI": {
        "description": "Learn about AI and large language models.",
        "content": "Course content goes here."
    }
}

@app.post("/register")
def register(username: str, password: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[username] = password
    return {"message": "User registered successfully"}

@app.post("/login")
def login(username: str, password: str):
    if users_db.get(username) != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.get("/courses/{course_name}")
def get_course(course_name: str):
    course = courses_db.get(course_name)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
