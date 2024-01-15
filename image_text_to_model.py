import os
from openai import OpenAI
from constants import openai_key
os.environ['OPENAI_API_KEY'] = openai_key

client = OpenAI()


def text_to_model(subject , text_notes):
    '''Takes subject and text notes in terms of text and text & returns bullets and summary'''
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": '''You are a course notes summarizer. You get a subject and broken text in terms of notes that has been taken 
        in the class, you have to write the summary in format of quill.js delta , make sure that the response has proper headings and bullets.'''},
        {"role": "user", "content": f"Subject is '{subject}' and notes are '{text_notes}"}]
    )

    return completion.choices[0].message.content


print(text_to_model('DSA','-LinkedList , -queue , complexity , = tim sort'))