from tensorflow.python.keras.models import load_model
import numpy as np

from EmojiClassifier.config import *
from EmojiClassifier.DataGenerator import convert_image_to_training_data, get_test_data_for_sklearn


def test_nn_model(path):
    """ Tests the model with a given path and returns the predicted emotion """
    model = load_model("./test.h5")
    ar = convert_image_to_training_data(path)
    y = model.predict(ar)
    y = int(np.argmax(y, axis=1))
    return emojiList[y]


def test_sklearn_model():
    """ Tests with scikit learn models returns the predicted emotion """
    # TODO test the models with scikit learn and see which one has the best performance
    x_test, y_test = get_test_data_for_sklearn()
    return 0


if __name__ == "__main__":
    print(test_nn_model("./Dataset/images/train/happy/32.jpg"))
