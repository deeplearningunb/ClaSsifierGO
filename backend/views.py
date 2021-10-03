import tensorflow as tf
from flask import request, Response

def index():
    return "Hello Sudoku!"

def image_processing():
    data = request.get_json()
    if 'image' not in data.keys():
        response = Response(
                status=400,
                mimetype='charge_viewlication/json'
            )
        return response

    # model = load_model()
    # img = decode_img_bytes(data['image'])
    # result = model.predict(img)
    # response = Response(
    #         status=200,
    #         mimetype='charge_viewlication/json'
    #
    #     )

    return data['image']

def decode_img_bytes(img_b64: str) -> tf.Tensor:
        img = tf.io.decode_image(
            img_b64, 
            channels=3,
            dtype=tf.uint8,
            expand_animations=False
        )
        img = tf.image.resize(img, size=self.img_size)
        img = tf.ensure_shape(img, (*self.img_size, 3))
        img = tf.cast(img, tf.float32)
        return img

def load_model():
    # Load CNN model
    model = 1
    return model
