def translate_malaria(preds):
    y_proba_Class0 = preds.flatten().tolist()[0] * 100
    y_proba_Class1 = 100.0 - y_proba_Class0

    para_prob = "Probability of the cell image to be Parasitized: {:.2f}%".format(
        y_proba_Class1
    )
    unifected_prob = "Probability of the cell image to be Uninfected: {:.2f}%".format(
        y_proba_Class0
    )

    total = para_prob + " " + unifected_prob
    total = [para_prob, unifected_prob]

    if y_proba_Class1 > y_proba_Class0:
        prediction = "Inference: The cell image shows strong evidence of Malaria."
        return total, prediction
    else:
        prediction = "Inference: The cell image shows no evidence of Malaria."
        return total, prediction
