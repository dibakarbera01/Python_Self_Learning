import cv2
from matplotlib.pyplot import gray
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:

    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)

  
    

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow("Video Frame",frame)

    key_pressed = cv2.waitKey(20) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()