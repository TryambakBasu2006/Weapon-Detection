import numpy as np
import cv2
import imutils
import datetime

# Load the cascade classifier
gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

# Variable initializations
first_frame = None

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame.")
        break
        
    # Reset detection state for the current frame
    gun_exist = False

    # Resize and convert to grayscale
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect guns
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    
    # Check if any guns were detected
    if len(gun) > 0:
        gun_exist = True
        
    # Draw bounding boxes
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Region of Interest (ROI) if you want to do further processing later
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
       
    # Initialize the first frame if needed (often used for motion detection background subtraction)
    if first_frame is None:
        first_frame = gray
        continue        
    
    # Display the results
    cv2.imshow("Security feed", frame)
    
    # Print status to the console
    if gun_exist:
        print("Guns detected!")
    else:
        print("No guns detected.")

    # Break loop on 'q' key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Clean up and close windows
camera.release()
cv2.destroyAllWindows()
   
