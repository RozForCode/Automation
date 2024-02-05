import os,shutil
path = r'file path/'
os.listdir(path)

files = os.listdir(path)

folder_names = []

for loop in range(0,len(folder_names)):
    if not os.path.exists(path+ folder_names[loop]):
        os.makedirs(path+folder_names[loop])

for file in files:
    if '.csv' in file and not os.path.exists(path+'csv files/'+ file):
        shutil.move(path+file , path+'csv files/'+ file)