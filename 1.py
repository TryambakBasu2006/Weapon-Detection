import requests

url = "https://your-deployed-app-url.com/api/detect"
image_path = "test_image.jpg"

with open(image_path, "rb") as img:
    response = requests.post(url, files={"image": img})
    
print(response.json())