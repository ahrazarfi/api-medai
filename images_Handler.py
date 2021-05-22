from PIL import Image
import numpy as np
import imageio
import cv2
from keras.preprocessing import image
from cv2 import resize, cvtColor, COLOR_GRAY2RGB


def images_Handler(model, tempImage):
    final_json = []  # empty array to store the final prediction
    if model == "dia":
        test_image = Image.open(tempImage)
        test_image = test_image.resize((128, 128), Image.ANTIALIAS)
        test_image = np.array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)
        data = test_image

    elif model == "oct":
        test_image = imageio.imread(tempImage)
        test_image = resize_image_oct(test_image)
        test_image = np.array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)
        data = test_image

    elif model == "mal":
        test_image = Image.open(tempImage)
        test_image = test_image.resize((128, 128))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)
        data = test_image
    return data


def resize_image_oct(image):
    resized_image = cv2.resize(image, (128, 128))
    if len(resized_image.shape) != 3:
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    return resized_image
