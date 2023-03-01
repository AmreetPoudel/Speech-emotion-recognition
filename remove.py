#put this python file in same directory where there are video files it can be kept in parent directory os.listdir()will do its job

import moviepy

import os
import glob
import moviepy.editor 

pathdir = "."
folders=os.listdir()
for folder in folders:
    if os.path.isdir(folder):   
        pathdir=folder
     # Get a list of all the files with .mp4 extension in pathdir folder.
    mp4_filenames_list = glob.glob(os.path.join(pathdir, "*.mp4"))
    for filename in mp4_filenames_list:
        os.remove(filename)