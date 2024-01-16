import uvicorn
from fastapi import FastAPI , Path ,UploadFile ,File,Form
from pydantic import BaseModel
from typing import Optional
from image_text_to_model import text_to_model , pre_text_transformer,post_text_transformer
from vision import read_text_from_image

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
    with open(f'Saved Notes/{file.filename}', "wb") as f:
        f.write(contents)
    response = read_text_from_image(f'Saved Notes/{file.filename}')
    response = text_to_model(subject , pre_text_transformer({
    "ops": [
        {
            "insert": f"{response}",
            "attributes": {
                "color": "#bdc1c6"
            }
        }
    ]
}))
    return post_text_transformer(response)


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
