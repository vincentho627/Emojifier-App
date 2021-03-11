from sklearn import metrics
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.callbacks import TensorBoard, EarlyStopping
import matplotlib.pyplot as plt
import numpy as np

from EmojiClassifier.DataGenerator import train_generator, validation_generator, get_train_data_for_sklearn
from EmojiClassifier.config import *
from EmojiClassifier.Model import create_model, create_random_forest, create_mlp_classifier


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

    models = [create_random_forest, create_mlp_classifier]
    modelNames = ["Random Forest", "MLP Classifier"]

    x_train, y_train = get_train_data_for_sklearn()
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, random_state=3, test_size=0.2, )

    for i in range(len(models)):
        name = modelNames[i]
        print(f'Training {name}')
        model = models[i]()
        model.fit(x_train, y_train)
        y_val_predict = model.predict(x_val)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_val, y_val_predict))
        print('Mean Squared Error:', metrics.mean_squared_error(y_val, y_val_predict))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_val, y_val_predict)))


if __name__ == "__main__":
    # train_NN_Model()
    train_sklearn_models()
