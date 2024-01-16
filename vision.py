from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time , json

credential = json.load(open('credentials.json'))

subscription_key = credential['API_KEY']
endpoint = credential['ENDPOINT']

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

file_path = '2.jpg'

with open(file_path, "rb") as image_stream:
    read_response = computervision_client.read_in_stream(image_stream,  raw=True)

read_operation_location = read_response.headers["Operation-Location"]
operation_id = read_operation_location.split("/")[-1]
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)






# from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
# from msrest.authentication import CognitiveServicesCredentials

# from array import array
# import os
# from PIL import Image
# import sys
# import time
# import json

# credential = json.load(open('credentials.json'))

# subscription_key = credential['API_KEY']
# endpoint = credential['ENDPOINT']

# computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# read_image_url = "https://static.skillshare.com/uploads/project/197455/cover_1242_c8db5284ea9adb59c864802834e32519.jpg"

# read_response = computervision_client.read(read_image_url,  raw=True)

# read_operation_location = read_response.headers["Operation-Location"]
# operation_id = read_operation_location.split("/")[-1]
# while True:
#     read_result = computervision_client.get_read_result(operation_id)
#     if read_result.status not in ['notStarted', 'running']:
#         break
#     time.sleep(1)

# if read_result.status == OperationStatusCodes.succeeded:
#     for text_result in read_result.analyze_result.read_results:
#         for line in text_result.lines:
#             print(line.text)
