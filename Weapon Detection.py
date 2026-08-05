
import datetime
import cv2
import imutils

# 1. Load the classifier
gun_cascade = cv2.CascadeClassifier('gun_cascade.xml')

# Check if XML file loaded properly
if gun_cascade.empty():
    raise IOError(
        "Unable to load gun_cascade.xml. Ensure the file is in the script directory."
    )

# 2. Initialize video capture
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame from camera.")
        break

    # Resize frame and convert to grayscale for processing
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Note capital 'S' in minSize
    guns = gun_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100)
    )

    gun_exist = len(guns) > 0

    if gun_exist:
        print("Gun detected at", datetime.datetime.now())
        for x, y, w, h in guns:
            cv2.rectangle(
                frame, (x, y), (x + w, y + h), (0, 0, 255), 2
            )  # Red box
            cv2.putText(
                frame,
                "Gun Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                2,
            )
    else:
        print("No gun detected at", datetime.datetime.now())

    # Render frame ALWAYS (outside of detection check)
    cv2.imshow("Gun Detection", frame)

    # Press 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Clean up resources outside the main loop
camera.release()
cv2.destroyAllWindows()
       
