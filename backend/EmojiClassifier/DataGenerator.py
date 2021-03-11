import cv2
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import numpy as np

from EmojiClassifier.config import *


def train_generator():
    """ Returns shuffled training generator that outputs the grayscale image array with the categorical emoji array """
    trainData = ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=10,
        shear_range=0.3,
        zoom_range=0.1,
        width_shift_range=0.4,
        height_shift_range=0.4,
        horizontal_flip=True,
        fill_mode='nearest')

    trainGen = trainData.flow_from_directory(
        PATH_TO_TRAIN,
        color_mode='grayscale',
        target_size=(IMG_ROW, IMG_COL),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=True)

    # TODO testing for convert image to training data, ensure that the output has shape (32, 48, 48, 1) and (5,)
    return trainGen


def validation_generator():
    """ Returns shuffled validation generator that outputs the grayscale image array with the categorical emoji array
    """
    validationData = ImageDataGenerator(rescale=1. / 255)

    validationGen = validationData.flow_from_directory(
        PATH_TO_VAL,
        color_mode='grayscale',
        target_size=(IMG_ROW, IMG_COL),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=True)

    # TODO testing for convert image to training data, ensure that the output has shape (32, 48, 48, 1) and (5,)
    return validationGen


def convert_image_to_training_data(path):
    """ Converts a given image path into a grayscale image array for the neural network for input """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_ROW, IMG_COL), interpolation=cv2.INTER_CUBIC)
    ar = np.expand_dims(img, axis=2)
    ar = np.expand_dims(ar, axis=0)
    # TODO testing for convert image to training data, ensure that the output has shape (1, 48, 48, 1)
    return ar


if __name__ == "__main__":
    l1, l2 = next(train_generator())
    labels = train_generator().class_indices
    labels = dict((v, k) for k, v in labels.items())
    print(labels)
    print(l2[0].shape)
