    # # Display the emotion with the highest probability
    # max_emotion = max(emotion_prediction, key=emotion_prediction.get)
    # st.subheader("Emotion Prediction")
    # st.write(f"The predicted emotion is **{max_emotion}** with a probability of **{emotion_prediction[max_emotion]:.2%}**.")




import streamlit as st
import pyaudio
import wave
import librosa
import numpy as np
import model as md
import feature_extraction
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Define the Streamlit app
st.set_page_config(page_title="Emotion Detection", page_icon=":microphone:", layout="wide")
st.title("Emotion Detection using Speech")

# Define the file uploader and emotion probabilities pie chart
file_col, prob_col = st.columns(2)
uploaded_file = file_col.file_uploader("Upload Audio File", type=["wav", "mp3"], key="file_uploader")
if uploaded_file is not None:
    with file_col:
        st.subheader("Selected File")
        st.write(uploaded_file.name)

emotion_prediction = None
with prob_col:
    st.subheader("Emotion Probabilities")
    if emotion_prediction is not None:
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(emotion_prediction.values(), labels=emotion_prediction.keys(), autopct='%1.1f%%')
        ax.set_title("Emotion Probabilities", fontsize=18)
        ax.axis('equal')
        st.pyplot(fig)

# Initialize the PyAudio object
audio = pyaudio.PyAudio()

# Define a function to extract features from audio data
@st.cache_data
def extract_features(data, sample_rate):
    mfcc = feature_extraction.feature_extraction(data, sample_rate)
    scaler = MinMaxScaler(feature_range = (-1,1))
    mfcc = np.array(mfcc).reshape(-1 , 1)
    mfcc = scaler.fit_transform(mfcc)
    mfcc = mfcc.reshape(1, 123, 1)
    return mfcc

# Define a function to predict the emotion from audio data
@st.cache_data
def predict_emotion(_model, mfcc):
    prediction = _model.predict(mfcc)
    emotions = ["surprise", "sad", "neutral", "happy", "fear", "disgust", "calm", "angry"]
    emotion_prediction = dict(zip(emotions, prediction[0]))
    return emotion_prediction

# Define a function to plot the emotion probabilities as a pie chart
@st.cache_data
def plot_emotion_probabilities(emotion_prediction):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(emotion_prediction.values(), labels=emotion_prediction.keys(), autopct='%1.1f%%')
    ax.set_title("Emotion Probabilities", fontsize=18)
    ax.axis('equal')
    return fig

# If the user has uploaded a file, extract and predict the emotion
if uploaded_file is not None:
    # Save the audio data to a WAV file
    file_name = "uploaded_audio.wav"
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load the audio data and extract features
    data, sample_rate = librosa.load(file_name, duration=2.5, offset=0.6)
    mfcc = extract_features(data, sample_rate)

    # Predict the emotion
    model = md.model()
    emotion_prediction = predict_emotion(model, mfcc)

    # Display the emotion with the highest probability
    max_emotion = max(emotion_prediction, key=emotion_prediction.get)
    st.subheader("Emotion Prediction")
    st.write(f"The predicted emotion is **{max_emotion}** with a probability of **{emotion_prediction[max_emotion]:.2%}**.")
    