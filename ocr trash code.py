# # import pytesseract
# # import cv2

# # # Set the path to the Tesseract executable (replace this with your path)
# # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# # img = cv2.imread('E:/Git Repos/FYP-II/3.jpg')

# # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # print(pytesseract.image_to_string(img))

# # # cv2.imshow('Result', img)
# # # cv2.waitKey(0)
# # # raise TesseractError(proc.returncode, get_errors(error_string))
# # # pytesseract.pytesseract.TesseractError: (1, 'Error opening data file C:\\Users\\Muhammad Bilal\\AppData\\Local\\Tesseract-OCR\\eng.traineddata Please make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory. Failed loading language \'eng\' Tesseract 
# # # couldn\'t load any languages! Could not initialize tesseract.')
# # import easyocr
# # import cv2

# # # Replace 'en' with the language code of the text in your image (e.g., 'en', 'es', 'fr', etc.)
# # reader = easyocr.Reader(['en'])

# # l = []
# # def run_ocr(image_path):
# #     # Read the image using OpenCV
# #     img = cv2.imread(image_path)

# #     # Convert the image from BGR to RGB
# #     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# #     # Run EasyOCR on the image
# #     results = reader.readtext(img_rgb)

# #     # Print the results
# #     for (bbox, text, prob) in results:
# #         # print(f"Text: {text}, Confidence: {prob:.2f}")
# #         l.append(text)
# #     print(l)
# # # Replace 'path/to/your/image.jpg' with the path to your image file
# # image_path = '2.jpg'
# # run_ocr(image_path)

import keras_ocr
import cv2


def run_keras_ocr(image_path):
    l = []
    # Load the detector and recognizer models
    pipeline = keras_ocr.pipeline.Pipeline()

    # Read the image using matplotlib
    # image = keras_ocr.tools.read(image_path)
    # print(type(image),image.shape)
    # Get predictions
    predictions = pipeline.recognize([image_path])

    # Print the detected text
    for text_result in predictions[0]:
        # confidence = float(text_result[1])  # Convert to float
        # print(f"Text: {text_result[0]}, Confidence: {confidence:.2f}")
        # print(text_result[0])   
        l.append(text_result[0])
        print(l)

# Replace 'path/to/your/image.jpg' with the path to your image file
image_path = '1_new.jpg'
run_keras_ocr(image_path)


# import cv2

# img = cv2.imread('1.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# img = cv2.erode(img, None, iterations=1)
# cv2.imwrite('1_new.jpg', img)
# cv2.imshow('Result', img)

# cv2.waitKey(0)
