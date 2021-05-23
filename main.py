import boto3
import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image
from datetime import datetime as dt
import numpy as np
from PIL import Image
import os
import images_Handler
import config
import model_Loader
import prediction_Handler


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/{disease}")
def get_image(disease: str, file: UploadFile = File(...)):
    model = config.DISEASES[disease]
    input_Temp_Image = file.file
    processed_Image = images_Handler.images_Handler(model, input_Temp_Image)
    model_loaded = model_Loader.load_Model_From_Disk(model)[0]
    prediction = prediction_Handler.predict(model, model_loaded, processed_Image)
    return prediction

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)