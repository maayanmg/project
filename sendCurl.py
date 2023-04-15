import json
import requests

def send_curl(photo_path):
    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'image_file': open(photo_path, 'rb'),
    }

    response = requests.post('http://localhost:5000/pneumonia/predict', headers=headers, files=files)
    print(response.text)

    jRes = json.loads(response.text)
    print(jRes)
    return str(jRes['predicted_class'] + jRes['pneumonia_probability'])

if __name__ == '__main__':
    send_curl(r"D:\Projects\pneumonia-detection\fixtures\pneumonia_1.jpeg")