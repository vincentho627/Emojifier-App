from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from PIL import Image, ImageOps
import numpy as np

from EmojiClassifier.config import *


def train_Generator():
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

    return trainGen


def validation_Generator():
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

    return validationGen


def convert_Image_To_Training_Data(path):
    """ Converts a given image path into a grayscale image array for the neural network for input """
    img = Image.open(path).convert('LA')
    img = ImageOps.grayscale(img)
    ar = np.array(img)
    np.reshape(ar, (IMG_ROW, IMG_COL))
    ar = np.expand_dims(ar, axis=2)
    ar = np.expand_dims(ar, axis=0)
    print(ar.shape)
    return ar
