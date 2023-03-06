import pickle
import os
from datetime import datetime
def model():
    filename = '20230306-095951-speech_emotion_recognition_model.pkl'
    with open(filename, 'rb') as file:
        return pickle.load(file)