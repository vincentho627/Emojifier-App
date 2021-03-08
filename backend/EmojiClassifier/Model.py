import datetime
from tensorflow.python.keras.callbacks import TensorBoard
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.python.keras.losses import SparseCategoricalCrossentropy
from tensorflow.python.keras.models import Sequential
from EmojiClassifier.config import INPUT_SHAPE
from sklearn.ensemble import RandomForestClassifier

# use this when fitting the data onto the tf model so that can visualise the loss, accuracy graphs and NN model struct
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
callback = TensorBoard(log_dir=log_dir, histogram_freq=1)


def create_Model():
    model = Sequential()
    model.add(Conv2D(2, 3, activation="relu", input_shape=INPUT_SHAPE))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(2, 3, activation="relu", input_shape=INPUT_SHAPE))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(2, 3, activation="relu", input_shape=INPUT_SHAPE))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10))

    model.compile(optimizer='adam',
                  loss=SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return model

# def random_Forest():





