from tensorflow.keras import callbacks
from tensorflow.keras.models import Sequential
<<<<<<< HEAD
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, BatchNormalization
from tensorflow.keras.layers import Rescaling, RandomFlip, RandomRotation, RandomZoom
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import Adam
=======
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model
>>>>>>> 437f011457ea58a29eeaeceeea626d8cfae2aa75
import pickle

DIR = "backend/model/data/CleanedData"
X = pickle.load(open(f"./{DIR}/X.pickle", 'rb'))
y = pickle.load(open(f"./{DIR}/y.pickle", 'rb'))

<<<<<<< HEAD

rescale = Sequential([Rescaling(1./255)])
data_augmentation = Sequential([
    RandomFlip("horizontal"),
    RandomRotation(0.1),
    RandomZoom(.2, .2)
])

model = Sequential([
    rescale,
    data_augmentation
    ]
)

model.add(Conv2D(32, (3, 3),
                 activation='relu',
                 input_shape=X.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(16, (3, 3),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
=======
X = X/255

model = Sequential()

model.add(Conv2D(16, (3, 3),
                 activation='relu',
                 input_shape=X.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
>>>>>>> 437f011457ea58a29eeaeceeea626d8cfae2aa75

model.add(Conv2D(16, (3, 3),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
<<<<<<< HEAD
model.add(Dense(10))
model.add(BatchNormalization())
model.add(Dense(7, activation='softmax'))
=======
model.add(Dense(3, activation='softmax'))
>>>>>>> 437f011457ea58a29eeaeceeea626d8cfae2aa75


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
<<<<<<< HEAD
          batch_size=24, epochs=100,
          validation_split=0.1,
          callbacks=callbacks)

plot_model(model, show_shapes=True, to_file="backend/model/model.png")
=======
          batch_size=32, epochs=25,
          validation_split=0.1,
          callbacks=callbacks)

plot_model(model, show_shapes=True, to_file="backend/model/model.png")
>>>>>>> 437f011457ea58a29eeaeceeea626d8cfae2aa75
