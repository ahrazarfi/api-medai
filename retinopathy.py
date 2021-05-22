def translate_retinopathy(preds):
    y_proba_Class0 = preds.flatten().tolist()[0] * 100
    y_proba_Class1 = preds.flatten().tolist()[1] * 100
    y_proba_Class2 = preds.flatten().tolist()[2] * 100
    y_proba_Class3 = preds.flatten().tolist()[3] * 100

    mild = "Probability of the input image to have Mild Diabetic Retinopathy: {:.2f}%".format(
        y_proba_Class0
    )
    mod = "Probability of the input image to have Moderate Diabetic Retinopathy: {:.2f}%".format(
        y_proba_Class1
    )
    norm = "Probability of the input image to be Normal: {:.2f}%".format(y_proba_Class2)
    severe = "Probability of the input image to have Severe Diabetic Retinopathy: {:.2f}%".format(
        y_proba_Class3
    )

    total = [mild, mod, norm, severe]

    list_proba = [y_proba_Class0, y_proba_Class1, y_proba_Class2, y_proba_Class3]
    statements = [
        "Inference: The image has high evidence for Mild Nonproliferative Diabetic Retinopathy Disease.",
        "Inference: The image has high evidence for Moderate Nonproliferative Diabetic Retinopathy Disease.",
        "Inference: The image has no evidence for Nonproliferative Diabetic Retinopathy Disease.",
        "Inference: The image has high evidence for Severe Nonproliferative Diabetic Retinopathy Disease.",
    ]

    index = list_proba.index(max(list_proba))
    prediction = statements[index]

    return total, prediction
