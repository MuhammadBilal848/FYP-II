import uvicorn
from fastapi import FastAPI , Path ,UploadFile ,File,Form
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Notes(BaseModel):
    subject : str
    image : UploadFile

class TextNotes(BaseModel):
    subject : Optional[str]
    text : Optional[str]

db = []

@app.post("/post-image_notes/")
async def image_notes(*,file: UploadFile = File(...), subject : str ):
    contents = await file.read() 
    db.append(file)
    db.append(subject)
    with open(file.filename, "wb") as f:
        f.write(contents)
    return {"filename": file.filename , 'subject':subject}


@app.post("/post-text_notes/")
async def text_notes(textnotes : TextNotes ):

    # db.append(textnotes)
    content = f"Subject: {textnotes.subject}\n\nText: {textnotes.text}"
    print(content)
    # filename = f"{textnotes.subject}_{textnotes.text[:10]}.txt"
    # with open(filename, "w") as f:
    #     f.write()

    return {"filename": content, "subject": textnotes.subject, "text": textnotes.text}

@app.get("/get-notes/")
def get_notes():
    return db



# student_data = {1: {
#                 'name':'Bilal Haneef',
#                 'section':'A',
#                 'program':'SE-Evening',
#                 'age':23
#                }}

# class Student(BaseModel):
#     name : str
#     section : str
#     program : str
#     age : int

# @app.get('/')
# def index(name:str = None): # here we set the query paramter to None so that it is not required
#     if name == None:
#         return {'Welcome': 'Stranger!!!'} 
#     return {'Welcome': f'{name}'}

# # @app.get('/get-student_data/{student_id}')
# # def get_stu(student_id:int):
# #     return student_data[student_id]

# @app.get('/get-info/{student_id}')
# def info(student_id:int ,age:int):
#     if student_id in student_data:
#         if age == student_data[student_id]['age']:
#             return student_data[student_id]
#         return {'Message':'You entered wrong age information!'}
#     else:
#         return {'Error':'You have entered wrong id'}

# @app.post('/post-create_student/{student_id}')
# def create_student(student_id : int , student : Student ): 
#     # here student : Student , 'student' is a parameter and 'Student' is a basemodel class that we defined,
#     # it is kinda key value thing, now when this endpoint is called, it will ask user to fill the details
#     # defined in the Student class.
#     if student_id in student_data:
#         return {'Error':'Student alreay exist in the records'}
#     student = student.dict() # this will convert the student class variable object into dict
#     student_data[student_id] = student
#     return student_data[student_id]


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)






