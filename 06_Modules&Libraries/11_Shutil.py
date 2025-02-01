#for performing high level files operation
import shutil
import os

#creates a file as mentioned in destination , if already exists overwrite the text
shutil.copy(src="textfile" , dst="11_text")
print("File copied")

#for copying folders , can't recreate already existing folder
shutil.copytree(src="09_directory_made" , dst="11_Copied_Directory")
print("Directory copied")

#moving from one place to other , only can be run once , running after source file is moved will give error
# shutil.move(src="07_savegraph.png" , dst="11_Copied_Directory")
# print("File moved")

if os.path.exists(path="11_Copied_Directory") :
    #To delete a directory
    shutil.rmtree("11_Copied_Directory")
    print("Directory deleted")

