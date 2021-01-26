#!/usr/local/bin/python3.7


# shift_files.py


# Run this file in the Terminal at the root of the project either with following
# command (if you want to perform some tests with the default argument values
# to check that the program works properly):
#
# python3.7 shift_files.py
#
# Or with this one (by selectively specifying the path of your "source folder"
# and "destination folder"):
#
# python3.7 shift_files.py --src absolute/path/to/source/folder --dest absolute/path/to/destination/folder
#
# Example:
# python3.7 shift_files.py --src /Users/anthony/Dropbox/Camera Uploads/B\)ArtsMartiaux/Tricking/TrickersForTests --dest /Users/anthony/Desktop/Trickers
# Or:
# python3.7 shift_files.py --src /Users/anthony/Dropbox/Camera Uploads/_PC-ALL-MY-FILES-Cloned-Structure --dest /Volumes/Elements4TB/_PC-ALL-MY-FILES





# Setting the current working directory automatically
import os
project_path = os.getcwd() # getting the path leading to the current working directory
os.getcwd() # printing the path leading to the current working directory
os.chdir(project_path) # setting the current working directory based on the path leading to the current working directory





## Required packages
import os
import shutil
import math as m
from pathlib import Path
from time import perf_counter
from termcolor import colored
from argparse import ArgumentParser






## Required functions
def computeElapsedTime(time):
    hours, rem = divmod(time, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)






## Parsing the arguments
parser = ArgumentParser()
parser.add_argument('--src', type = str, default = project_path + '/folder_src')
parser.add_argument('--dest', type = str, default = project_path + '/folder_dest')
args = parser.parse_args()






## Defining the paths of the two folders of interest
#path_to_folder_src = project_path + '/folder_src'
path_to_folder_src = args.src
#path_to_folder_dest = project_path + '/folder_dest'
path_to_folder_dest = args.dest







## Getting the total number of files in the "source folder"
# (By visiting each folder and subfolder)
number_of_total_files = 0
for root, directories, files in os.walk(path_to_folder_src):
    for filename in files:
        number_of_total_files += 1

# Initializing the number of handled file
global number_of_handled_files
number_of_handled_files = 0





## Creating the logging text files (in case they do not exist yet) and placing
# them into the parent directory of the "source folder"
path_to_parent_of_folder_src = Path(path_to_folder_src).parent

# Creating "logAllFiles.txt" if it does not exist yet
logAllFilesTxtPath = str(path_to_parent_of_folder_src) + '/' + 'logAllFiles.txt'
if not os.path.exists(logAllFilesTxtPath):
    with open(logAllFilesTxtPath, "w"):
        pass
# Or erasing its content in case it already exists
else:
    logAllFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logAllFiles.txt', "r+")
    logAllFilesTXT.truncate(0)
    logAllFilesTXT.close()
# Writing the heading of the text file at the top of the text file:
logAllFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logAllFiles.txt', "w")
logAllFilesTXT.write('"logAllFiles.txt" lists all the files encountered in the "source folder":\n')
logAllFilesTXT.close()

# Creating "logAlreadyExistingFiles.txt" if it does not exist yet
logAlreadyExistingFilesTxtPath = str(path_to_parent_of_folder_src) + '/' + 'logAlreadyExistingFiles.txt'
if not os.path.exists(logAlreadyExistingFilesTxtPath):
    with open(logAlreadyExistingFilesTxtPath, "w"):
        pass
# Or erasing its content in case it already exists
else:
    logAlreadyExistingFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logAlreadyExistingFiles.txt', "r+")
    logAlreadyExistingFilesTXT.truncate(0)
    logAlreadyExistingFilesTXT.close()
# Writing the heading of the text file at the top of the text file:
logAlreadyExistingFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logAlreadyExistingFiles.txt', "w")
logAlreadyExistingFilesTXT.write('"logAlreadyExistingFiles.txt" lists all the files encountered in the "source folder" that were already present in the "destination folder" before executing the "shift_files" program:\n')
logAlreadyExistingFilesTXT.close()

# Creating "logNonFiles.txt" if it does not exist yet
logNonFilesTxtPath = str(path_to_parent_of_folder_src) + '/' + 'logNonFiles.txt'
if not os.path.exists(logNonFilesTxtPath):
    with open(logNonFilesTxtPath, "w"):
        pass
# Or erasing its content in case it already exists
else:
    logNonFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logNonFiles.txt', "r+")
    logNonFilesTXT.truncate(0)
    logNonFilesTXT.close()
# Writing the heading of the text file at the top of the text file:
logNonFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logNonFiles.txt', "w")
logNonFilesTXT.write('"logNonFiles.txt" lists all the elements encountered in the "source folder" that are NEITHER files NOR folders:\n')
logNonFilesTXT.close()













## "shiftFilesToDestFolder" function (main function)
# Move the files from the "source folder" into the "destination folder" and
# list the files and folders in "source folder"


def shiftFilesToDestFolder(srcFolderPath, destFolderPath):
    '''
    For the given path, get the list of all files in the directory tree
    '''

    # Create a list of files and sub directories
    # names in the given current main directory
    listOfFile = os.listdir(srcFolderPath)
    allFiles = list()

    # Adding global statement for the variable "global number_of_handled_files"
    # at the beginning of the function "shiftFilesToDestFolder"
    global number_of_handled_files

    # Iterate over all the entries
    for entry in listOfFile:

        # Create full path
        srcFullPath = os.path.join(srcFolderPath, entry)
        destFullPath = os.path.join(destFolderPath, entry)

        # If entry is a FILE in the "source folder" and if it does NOT exist
        # already in the "destination folder", simply move it to the
        # "destination folder"
        if os.path.isfile(srcFullPath) & (not os.path.isfile(destFullPath)):
            path_to_file_in_src_to_move_in_dest = srcFullPath
            path_to_get_file_in_dest = destFolderPath

            # Moving to "destination folder" (i.e. copying to the "destination
            # folder" and then erasing from the "source folder")
            try:
                shutil.move(path_to_file_in_src_to_move_in_dest, path_to_get_file_in_dest)
            except:
                print('shutil.Error: Destination path already exists')

            # Appending the current file to the list "allFiles"
            allFiles.append(path_to_file_in_src_to_move_in_dest)
            # Logging the current file in the text file "logAllFiles.txt"
            logAllFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logAllFiles.txt', "a")
            logAllFilesTXT.write("\n" + path_to_file_in_src_to_move_in_dest)
            logAllFilesTXT.close()

            # Indicating that we have handled one additional file out of of
            # "source folder"
            number_of_handled_files += 1
            # Printing the shifting progress
            time_so_far = perf_counter()
            shifting_progress = (number_of_handled_files / number_of_total_files) * 100
            elapsed_time_so_far = computeElapsedTime(time_so_far - time_start)
            # Updating the console
            print(
                '{0:.3f}%|{1}{2}| handled files: {3}/{4} [tot. time: {5}] [avg. time/file: {6:.3f}[ms]]'.format(
                    shifting_progress,
                    colored(m.floor(shifting_progress / 2) * '█', 'green'),
                    m.ceil((100 - shifting_progress) / 2) * ' ',
                    colored(number_of_handled_files, 'blue'),
                    number_of_total_files, colored(elapsed_time_so_far, 'red'),
                    (time_so_far - time_start) / number_of_handled_files * 1000))


        # Else if entry is a DIRECTORY then dig into this directory and
        # get the list of files in this directory
        elif os.path.isdir(srcFullPath):
            subdirectoryPathInSrcFolder = srcFolderPath + '/' + entry
            subdirectoryPathInDestFolder = destFolderPath + '/' + entry

            # If this directory does NOT exist in the "destination folder",
            # we create it
            if not (os.path.isdir(subdirectoryPathInDestFolder)):
                p = Path(subdirectoryPathInDestFolder)
                try:
                    p.mkdir()
                except FileExistsError as exc:
                    print(exc)

            # Digging into the current subfolder
            # (Now that we know that this subfolder exists at any rate)
            allFiles = allFiles + shiftFilesToDestFolder(subdirectoryPathInSrcFolder, subdirectoryPathInDestFolder)

        # Else it means that the element is neither a file nor a folder
        # (it could be e.g. a hidden file beginning with a ".")
        else:

            if os.path.isfile(destFullPath):

                print("⚠️ The file '{0}' to be shifted to the 'destination folder' already exists in the 'destination folder'...".format(entry))

                # Logging the current "already existing file" in the text file "logAlreadyExistingFiles.txt"
                logAlreadyExistingFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logAlreadyExistingFiles.txt', "a")
                logAlreadyExistingFilesTXT.write("\n" + srcFullPath)
                logAlreadyExistingFilesTXT.close()

                # Indicating that we have handled one additional file out of of
                # "source folder"
                number_of_handled_files += 1
                # Printing the shifting progress
                time_so_far = perf_counter()
                shifting_progress = (number_of_handled_files / number_of_total_files) * 100
                elapsed_time_so_far = computeElapsedTime(time_so_far - time_start)
                # Updating the console
                print(
                    '{0:.3f}%|{1}{2}| handled files: {3}/{4} [tot. time: {5}] [avg. time/file: {6:.3f}[ms]]'.format(
                        shifting_progress,
                        colored(m.floor(shifting_progress / 2) * '█', 'green'),
                        m.ceil((100 - shifting_progress) / 2) * ' ',
                        colored(number_of_handled_files, 'blue'),
                        number_of_total_files,
                        colored(elapsed_time_so_far, 'red'),
                        (time_so_far - time_start) / number_of_handled_files * 1000))


            else:
                print("⚠️ The element '{0}' is NOT a file NOR a directory and won't be copied to the destination folder...".format(entry))
                # Logging the current "non file" in the text file "logNonFiles.txt"
                logNonFilesTXT = open(str(path_to_parent_of_folder_src) + '/' + 'logNonFiles.txt', "a")
                logNonFilesTXT.write("\n" + srcFullPath)
                logNonFilesTXT.close()


    return allFiles












# Initial spacing in the console window
print("\n")
# Move files from "source folder" to "destination folder" and get the list of
# all files in directory tree at given path
time_start = perf_counter()
allFiles = shiftFilesToDestFolder(path_to_folder_src, path_to_folder_dest)


# Finally: printing all the encountered files
print("\n\nSummary log of ALL the encountered files:\n" + "------\n")
for elem in allFiles:
    print(elem)