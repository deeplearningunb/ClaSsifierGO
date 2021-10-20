from tensorflow.keras import callbacks
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model
import pickle

DIR = "backend/model/data/CleanedData"
X = pickle.load(open(f"./{DIR}/X.pickle", 'rb'))
y = pickle.load(open(f"./{DIR}/y.pickle", 'rb'))

X = X/255

model = Sequential()

model.add(Conv2D(16, (3, 3),
                 activation='relu',
                 input_shape=X.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(16, (3, 3),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(3, activation='softmax'))


model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])


callbacks = [
    ModelCheckpoint(
        filepath="backend/model/model.h5",
        monitor="val_loss",
        save_best_only=True)
]

model.fit(X, y,
          batch_size=32, epochs=25,
          validation_split=0.1,
          callbacks=callbacks)

plot_model(model, show_shapes=True, to_file="backend/model/model.png")