import pandas as pd
import numpy as np
from PIL import Image, ImageOps
from tensorflow.python.keras.utils.np_utils import to_categorical

from EmojiClassifier.config import PATH_TO_DATA_CSV, PATH_TO_IMAGES, EMOJI_DICT


def get_image_features(img_given):
    """ Converting a given image into grayscale and turn it into (66564,) flattened numpy array for training """
    path = PATH_TO_IMAGES + "/{}".format(img_given)
    img = Image.open(path)
    img = ImageOps.grayscale(img)
    img = img.resize((258, 258))
    img = np.asarray(img)

    # normalize the image into the range [0, 1]
    img = img / 255
    assert (258, 258) == img.shape

    # specify that there is only 1 color channel since its grayscale
    img = img.reshape(258, 258, 1)
    return img


def get_expected_emotion_array(emotion_given):
    """ Translates the given emotion into a numpy array where its corresponding index in the array will be 1,
    rest is 0 """
    length = len(EMOJI_DICT.keys())
    return to_categorical(EMOJI_DICT[emotion_given], length)


def data_generator():
    """ Generator that gives training data for next image array and next emotion array """
    df = pd.read_csv(PATH_TO_DATA_CSV)
    for i in df.index:
        image = df['image'][i]
        emotion = df['emotion'][i]
        image_array = get_image_features(image)
        emotion_array = get_expected_emotion_array(emotion)
        yield image_array, emotion_array


if __name__ == "__main__":
    print(next(data_generator()))
