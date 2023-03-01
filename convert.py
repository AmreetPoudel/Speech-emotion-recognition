import moviepy
import os
import glob
import moviepy.editor 
count=0
pathdir = "."
folders=os.listdir()
for folder in folders:
    if os.path.isdir(folder):   
        pathdir=folder
    else:
        pass


    # Get a list of all the files with .mp4 extension in pathdir folder.
    mp4_filenames_list = glob.glob(os.path.join(pathdir, "*.mp4"))

    for filename in mp4_filenames_list:
        print(filename)
        print(count)
            
        video = moviepy.editor.VideoFileClip(filename)
        audio = video.audio

        # Some of my mp4 files are without audio.
        if audio is not None:
            wav_file_name = filename.replace('.mp4', '.wav')  # Replace .mp4 with .wav
            audio.write_audiofile(wav_file_name)
            count=count+1
        
    else:
        print("Finished conversion")


for folder in folders:
    if os.path.isdir(folder):   
        pathdir=folder


    # Get a list of all the files with .mp4 extension in pathdir folder.
    mp4_filenames_list = glob.glob(os.path.join(pathdir, "*.mp4"))


