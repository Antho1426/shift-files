#!/usr/local/bin/python3.7



# copy_folders_structure.py
# Cf.: https://stackoverflow.com/questions/40828450/how-to-copy-folder-structure-under-another-directory




# Run this file in the Terminal at the root of the project either with following
# command (if you want to perform some tests with the default argument values
# to check that the program works properly):
#
# python3.7 copy_folders_structure.py
#
# Or with this one (by selectively specifying the path of your "source folder"
# and "destination folder"):
#
# python3.7 copy_folders_structure.py --src absolute/path/to/source/folder --clonedStructure absolute/path/to/folder/in/which/the/folders/structure/will/be/cloned
#
# Example:
# python3.7 copy_folders_structure.py --src /Users/anthony/Dropbox/Camera Uploads/B\)ArtsMartiaux/Tricking/TrickersForTests --clonedStructure /Users/anthony/Desktop/Trickers
# Or:
# python3.7 copy_folders_structure.py --src /Volumes/Elements4TB/_PC-ALL-MY-FILES --clonedStructure /Users/anthony/Desktop/_PC-ALL-MY-FILES-Cloned-Structure
# python3.7 copy_folders_structure.py --src /Volumes/Elements4TB/_PC-ALL-MY-FILES/Documents/A\)EtudesUniversitairesEPFL --clonedStructure /Users/anthony/Desktop/_PC-ALL-MY-FILES-Cloned-Structure/Documents/A\)EtudesUniversitairesEPFL
# python3.7 copy_folders_structure.py --src /Volumes/Elements4TB/_PC-ALL-MY-FILES/Documents/B\)ArtsMartiaux --clonedStructure /Users/anthony/Desktop/_PC-ALL-MY-FILES-Cloned-Structure/Documents/B\)ArtsMartiaux
# python3.7 copy_folders_structure.py --src /Volumes/Elements4TB/_PC-ALL-MY-FILES/Documents/C\)Divers --clonedStructure /Users/anthony/Desktop/_PC-ALL-MY-FILES-Cloned-Structure/Documents/C\)Divers
# python3.7 copy_folders_structure.py --src /Volumes/Elements4TB/_PC-ALL-MY-FILES/Documents/D\)MesSociétés --clonedStructure /Users/anthony/Desktop/_PC-ALL-MY-FILES-Cloned-Structure/Documents/D\)MesSociétés
# python3.7 copy_folders_structure.py --src /Volumes/Elements4TB/_PC-ALL-MY-FILES/Images --clonedStructure /Users/anthony/Desktop/_PC-ALL-MY-FILES-Cloned-Structure/Images



# Setting the current working directory automatically
import os
project_path = os.getcwd() # getting the path leading to the current working directory
os.getcwd() # printing the path leading to the current working directory
os.chdir(project_path) # setting the current working directory based on the path leading to the current working directory




## Required packages
import os
import shutil
import warnings
from pathlib import Path
from time import perf_counter
from argparse import ArgumentParser




## Parsing the arguments
parser = ArgumentParser()
parser.add_argument('--src', type = str, default = project_path + '/folder_dest')
parser.add_argument('--clonedStructure', type = str, default = project_path + '/folder_dest_copied_structure')
args = parser.parse_args()




## Defining the paths of the two folders of interest
path_to_folder_dest = args.src
# ⚠️ This file below (in which the structure of "folder_dest" will be copied)
# should NOT exist yet! It will be created by running the code below
path_to_folder_dest_copied_structure = args.clonedStructure






# Function to ignore elements of type "file"
def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

# Copying the folder structure of "folder_dest" to a newly created
# "folder_dest_copied_structure" folder
try:
    shutil.copytree(path_to_folder_dest, path_to_folder_dest_copied_structure, ignore=ig_f)
except FileExistsError:
    warnings.warn("⚠️"
          "\n\n------\nThe folder 'folder_dest_copied_structure' already exists.\n"
          "The structure of 'folder_dest' won't be copied to "
          "'folder_dest_copied_structure'.\n"
          "First delete 'folder_dest_copied_structure' if you want to copy the "
          "structure of 'folder_dest' to 'folder_dest_copied_structure'.")



