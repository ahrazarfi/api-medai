def translate_oct(preds):
    y_proba_Class0 = preds.flatten().tolist()[0] * 100
    y_proba_Class1 = preds.flatten().tolist()[1] * 100
    y_proba_Class2 = preds.flatten().tolist()[2] * 100
    y_proba_Class3 = preds.flatten().tolist()[3] * 100

    cnv = "Probability of the input image to have Hyperdynamic Circulation: {:.2f}%".format(
        y_proba_Class0
    )
    dme = "Probability of the input image to have Normal Ejection Fraction: {:.2f}%".format(
        y_proba_Class1
    )
    drusen = "Probability of the input image to have Moderate Ejection Fraction: {:.2f}%".format(
        y_proba_Class2
    )
    normal = "Probability of the input image to have Severe Ejection Fraction: {:.2f}%".format(
        y_proba_Class3
    )

    total = [cnv, dme, drusen, normal]

    list_proba = [y_proba_Class0, y_proba_Class1, y_proba_Class2, y_proba_Class3]
    statements = [
        "Inference: The image has high evidence of Hyperdynamic circular.",
        "Inference: The image has high evidence of Normal Ejection Fraction.",
        "Inference: The image has high evidence of Mild Ejection Fraction .",
        "Inference: The image has high evidence of Moderate Ejection Fraction.",
    ]

    index = list_proba.index(max(list_proba))
    prediction = statements[index]

    return total, prediction
