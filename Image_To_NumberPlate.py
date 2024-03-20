import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
lic_data = cv2.CascadeClassifier("Datacluster_number_plates (101).xml")
cap = cv2.VideoCapture(0)
# number = lic_data.detectMultiScale(cap,1.2)

while (True):

    ret , frame = cap.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    number = lic_data.detectMultiScale(grey,1.2)

    for (x,y,w,h) in number:
        
        plate = frame[y:y+h,x:x+w]
        text = pytesseract.image_to_string(plate)

        if len(text) != 0:

            p = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)
            # print('---------------------------------------------------------------------------------------------------------------------------------------------')
            # print(p)
            # print('*********************************************************************************************************************************************')
            cv2.imwrite('.\images\\image1.jpg',frame)
            print(text)

    cv2.imshow('Image',frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
