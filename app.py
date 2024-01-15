import uvicorn
from fastapi import FastAPI , Path ,UploadFile ,File,Form
from typing import Optional
from pydantic import BaseModel
from image_text_to_model import text_to_model , pre_text_transformer,post_text_transformer

app = FastAPI()


class Notes(BaseModel):
    subject : str
    image : UploadFile

class TextNotes(BaseModel):
    subject : Optional[str]
    text : Optional[dict]

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
async def text_notes(textnotes : TextNotes):
    response = text_to_model(textnotes.subject , pre_text_transformer(textnotes.text))
    # return {'Subject':textnotes.subject , 'Data': textnotes.text}
    return post_text_transformer(response)

@app.get("/")
def get_notes():
    return 'Welcome! Boss'



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
