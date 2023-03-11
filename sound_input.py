import pyaudio
import wave
import librosa
import numpy as np
import model as md
import feature_extraction 
# from IPython.display import Audio, display
from sklearn.preprocessing import MinMaxScaler


# Set the audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "amrit_happy.wav"

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



model=md.model()
song="amrit_happy.wav" 

# display(Audio(song, autoplay=True))
data, sample_rate = librosa.load(song, duration=2.5, offset=0.6)
mfcc=feature_extraction.feature_extraction(data,sample_rate)
scaler = MinMaxScaler(feature_range = (-1,1))
mfcc = np.array(mfcc).reshape(-1 , 1)
mfcc =  scaler.fit_transform(mfcc)
mfcc = mfcc.reshape(1 , 123 ,1)
prediction =  model.predict(mfcc)
print(prediction.argmax())
for item in prediction:
  pass

emotions=["surprise","sad","neutral","happy","fear","disgust","calm","angry"]
emotionPrediction=zip(emotions,item)
for emotion,item in emotionPrediction:
  print(str(emotion)+":"+str(int(item*100))+"%")



