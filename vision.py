import os,io
from google.cloud import vision
# from google.cloud.vision_v1 import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'propane-sphinx-411310-c77962b133eb.json'

client = vision.ImageAnnotatorClient()

with io.open('Handwritten Notes/1.jpg','rb') as img_file:
    content = img_file.read()

image = vision.Image(content = content)
 
response = client.document_text_detection(image = image)
print(response)





# def detect_text(path):
#     """Detects text in the file."""
#     from google.cloud import vision

#     client = vision.ImageAnnotatorClient()

#     with open(path, "rb") as image_file:
#         content = image_file.read()

#     image = vision.Image(content=content)

#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     print("Texts:")

#     for text in texts:
#         print(f'\n"{text.description}"')

#         vertices = [
#             f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
#         ]

#         print("bounds: {}".format(",".join(vertices)))

#     if response.error.message:
#         raise Exception(
#             "{}\nFor more info on error messages, check: "
#             "https://cloud.google.com/apis/design/errors".format(response.error.message)
#         )


# detect_text('Handwritten Notes/1.jpg')