import os
import zipfile

base_dir = '.' # absolute path to the data folder
extension = ".zip"

os.chdir(base_dir)  # change directory from working dir to dir with files


def unpack_all_in_dir(_dir):
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(_dir)  # extract file to dir
            zip_ref.close()  # close file
            os.remove(file_name)  # delete zipped file
        elif os.path.isdir(abs_path):
            unpack_all_in_dir(abs_path)  # recurse this function with inner folder


unpack_all_in_dir(base_dir)