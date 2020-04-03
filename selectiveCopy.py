#! python3
# Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
import os
import shutil
from pathlib import Path

copySource = Path.home() / 'PythonTestDir'               # <--- Source folder
copyDestination = str(Path.home() / 'PythonCopyDir')     # <--- Destination folder

for root, dirs, filenames in os.walk(copySource):
    for eachFile in filenames:
        if eachFile.endswith('.txt'):  # <------------------ file extension to copy
            joinFiles = os.path.join(root, eachFile)
            print('Copying file %s to %s' %(joinFiles,copyDestination))
            shutil.copy(joinFiles, copyDestination)