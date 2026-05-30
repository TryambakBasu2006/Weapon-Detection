import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)
first_frame = None

while True:
    ret, frame = camera.read()
    if not ret:
        break
        
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Fixed typo
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    
    gun_exist = False # Reset state every frame
    if len(gun) > 0: # Added missing colon
        gun_exist = True
        
    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
       
    if first_frame is None:
        first_frame = gray
        continue        
    
    cv2.imshow("Security feed", frame)
    
    if gun_exist:
        print("guns detected")
    else:
        print("guns not detected")

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows() # Added missing parentheses
   
