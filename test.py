import csv
import os
# import pandas as pd


# import pandas as pd 
emotions=['neutral','calm','happy','sad','angry','fearful','disgust','surprised']
DATASET_PATH=os.getcwd()
songs=[]
label=[]
destination_path=os.getcwd()
csv_path=os.path.join(destination_path,'dataset.csv')
for root, dirs, files in os.walk(DATASET_PATH, topdown=False):
    for file in files:
        song=os.path.join(root,file)
        songs.append(song)
        #unpacking the files to  file name and extension
        file_name, file_extension = os.path.splitext(file)
        if file_extension==".py":
            pass
        else:
            
            emotion=file[6:8]
            label.append(emotion)

# print(songs)
# print(label)
# final_label_data=[]
# for song in songs:
#     final_label_data.append(song,label)


# with open(csv_path, 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows([("path","label")])
#     writer.writerows(songs)
#     writer.writerows(label)
# f.close()

# list_dict = {'songs':songs, 'emotions':emotions} 
# df = pd.DataFrame(list_dict) 
# df.to_csv('example.csv', index=False) 

    
# create a .csv file for a songs and emotion ?

# import csv

# with open('name.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     # header
#     writer.writerow(['A', 'B', ..., 'F'])
#     for i in range(len(A)):
#         writer.writerow([A[i], B[i], ..., F[i]])


