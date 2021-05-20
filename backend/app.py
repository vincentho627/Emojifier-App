from flask import Flask, request
import os

from EmojiClassifier.TestModel import get_emotion

template_path = os.path.abspath("../public")
app = Flask(__name__, template_folder=template_path)


@app.route("/get-emotion")
def retrieve_emotion():
    img = request.files.get('image')
    emotion = get_emotion(img)
    return {"emotion": emotion}


if __name__ == "__main__":
    app.run()
