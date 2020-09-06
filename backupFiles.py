import os
import shutil
source = input("Enter Source Folder Name")
destination = input("Enter Destination Name")
source = source+"/"
destination = destination+"/"
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)