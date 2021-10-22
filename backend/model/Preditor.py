from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import tensorflow as tf


def prepare(filepath):
    IMG_SIZE = 100
    img = load_img(filepath,
                   color_mode="rgb",
                   target_size=(IMG_SIZE, IMG_SIZE))
    img_array = img_to_array(img) / 255.0
    img_array = tf.expand_dims(img_array, 0)
    return img_array


model = load_model("backend/model/model.h5")

imagem = prepare("backend/model/data/Nuke_val.png")
prediction = model.predict(imagem)

print(prediction)