#shutil is used to move songs to their respective folders with emotion
import shutil

import os
import glob

requiredfolders=[]
pathdir = "."
folders=os.listdir()
for folder in folders:
    if os.path.isdir(folder):   
        requiredfolders.append(folder)

#now we will iterate through all the folders and all audio files and all the audios will be moved
#to specific folder i.e all same emotions will be moved to same folder
emotions=['neutral','calm','happy','sad','angry','fearful','disgust','surprised']
for emotion in emotions:
    os.mkdir(emotion)

for folder in requiredfolders:
    #list of all the songs in a folder
    # mp3_filenames_list = glob.glob(os.path.join(folder, "*.mp3"))
    # print(mp3_filenames_list)
    audios=os.listdir(os.path.join(pathdir,folder))
    songs=[]
    for audio in audios:
        if audio.endswith('.wav'):
            songs.append(audio)

            
    # print(songs)
    
    for song in songs:
        print(1)
        
        if song[6:8]=="01":
            destinationfolder=os.path.join(pathdir,emotions[0])
            
        elif song[6:8]=="02":
            destinationfolder=os.path.join(pathdir,emotions[1])

        elif song[6:8]=="03":
            destinationfolder=os.path.join(pathdir,emotions[2])

        elif song[6:8]=="04":
            destinationfolder=os.path.join(pathdir,emotions[3])

        elif song[6:8]=="05":
            destinationfolder=os.path.join(pathdir,emotions[4])

        elif song[6:8]=="06":
            destinationfolder=os.path.join(pathdir,emotions[5])

        elif song[6:8]=="07":
            destinationfolder=os.path.join(pathdir,emotions[6])

        elif song[6:8]=="08":
            destinationfolder=os.path.join(pathdir,emotions[7])
        
        sourcefolder=os.path.join(folder,song)
        shutil.move(sourcefolder,destinationfolder)
    os.rmdir(folder)
    


