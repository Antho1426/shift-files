# shift_files.py
Simple Python program used to shift files from a "source folder" to a
"destination folder" for storage.

<img src="shift-files-icon.png" alt="shif-files-icon-png" style="width: 320px;"/>

## Table of contents
* [1. Description](#1-description)
* [2. Getting started](#2-getting-started)
    * [2.1 Dependencies](#21-dependencies)
    * [2.2 Installing](#22-installing)
    * [2.3 Executing program](#23-executing-program)
* [3. Version history](#3-version-history)

<!-- toc -->

## 1. Description
`shift_files.py` is intended to simplify the workflow of moving files and
folders from a "source folder" to a "destination folder" by mimicking the
structure of the "source folder" into the structure of the "destination folder".
This software might be useful to quickly and automatically move files to from a
computer to an external hard drive on which they will be stored.

The python program `copy_folders_structure.py` can initially be used to copy the
folders structure (i.e. all the folders but empty of any files) of an external
hard drive for example. This can be done by typing following command at the root
of this project:

`python3.7 copy_folders_structure.py --src absolute/path/to/source/folder --clonedStructure absolute/path/to/folder/in/which/the/folders/structure/will/be/cloned`

The folders situated in the "source folder" remain in place, but their files are
shifted (i.e. moved) in the "destination folder" in case they are not already
existing in the "destination folder".
If a file needed to be shift from the "source folder" to
the "destination folder" already exists in the "destination folder", it is left
in place in the "source folder" and its absolute path is reported in the log
text file `logAlreadyExistingFiles.txt` eventually created in the parent
directory of the "source folder".
In case an element of the "source folder" is
not a file nor a folder, then it is left in place in the "source folder" and its
absolute path is reported in `logNonFiles.txt` (eventually created in the parent
directory of the "source folder").
Finally all the files that have been
successfully shifted from the "source folder" to the "destination folder" are
reported in `logAllFiles.txt` (eventually created in the parent directory of the
"source folder")

The program basically goes through each file and each folder (and each file in
each subfolder) of the "source folder" and behaves as follows:
- If the current folder doesn't exist in the subfolder of the "destination
folder", then it creates it and moves its whole content (i.e. each of its files
and folders) in that new folder;
otherwise it simply moves each of the files (and folders in case they
don't already exist) in the corresponding folder of the "destination folder".
- If the file doesn't already exist in the "destination folder", it simply moves
it in the "destination folder";
otherwise, it leaves it in place in the "source folder"
and report its absolute path in `logAlreadyExistingFiles.txt` (eventually
created in the parent directory of the "source folder").

## 2. Getting started


### 2.1 Dependencies
* Tested on macOS Catalina version 10.15.7
* Python 3.7

### 2.2 Installing
`pip install -r requirements.txt`

### 2.3 Executing program
A simple test with the default "source folder" and "destination folder" can be
done by typing following Terminal command at the root of the project:

`python3.7 shift_files.py`

Following Terminal command uses argument parsing and allows to select any source and
destination folders by specifying their absolute path:

`python3.7 shift_files.py --src absolute/path/to/source/folder --dest absolute/path/to/destination/folder`

Example:

`python3.7 shift_files.py --src /Users/anthony/Dropbox/Camera Uploads/_PC-ALL-MY-FILES-Cloned-Structure --dest /Volumes/Elements4TB/_PC-ALL-MY-FILES`

## 3. Version history
* 0.1
    * Initial release