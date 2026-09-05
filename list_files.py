import os
folders = input("Enter the name of the files with spaces in between: ").split()

for folder in folders:
    try :
        files = os.listdir(folder)
    except FileNotFoundError :
        print("The following directory doesnt exist : " + folder)
        continue    
    print("========Listing Files in the folder named " + folder)
    for file in files:
        print(file) 
