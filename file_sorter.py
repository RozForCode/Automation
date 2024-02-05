#the shutil module provides higher level interface for file operations
# including functions to copy, move and delete files and directories.
import os,shutil

#provide the path to the place where you want to sort files
# end the path with '/' to make new path creation easier later in the code
path = r'file path/'

#this will list all the files in the given path
os.listdir(path)

# store all the files in this variable
files = os.listdir(path)

#check the files and see which folder you want to sort them into and 
#put the folder types in the folder_names list
folder_names = []

#loop through the list to check if the folder exists, if not the create it.
for loop in range(0,len(folder_names)):
    if not os.path.exists(path+ folder_names[loop]):
        os.makedirs(path+folder_names[loop])

# now iterate through all the files, check and move them into the right place
# no. of conditions will depends on the no. of elements in the folder_name list.
for file in files:
    if '.csv' in file and not os.path.exists(path+'csv files/'+ file):
        shutil.move(path+file , path+'csv files/'+ file)