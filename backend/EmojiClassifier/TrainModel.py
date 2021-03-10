import numpy as np
from tensorflow.python.keras.callbacks import TensorBoard

from EmojiClassifier.DataGenerator import train_Generator, validation_Generator, convert_Image_To_Training_Data
from EmojiClassifier.config import *
from EmojiClassifier.Model import create_Model


def train_NN_Model():
    """ Trains the model with the train and validation generators and saves the weights in weights.h5 file """
    tensorBoardCallBack = TensorBoard(log_dir="./logs", histogram_freq=1)
    model = create_Model()
    trainGen = train_Generator()
    validationGen = validation_Generator()
    H = model.fit_generator(trainGen,
                            steps_per_epoch=NUM_TRAIN_SAMPLES // BATCH_SIZE,
                            validation_data=validationGen,
                            validation_steps=NUM_VAL_SAMPLES // BATCH_SIZE,
                            epochs=EPOCHS,
                            callbacks=[tensorBoardCallBack])
    model.save_weights("./weights.h5")


def test_NN_Model(path):
    """ Tests the model with a given path and returns the predicted emotion """
    model = create_Model()
    model.load_weights("./weights.h5")
    ar = convert_Image_To_Training_Data(path)
    y = model.predict(ar)
    y = np.argmax(y, axis=1)
    return emojiList[y]


if __name__ == "__main__":
    test_NN_Model("./Dataset/images/train/angry/1.jpg")
