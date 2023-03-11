import pickle
import os
from tensorflow import keras
from datetime import datetime
def model():
    path="h5Model.h5"
    model = keras.models.load_model(path)
    return model

    # filename = 'speech_emotion_recognition_model.pkl'
    # with open(filename, 'rb') as file:
    #     model = pickle.load(file)
    #     return model
    