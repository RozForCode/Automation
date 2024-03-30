# normally only one thing can be copied, with this we'll be able to copy multiple things and paste them.
#works from cli
import sys
import pyperclip  # so that we can pass input while we run the program file.
import json # we'll save the data  in a json file.

#two functions, one to create a json and one to read that json file.

def save_items(filepath):
    key  = input("Enter a key: ")
    data = {}
    while(key!= '-1'):
        data[key] = pyperclip.paste()+"\n"
        key  = input("Enter a key: ")
    with open(filepath,'a') as f:
        # we'll use json lib to put data into f
        json.dump(data, f)


def load_items(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    
def empty_file(filepath):#for reusing use the empty function first in the cli, write function is using append
    with open(filepath,'w') as f:
        f.write('')

data = load_items('test.json')
x = sys.argv[1]
if len(sys.argv) == 2:
    # print(sys.argv[1])
    if(x == "save"):save_items('test.json') 
    elif(x == "load"): 
        key = input("Enter key")
        if key in data:pyperclip.copy(data[key])
        else: print("key doesn't exist")
    elif(x == "list"): print(data)
    elif(x=="empty"): empty_file('test.json')
    else: print('unknown')
else: print("one value only")


