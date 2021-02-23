from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.python.keras.losses import SparseCategoricalCrossentropy
from tensorflow.python.keras.models import Sequential
from EmojiClassifier.config import INPUT_SHAPE
from sklearn.ensemble import RandomForestClassifier


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





