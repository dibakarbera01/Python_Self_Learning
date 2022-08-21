
import cv2
import numpy as np

# init camera
cap = cv2.VideoCapture(0)

# face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

skip = 0

while True:
    ret,frame = cap.read()

    if ret==False:
        continue

    cv2.imshow("Frame",frame)

    faces = face_cascade.detectMultiScale(frame,1.3,5)
    print(faces)

    # story every 1oth face
    if(skip%10==0):
        #store the 10th face later on
        pass
 
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()

    
