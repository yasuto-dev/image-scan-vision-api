import io
import cv2
from PIL import Image
from PIL import ImageGrab

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

def detect_text(path):
   """Detects text in the file."""
   with io.open(path, 'rb') as image_file:
       content = image_file.read()
   image = vision.Image(content=content)
   response = client.text_detection(image=image)
   texts = response.text_annotations
   string = ''
   for text in texts:
       string+=' ' + text.description
   return string
   
num = 1
cap = cv2.VideoCapture(0)
while(num):
   # Capture frame-by-frame
   ret, frame = cap.read()
   Height, Width = frame.shape[:2]
   img = cv2.resize(frame,(int(Width),int(Height)))

   file = 'live.png'
   cv2.imwrite( file,frame)
   # print OCR text
   text = detect_text(file)
   print(text)
   if "文字" in (text):
       
       cv2.imwrite("picture- "+ '{0:03d}'. format(num) + ".jpg" ,img)
       num += 1
 
   # Display the resulting frame
   cv2.imshow('OCRtest',frame)
   
   cv2.waitKey(1)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()