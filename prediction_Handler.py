import keras.backend as K
from fastapi.encoders import jsonable_encoder
import retinopathy
import cardiac
import malaria


def predict(model, model_loaded, image_data):
    final_json = []
    if model == "dia":
        preds, pred_val = retinopathy.translate_retinopathy(
            model_loaded["model"].predict_proba(image_data)
        )
        final_json.append(
            {
                "empty": False,
                "type": model_loaded["type"],
                "mild": preds[0],
                "mod": preds[1],
                "norm": preds[2],
                "severe": preds[3],
                "pred_val": pred_val,
            }
        )
    elif model == "oct":
        preds, pred_val = cardiac.translate_oct(
            model_loaded["model"].predict(image_data)
        )
        final_json.append(
            {
                "empty": False,
                "type": model_loaded["type"],
                "cnv": preds[0],
                "dme": preds[1],
                "drusen": preds[2],
                "normal": preds[3],
                "pred_val": pred_val,
            }
        )

    elif model == "mal":
        preds, pred_val = malaria.translate_malaria(
            model_loaded["model"].predict_proba(image_data)
        )
        final_json.append(
            {
                "empty": False,
                "type": model_loaded["type"],
                "para": preds[0],
                "unin": preds[1],
                "pred_val": pred_val,
            }
        )

    else:
        warn = (
            "Feeding blank image won't work. Please enter an input image to continue."
        )
        pred_val = " "
        final_json.append(
            {
                "pred_val": warn,
                "para": " ",
                "unin": " ",
                "tumor": " ",
                "can": " ",
                "normal": " ",
                "bac": " ",
                "viral": " ",
                "cnv": " ",
                "dme": " ",
                "drusen": " ",
                "mild": " ",
                "mod": " ",
                "severe": " ",
                "norm": " ",
                "top1": " ",
                "top2": " ",
                "top3": " ",
                "top4": " ",
                "top5": " ",
            }
        )

    K.clear_session()
    result = jsonable_encoder(final_json[0])
    return result
