import librosa
import numpy as np 

def feature_extraction(data,sample_rate):
  mfccs=np.mean(librosa.feature.mfcc(y=data,n_mfcc=35,sr=sample_rate).T,axis=0)
  delta=librosa.feature.delta(mfccs)
  delta2=librosa.feature.delta(mfccs,order=2)
  tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(data), sr=sample_rate).T,axis=0)
  chroma = librosa.feature.chroma_stft(y=data, sr=sample_rate)
  mean_chroma=[]
  for item in chroma:
    mean_chroma.append(np.mean(item))
  final_mfccs=np.concatenate((mfccs,delta,delta2,mean_chroma,tonnetz))
  return final_mfccs