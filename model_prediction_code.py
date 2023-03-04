#this code will take take song input and show resepective emotions  but feature extraction need to be defined 
# song="/content/drive/MyDrive/final year project/datas/CREME/1001_IEO_ANG_MD.wav"#neutral 
# song="/content/drive/MyDrive/final year project/datas/RAVDASS/Actor_24/03-01-04-02-02-01-24.wav" # pure sad cry
song="/content/drive/MyDrive/final year project/datas/emodv/16b01Eb.wav"
from IPython.display import Audio, display
display(Audio(song, autoplay=True))
data, sample_rate = librosa.load(song, duration=2.5, offset=0.6)
mfcc=feature_extraction(data)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (-1,1))
mfcc = np.array(mfcc).reshape(-1 , 1)
mfcc =  scaler.fit_transform(mfcc)
mfcc = mfcc.reshape(1 , 40 ,1)
prediction =  model.predict(mfcc)
# print(prediction.argmax())
# print(prediction)
for item in prediction:
  pass

emotions=["angry","disgust","surprise_or_calm","happy","fear","neutral","sad","calm_or_surprise"]
emotionPrediction=zip(emotions,item)
for emotion,item in emotionPrediction:
  print(str(emotion)+":"+str(int(item*100))+"%")

