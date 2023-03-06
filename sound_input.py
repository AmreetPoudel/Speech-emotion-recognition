import pyaudio
import wave
import librosa
import numpy as np
import model
import feature_extraction

# Set the audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "recording.wav"

# Initialize the PyAudio object
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# Start recording
print("Recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording
print("Finished recording.")
stream.stop_stream()
stream.close()
audio.terminate()

# Save the audio data to a WAV file
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

print("Recording saved to {}".format(WAVE_OUTPUT_FILENAME))



model=model
song="recording.wav" 
from IPython.display import Audio, display
display(Audio(song, autoplay=True))
data, sample_rate = librosa.load(song, duration=2.5, offset=0.6)
mfcc=feature_extraction(data)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (-1,1))
mfcc = np.array(mfcc).reshape(-1 , 1)
mfcc =  scaler.fit_transform(mfcc)
mfcc = mfcc.reshape(1 , 123 ,1)
prediction =  model.predict(mfcc)
print(prediction.argmax())
for item in prediction:
  pass

emotions=["angry","disgust","surprise","happy","fear","neutral","sad","calm"]
emotionPrediction=zip(emotions,item)
for emotion,item in emotionPrediction:
  print(str(emotion)+":"+str(int(item*100))+"%")



