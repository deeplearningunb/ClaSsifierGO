import tensorflow as tf
import json
import io
import PIL
import base64
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask import request, Response
from tensorflow.keras.models import load_model


def index():
    return "Hello ClaSsifierGO!"


def image_processing():
    data = request.get_json()
    if 'image' not in data.keys():
        response = Response(
            status=400,
            mimetype='charge_viewlication/json'
        )
        return response

    data = data["image"].split(',')[1]
    with open('tmp.txt', 'w') as f:
        f.write(data)

    with open('tmp.txt', 'r') as f:
        data = f.read().strip()

    im = PIL.Image.open(io.BytesIO(base64.b64decode(data)))
    im.save('image.png', 'PNG')
    model = load_model_tmp()

    image = prepare('image.png')
    prediction = model.predict(image)

    print(prediction[0])
    result = {
        'predictions': [
            # {"name":"Dust2", "prediction": str(prediction[0][0])},
            {"name":"Inferno", "prediction": str(prediction[0][0])},
            {"name":"Mirage", "prediction": str(prediction[0][1])},
            # {"name":"Nuke", "prediction": str(prediction[0][2])},
            # {"name":"Overpass", "prediction": str(prediction[0][4])},
            {"name":"Train", "prediction": str(prediction[0][2])},
            {"name":"Vertigo", "prediction": str(prediction[0][3])},
        ],
        'winner': list(prediction[0]).index(max(prediction[0]))
    }
    response = Response(
        response=json.dumps(result),
        status=200,
        mimetype='charge_viewlication/json'
    )
    return response


def load_model_tmp():
    model = load_model("backend/model/model.h5")
    return model


def prepare(filepath):
    IMG_SIZE = 100
    img = load_img(filepath,
                   color_mode="rgb",
                   target_size=(IMG_SIZE, IMG_SIZE))
    img_array = img_to_array(img) / 255.0
    img_array = tf.expand_dims(img_array, 0)
    return img_array
