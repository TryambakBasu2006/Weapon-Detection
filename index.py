from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)
gun_cascade = cv2.CascadeClassifier('cascade.xml')

@app.route('/')
def home():
    return "Weapon Detection API is Running. Send a POST request to /api/detect with an image."

@app.route('/api/detect', methods=['POST'])
def detect_weapon():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
        
    file = request.files['image']
    filestr = file.read()
    
    # Convert string data to OpenCV image
    npimg = np.frombuffer(filestr, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    # Process image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    
    gun_detected = len(guns) > 0
    
    return jsonify({
        "gun_detected": gun_detected,
        "count": len(guns)
    })
