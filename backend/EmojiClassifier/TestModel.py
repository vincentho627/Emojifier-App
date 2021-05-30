from tensorflow.python.keras.models import load_model
import numpy as np
from tensorflow.python.ops.confusion_matrix import confusion_matrix

from EmojiClassifier.config import *
from EmojiClassifier.DataGenerator import convert_image_to_training_data, get_test_data_for_sklearn, \
    validation_generator


def get_emotion(path):
    """ Tests the model with a given path and returns the predicted emotion """
    model = load_model("Models/current.h5")
    ar = convert_image_to_training_data(path)
    y = model.predict(ar)
    y = int(np.argmax(y, axis=1))
    return emojiList[y]


def test_nn_model_with_validation():
    validation_gen = validation_generator(1)
    index = 0
    model = load_model("../Models/current.h5")

    y_predicts = []
    y_labels = []

    while index < NUM_VAL_SAMPLES:
        print(index)
        image_array, y_label_array = next(validation_gen)
        y_predict_array = model.predict(image_array)
        y_predict = int(np.argmax(y_predict_array, axis=1))
        y_label = int(np.argmax(y_label_array, axis=1))
        y_predicts.append(y_predict)
        y_labels.append(y_label)

        index += 1

    print(len(y_labels))
    print(len(y_predicts))
    conf_matrix = confusion_matrix(y_labels, y_predicts, num_classes=NUM_OUTPUTS)
    return conf_matrix


def test_sklearn_model():
    """ Tests with scikit learn models returns the predicted emotion """
    # TODO test the models with scikit learn and see which one has the best performance
    x_test, y_test = get_test_data_for_sklearn()
    return 0


if __name__ == "__main__":
    print(test_nn_model_with_validation())
