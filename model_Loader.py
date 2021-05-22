import config
from keras.models import load_model


def load_Model_From_Disk(model):
    model_name = []
    model_path = f"{config.MODEL_PATH}{model}.h5"
    model_name.append({"model": load_model(model_path), "type": model})
    return model_name
