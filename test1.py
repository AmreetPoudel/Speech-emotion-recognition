# import csv
# import os
emotions=['neutral','calm','happy','sad','angry','fearful','disgust','surprised']
# DATASET_PATH=os.getcwd()
# songs=[]
# label=[]
destination_path=os.getcwd()
# itemNo=0
# for root, dirs, files in os.walk(DATASET_PATH, topdown=False):
#     for item in files:
#         song=os.path.join(root,item)
#         songs.append(song)
#         emotionNo=item[6:8]
#         # emotion=emotions.index(emotionNo)

#         label.append(emotionNo)
#     itemNo=itemNo+1

# #now we have list of songs on songs list and corresponding label in label list 
# #now we write the songs and label in csv form in a file
# #now we will create list of list list contains filename and label which can be 
# #directly converted to csv value
# # final_list=[]
# # itemNo=0
# # for song in songs:
# #     final_list.append(song,emotions[itemNo])
# #     itemNo=itemNo+1


# with open (destination_path,'w') as file:
#     write=csv.write(file)
#     write.writerows([("songs","label")])
#     write.writerows(songs,label)
# file.close()
    
#i did this one but end up coping the following code because of error but in fresh i will try this again










import csv
import os
import sys


def create_csv_file():
  dataset_path=os.path.abspath(dataset_path)
  csv_path=os.path.join(destination_path,'dataset.csv')
  filelist=[]
  for root,dirs,files in os.walk(dataset_path,topdown=False):
    for name in files:
      if(name.endswith('.wav')):
        fullname=os.path.join(root,name)
        filelist.append(fullname)
  split_format=str('/') if sys.platform=="linux" else str('\\')
  filenames=[]
  for idx,file in enumerate(filelist):
    filenames.append(file.split(split_format))
  types=[]
  for idx,path in enumerate(filenames):
        types.append((filelist[idx],emotions.index(path[-2]))) ##second last location has emotion name

  with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows([("path","label")])
        writer.writerows(types)
  f.close()
     # change destination_path to DATASET_PATH if destination_path is None 
  if destination_path == None:
        destination_path = dataset_path
        # write out as dataset_attr.csv in destination_path directory
        # if no error
  return True


