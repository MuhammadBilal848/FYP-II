import os
from openai import OpenAI
from constants import openai_key
os.environ['OPENAI_API_KEY'] = openai_key

client = OpenAI()


def text_transformer(dic : dict):
    b = ''
    for a in range(0,len(dic['ops'])):
        b += dic['ops'][a]['insert']
    return b.replace('\n',' ')


def text_to_model(subject , text_notes):
    '''Takes subject and text notes in terms of text and text & returns bullets and summary'''
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": '''You are a course notes summarizer. You get a subject and broken text in terms of notes that has been
          taken in the class, you have to write numbered bullets by reading the text and in the end summarize all the numbered bullets in a small paragraph.'''},
        {"role": "user", "content": f"Subject is '{subject}' and notes are '{text_notes}"}]
    )

    return completion.choices[0].message.content


# print(text_to_model('DSA','-LinkedList , -queue , complexity , = tim sort'))

# print(text_transformer({
#             "ops": [
#                 {
#                     "insert": "Data science is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processes, algorithms and systems to extract or extrapolate knowledge and insights from potentially noisy, structured, or unstructured data.",
#                     "attributes": {
#                         "color": "#bdc1c6"
#                     }
#                 },
#                 {
#                     "insert": "\n\n"
#                 },
#                 {
#                     "insert": "dadada bilalda dadad AAAAAAAAAAAAAAAAAAAAA.",
#                     "attributes": {
#                         "background": "#202124",
#                         "color": "#bdc1c6"
#                     }
#                 },
#                 {
#                     "insert": "\n"
#                 }
#             ]
#         })
# )
