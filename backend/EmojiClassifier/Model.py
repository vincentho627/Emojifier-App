from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.python.keras.models import Sequential
from EmojiClassifier.config import INPUT_SHAPE


def create_Model():
    """ Inspired by the VGGNet, removed its fifth Convolution block  """
    model = Sequential()

    # Block 1
    model.add(Conv2D(32, 3, activation="relu", input_shape=INPUT_SHAPE, padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(32, 3, activation="relu", input_shape=INPUT_SHAPE, padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 2
    model.add(Conv2D(64, 3, activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, 3, activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 3
    model.add(Conv2D(128, 3, activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, 3, activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 4
    model.add(Conv2D(256, 3, activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, 3, activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 5
    model.add(Flatten())
    model.add(Dense(64, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # Block 6
    model.add(Dense(64, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # Block 7
    model.add(Dense(7, activation="softmax"))

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    print(model.summary())
    return model


if __name__ == "__main__":
    m = create_Model()




