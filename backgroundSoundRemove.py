import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Set the duration and sample rate of the recording
duration = 5  # in seconds
sample_rate = 44100  # in Hz

# Record audio from the user
print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()
print("Recording finished!")

# Save the audio to a WAV file
file_name = "user_audio.wav"
sf.write(file_name, audio, sample_rate)
print(f"Audio saved to {file_name}")

# Load the audio file
audio_file = AudioSegment.from_wav(file_name)

# Define the silence threshold (in dB)
silence_threshold = -45

# Split the audio on silence
chunks = split_on_silence(audio_file, 
                          min_silence_len=500, 
                          silence_thresh=silence_threshold)

# Combine the non-silent chunks
clean_audio = chunks[0]
for i in range(1, len(chunks)):
    clean_audio += chunks[i]

# Save the clean audio
clean_file_name = "clean_audio.wav"
clean_audio.export(clean_file_name, format="wav")
print(f"Clean audio saved to {clean_file_name}")













# import os
# import glob
# import sounddevice as sd
# import soundfile as sf
# from pydub import AudioSegment
# from pydub.silence import split_on_silence

# # Set the duration and sample rate of the recording
# duration = 10  # in seconds
# sample_rate = 44100  # in Hz

# # Define the silence threshold (in dB)
# silence_threshold = -45

# # Define a function to clean an audio file
# def clean_audio(file_path):
#     # Load the audio file
#     audio_file = AudioSegment.from_file(file_path, format=file_path.split(".")[-1])

#     # Split the audio on silence
#     chunks = split_on_silence(audio_file, 
#                               min_silence_len=500, 
#                               silence_thresh=silence_threshold)

#     # Combine the non-silent chunks
#     clean_audio = chunks[0]
#     for i in range(1, len(chunks)):
#         clean_audio += chunks[i]

#     # Save the clean audio
#     clean_file_path = file_path.split(".")[0] + "_clean.wav"
#     clean_audio.export(clean_file_path, format="wav")
#     print(f"Clean audio saved to {clean_file_path}")

# # Record audio from the user
# print("Recording...")
# audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
# sd.wait()
# print("Recording finished!")

# # Save the audio to a WAV file
# file_name = "user_audio.wav"
# sf.write(file_name, audio, sample_rate)
# print(f"Audio saved to {file_name}")

# # Clean the recorded audio
# print("Cleaning recorded audio...")
# clean_audio(file_name)

# # Define the directory containing the audio files
# audio_dir = "/path/to/audio/directory"

# # Clean all the audio files in the directory
# for file_path in glob.glob(os.path.join(audio_dir, "*.wav")):
#     print(f"Cleaning {file_path}...")
#     clean_audio(file_path)
