import base64
import cv2
from PIL import Image
from flask import Flask, request
import os
import pandas as pd
import matplotlib.pyplot as plt
import io
import numpy as np


from EmojiClassifier.TestModel import get_emotion
from EmojiExtractor.EmojiExtractor import get_image_from_emotion
from FaceDetection.FaceDetector import detect_Faces


template_path = os.path.abspath("../public")
app = Flask(__name__, template_folder=template_path)


@app.route("/image", methods=["POST"])
def retrieve_emotion():
    if request.method == "POST":

        resp = request.get_json()
        img_data = resp['image']

        byte_data = bytes(img_data, 'utf-8')

        b = base64.b64decode(byte_data)

        jpg_as_np = np.frombuffer(b, dtype=np.uint8)
        img = cv2.imdecode(jpg_as_np, flags=1)
        # img = Image.open(io.BytesIO(b))

        detect_Faces(img)

        faces_to_emoji = {}
        for root, dirs, files in os.walk("./FaceDetection/Images"):
            for filename in files:
                emotion = get_emotion("./FaceDetection/Images/" + filename)
                filename = int(filename.replace(".jpg", ""))
                faces_to_emoji[filename] = emotion

        df = pd.read_csv("./FaceDetection/Dataset/faces.csv")

        for index, row in df.iterrows():
            x = row['x']
            y = row['y']
            h = row['height']
            w = row['width']
            emotion = faces_to_emoji[index]
            emoji = get_image_from_emotion(f"./EmojiExtractor/Images/{emotion}.png", h, w)
            for c in range(3):
                alpha_s = emoji[:, :, 2] / 255.0
                alpha_l = 1.0 - alpha_s
                img[y:y + h, x:x + w, c] = (alpha_s * emoji[:, :, c] + alpha_l * img[y:y + h, x:x + w, c])

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_save = Image.fromarray(img)
        b = io.BytesIO()
        img_save.save(b, format="jpeg")
        b.seek(0)

        labelled_image = base64.b64encode(b.read()).decode('ascii')

        return {"image": labelled_image}


@app.route("/testing")
def testing():
    return {"success": True}


if __name__ == "__main__":
    app.run(debug=True)
