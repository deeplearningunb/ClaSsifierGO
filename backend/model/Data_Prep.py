import os
import random
import pickle
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img

LABELS = ["Inferno", "Mirage", "Nuke"]
DIR = "backend/model/data/Mapas"

def image_prep(dir, labels, size=(100, 100)):
    data = []
    for number in labels:
        path = f"./{dir}/{number}"
        index = labels.index(number)

        for image_name in os.listdir(path):
            img_path = f'{path}/{image_name}'
            img_loaded = load_img(img_path, color_mode="rgb",
                                  target_size=size)
            img_arr = img_to_array(img_loaded)
            data.append([img_arr, index])
    return data


data = image_prep(DIR, LABELS)

print("="*100)
random.seed(2021)
random.shuffle(data)


def sep_Xy(data):
    X = []
    y = []
    for feature, label in data:
        X.append(feature)
        y.append(label)
    X = np.array(X)
    y = np.array(y)
    return (X, y)


X, y = sep_Xy(data)


def pickle_np_save(data, name):
    pickle_out = open(f'./backend/model/data/CleanedData/{name}.pickle', 'wb')
    pickle.dump(data, pickle_out)
    pickle_out.close()


pickle_np_save(X, 'X')
pickle_np_save(y, 'y')

