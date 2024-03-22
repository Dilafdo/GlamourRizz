from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 14,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name": "First name"}

@app.get("/students/{student_id}")
def get_student(student_id: int = Path(description="Id of the student", gt=0, lt=3)):
    return students[student_id]

@app.get("/students-by-name")
def get_student_by_name(name: Optional[str] =  None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "not found"}

## create student endpoint
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: dict):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]