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
st.title("Speech Emotion Recognition")

# Define the file uploader and emotion probabilities
uploaded_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"], key="file_uploader")

if uploaded_file is not None:
    st.subheader("Selected File")
    st.write(uploaded_file.name)

    # Initialize the PyAudio object
    audio = pyaudio.PyAudio()

    # Define a function to extract features from audio data
    @st.cache_data
    def extract_features(data, sample_rate):
        mfcc = feature_extraction.feature_extraction(data, sample_rate)
        scaler = MinMaxScaler(feature_range=(-1, 1))
        mfcc = np.array(mfcc).reshape(-1, 1)
        mfcc = scaler.fit_transform(mfcc)
        mfcc = mfcc.reshape(1, 123, 1)
        return mfcc

    # Define a function to predict the emotion from audio data
    @st.cache_data
    def predict_emotion(_model, mfcc):
        prediction = _model.predict(mfcc)
        emotions = ["surprise", "sad", "neutral", "happy", "fear", "disgust", "calm", "angry"]
                 
        emotion_prediction = dict(zip(emotions, prediction[0]))
        # Round off probabilities to 3 significant digits
        for emotion, probability in emotion_prediction.items():
            emotion_prediction[emotion] = round(probability, 3)
        return emotion_prediction

    # Save the audio data to a WAV file
    file_name = "uploaded_audio.wav"
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load the audio data and extract features
    data, sample_rate = librosa.load(file_name, duration=3, offset=0.6)
    mfcc = extract_features(data, sample_rate)

    # Predict the emotion
    model = md.model()
    emotion_prediction = predict_emotion(model, mfcc)

    # Play the audio file
    st.audio(file_name)

    # Create columns for left and right side
    left_column, right_column = st.columns(2)

    # Display the emotion with the highest probability on the left side
    max_emotion = max(emotion_prediction, key=emotion_prediction.get)
    max_emotion_prob = "{:.2f}".format(emotion_prediction[max_emotion]*100)
    left_column.subheader("Highest Probability")
    left_column.write(f"<p style='font-size:16pt'>The emotion in the sound is {max_emotion} ({max_emotion_prob}%)</p>", unsafe_allow_html=True)

    # Display the wave plot on the right side
    right_column.subheader("Wave Plot")
    fig, ax = plt.subplots()
    ax.plot(data)
    ax.set_title("Waveform")
    right_column.pyplot(fig)

    # Display the mel spectrogram, delta spectrogram, and double delta spectrogram in a 2x2 grid
    st.subheader("Mel Spectrogram, Delta Spectrogram, and Double Delta Spectrogram")
    mel_spectrogram = librosa.feature.melspectrogram(y=data, sr=sample_rate)
    delta_spectrogram = librosa.feature.delta(mel_spectrogram)
    double_delta_spectrogram = librosa.feature.delta(delta_spectrogram)

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    librosa.display.specshow(librosa.power_to_db(mel_spectrogram, ref=np.max), ax=axes[0, 0], x_axis='time', y_axis='mel')
    axes[0, 0].set_title('Mel Spectrogram')
    librosa.display.specshow(delta_spectrogram, ax=axes[0, 1], x_axis='time', y_axis='mel')
    axes[0, 1].set_title('Delta Spectrogram')
    librosa.display.specshow(double_delta_spectrogram, ax=axes[1, 0], x_axis='time', y_axis='mel')
    axes[1, 0].set_title('Double Delta Spectrogram')
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    st.pyplot(fig)

    # Display the Tonnetz and Chroma plots side by side
    st.subheader("Tonnetz and Chroma")
    y = librosa.effects.harmonic(data)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sample_rate)
    chroma = librosa.feature.chroma_stft(y=data, sr=sample_rate)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    img1 = librosa.display.specshow(tonnetz, x_axis='time', y_axis='tonnetz', cmap='coolwarm', ax=axes[0])
    fig.colorbar(img1, ax=axes[0])
    axes[0].set_title('Tonnetz')
    img2 = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', cmap='coolwarm', ax=axes[1])
    fig.colorbar(img2, ax=axes[1])
    axes[1].set_title('Chroma')
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    st.pyplot(fig)

    # Display the emotion probabilities as a pie chart with a blue background and simple animation
    st.subheader("Emotion Probabilities")
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(emotion_prediction.values(), labels=emotion_prediction.keys(), autopct='%1.3f%%', startangle=90, textprops={'fontsize': 10}, pctdistance=0.85)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['savefig.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.setp(autotexts, size=8, weight="bold", color="white")
    plt.setp(texts, size=8, weight="bold", color="black")
    for w in wedges:
        w.set_edgecolor('white')
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    fig.subplots_adjust(hspace=0.5)
    st.pyplot(fig)
else:
    emotion_prediction = {}
