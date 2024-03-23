from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

# students = {
#     1: {
#         "name": "John",
#         "age": 14,
#         "class": "year 12"
#     }
# }

@app.get("/")
def index():
    return {"App is working!!"}

@app.post("post-prompt")
def post_prompt(user_id: int, prompt: str, gendre: str):
    return students[student_id]

# @app.get("/students-by-name")
# def get_student_by_name(name: Optional[str] =  None):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"data": "not found"}
#
# ## create student endpoint
# @app.post("/create-student/{student_id}")
# def create_student(student_id: int, student: dict):
#     if student_id in students:
#         return {"Error": "Student exists"}
#     students[student_id] = student
#     return students[student_id]