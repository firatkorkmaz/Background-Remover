# Removing Background from Images #

import os
import glob

try:
    from rembg import remove
except:
    os.system("pip install rembg")
    from rembg import remove


def RemoveBG(in_path):
    if not os.path.isfile(in_path):
        print(f"{in_path} does Not Exist!\n")
        return
    
    with open(in_path, 'rb') as i:
        try:
            input = i.read()
            output = remove(input)
        except:
            print(f"{in_path} is Not An Image File!\n")
            return
        
        out_path = in_path[:in_path.rfind(".")] + "_rembg.png"    # Save as ".png"
        with open(out_path, 'wb') as out_file:
            out_file.write(output)

    # Printing Process Information
    print(f"Source File: {in_path}")
    print(f"Saved File : {out_path}\n")

    
def main():
    exit_main = False
    while True:
        inputMode = input("File Name(s): 1\nFolder Name : 2\nExit Program: *\nSelect Input Mode: ")
        if inputMode == "*":
            exit_main = True
            break
        
        try:
            inputMode = int(inputMode.strip())
            if inputMode != 1 and inputMode != 2:
                print("Enter 1 or 2!\n")
                continue
        except:
            print("Enter 1 or 2!\n")
            continue
        
        break
    
    
    if not exit_main:
        if inputMode == 1:
            # Example: car.jpg, cat.png
            inputString = input("\nExample: car.jpg, cat.png\nEnter Image File Name(s): ")
            splitString = [x.strip() for x in inputString.split(',')]
            filenames = [f for f in splitString]

        else:
            # Example: image
            inputString = input("\nExample: image\nEnter Image Folder Name: ")
            splitString = inputString.strip()
            if not os.path.isdir(splitString):
                print("\nFolder does Not Exist!")
            filenames = glob.glob(splitString+'/*.*')

        if len(filenames) > 0:
            print()
            for file in filenames:
                RemoveBG(file)


if __name__ == '__main__':
    
    main()