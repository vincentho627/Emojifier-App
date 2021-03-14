from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.python.keras.models import Sequential
from thinc.optimizers import Adam

from EmojiClassifier.config import INPUT_SHAPE, NUM_OUTPUTS


def create_model():
    """ Inspired by the VGGNet, removed its fifth Convolution block  """
    model = Sequential()

    # Block 1
    model.add(Conv2D(32, 3, activation="relu", kernel_initializer='he_normal', input_shape=INPUT_SHAPE, padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(32, 3, activation="relu", kernel_initializer='he_normal', input_shape=INPUT_SHAPE, padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 2
    model.add(Conv2D(64, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 3
    model.add(Conv2D(128, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 4
    model.add(Conv2D(256, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 5
    model.add(Conv2D(512, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(512, 3, kernel_initializer='he_normal', activation="relu", padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Dropout(0.2))

    # Block 6
    model.add(Flatten())
    model.add(Dense(128, kernel_initializer='he_normal', activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # Block 7
    model.add(Dense(64, kernel_initializer='he_normal', activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # Block 8
    model.add(Dense(NUM_OUTPUTS, activation="softmax"))

    adam = Adam(learning_rate=0.001)

    model.compile(optimizer=adam,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    print(model.summary())
    return model


def create_random_forest():
    return RandomForestClassifier(n_estimators=20, random_state=0)


def create_mlp_classifier():
    return MLPClassifier(activation="relu", hidden_layer_sizes=(256, 128, 64), solver="adam", batch_size=32,
                         verbose=True)


if __name__ == "__main__":
    m = create_model()




