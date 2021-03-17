import cv2
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import numpy as np

from EmojiClassifier.config import *


def train_generator(batch_size):
    """ Returns shuffled training generator that outputs the grayscale image array with the categorical emoji array """
    train_data = ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=10,
        shear_range=0.3,
        zoom_range=0.1,
        width_shift_range=0.4,
        height_shift_range=0.4,
        horizontal_flip=True,
        fill_mode='nearest')

    train_gen = train_data.flow_from_directory(
        PATH_TO_TRAIN,
        color_mode='grayscale',
        target_size=(IMG_ROW, IMG_COL),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True)

    # TODO testing for convert image to training data, ensure that the output has shape (32, 48, 48, 1) and (5,)
    return train_gen


def validation_generator(batch_size=BATCH_SIZE):
    """ Returns shuffled validation generator that outputs the grayscale image array with the categorical emoji array
    """
    validation_data = ImageDataGenerator(rescale=1. / 255)

    validation_gen = validation_data.flow_from_directory(
        PATH_TO_VAL,
        color_mode='grayscale',
        target_size=(IMG_ROW, IMG_COL),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True)

    # TODO testing for convert image to training data, ensure that the output has shape (32, 48, 48, 1) and (5,)
    return validation_gen


def get_train_data_for_sklearn():
    index = 0
    x_train = []
    y_train = []
    train_gen = train_generator(1)

    while index < NUM_TRAIN_SAMPLES:
        print(index)
        curr_x, curr_y = next(train_gen)
        curr_x = curr_x.reshape((IMG_ROW * IMG_COL))
        curr_y = curr_y.reshape((NUM_OUTPUTS, ))
        x_train.append(curr_x)
        y_train.append(curr_y)
        index += 1

    return x_train, y_train


def get_test_data_for_sklearn():
    index = 0
    x_test = []
    y_test = []
    train_gen = validation_generator()

    while index < NUM_TRAIN_SAMPLES:
        print(index)
        curr_x, curr_y = next(train_gen)
        curr_x = curr_x.reshape((IMG_ROW * IMG_COL))
        curr_y = curr_y.reshape((NUM_OUTPUTS, ))
        x_test.append(curr_x)
        y_test.append(curr_y)
        index += 1

    return x_test, y_test


def convert_image_to_training_data(path):
    """ Converts a given image path into a grayscale image array for the neural network for input """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_ROW, IMG_COL), interpolation=cv2.INTER_CUBIC)
    ar = np.expand_dims(img, axis=2)
    ar = np.expand_dims(ar, axis=0)
    # TODO testing for convert image to training data, ensure that the output has shape (1, 48, 48, 1)
    return ar


if __name__ == "__main__":
    x, y = get_train_data_for_sklearn()
