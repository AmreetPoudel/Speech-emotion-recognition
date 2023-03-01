# this entire code will take ~1 hr to complete as there are 24 actors and  3119 audio files 
#i.e in a minute 60 videos are converted to audio which is pretty good single video to audio in a second
#put this python file in same directory where there are video files it can be kept in parent directory os.listdir()will do its job
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
            # first convert the video to audio
            wav_file_name = filename.replace('.mp4', '.wav')  # Replace .mp4 with .wav
            audio.write_audiofile(wav_file_name)
            # #delete the video
            os.remove(filename)

            count=count+1
        
    else:
        print("Finished conversion")


for folder in folders:
    if os.path.isdir(folder):   
        pathdir=folder


    # Get a list of all the files with .mp4 extension in pathdir folder.
    mp4_filenames_list = glob.glob(os.path.join(pathdir, "*.mp4"))


