import numpy as np
from tensorflow.python.keras.callbacks import TensorBoard, EarlyStopping
from tensorflow.python.keras.models import load_model
import matplotlib.pyplot as plt

from EmojiClassifier.DataGenerator import train_generator, validation_generator, convert_image_to_training_data, \
    get_test_data_for_sklearn
from EmojiClassifier.config import *
from EmojiClassifier.Model import create_model


def train_nn_model():
    """ Trains the model with the train and validation generators and saves the weights in weights.h5 file """
    tensor_board_call_back = TensorBoard(log_dir="./logs", histogram_freq=1)
    early_stopping_call_back = EarlyStopping(monitor='val_loss',
                                             min_delta=0.01,
                                             patience=3,
                                             verbose=1,
                                             restore_best_weights=True
                                             )
    callbacks = [tensor_board_call_back, early_stopping_call_back]
    model = create_model()
    train_gen = train_generator(BATCH_SIZE)
    validation_gen = validation_generator()
    history = model.fit_generator(train_gen,
                                  steps_per_epoch=NUM_TRAIN_SAMPLES // BATCH_SIZE,
                                  validation_data=validation_gen,
                                  validation_steps=NUM_VAL_SAMPLES // BATCH_SIZE,
                                  epochs=EPOCHS,
                                  callbacks=callbacks)
    model.save("./current.h5")

    # plotting graph to visualise accuracy
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')
    plt.show()


def train_sklearn_models():
    """ Trains scikit learn models to see which model does best """
    # TODO make and train with scikit learn and see which one has the best performance
    x_train, y_train = get_test_data_for_sklearn()
    return 0


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
    # train_NN_Model()
    print(test_nn_model("./Dataset/images/train/happy/32.jpg"))
