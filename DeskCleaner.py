""" In this project, my aim is to make a scrip (if possible with a GUI) in order to sort out my Downloads folder
meaning that i want to place all png, jpg, img files into a folder in another location on my pc, as well as for 
mp3 mp4..etc."""

 
""" !TODO: basic file handeling | Catergorize and Organize | User input and flexibility | Error Handiling
(optional) make a GUI """ 


# Basic file handeling:

import os
import shutil
import mimetypes


# i'm going to be working on the Downloads file
folder_path = "C:\\Users\\USER\\Downloads"

# this lists all the files in my downloads folder
files = os.listdir(folder_path)

for file in files:
    # basic check if it's a file or not
    if os.path.isfile(os.path.join(folder_path,file)):
        file_name, file_extension = os.path.splitext(file)
        # just checking if the files exist
        # print(f"File: {file_name}, Extension: {file_extension}")

""" !TODO: Today i will start by catergorzing and organizing the files"""
# Use a dictionary in order to map files to folders

# finder = {
#     ".mp4": "Videos",
#     ".avi": "Videos",
#     ".m4v": "Videos",
#     ".jpeg": "Pictures",
#     ".jpg": "Picitures",
#     ".img": "Pictures",
#     ".png": "Pictures",
#     ".wav": "Music",
#     ".mp3": "Music",
#     ".aiff": "Music",
# }

# for f_name in os.listdir(folder_path):
#     # i could use the split() here, but using the os library is better
#     # os.path.splittext makes 2 splits, at the file name and at the extention, that's why we use _ and extention 
#     _, extention = os.path.splitext(f_name) 
#     extention = extention.lower()
#     # Debug: Print the extension and file name
#     if extention == ".mp4":
#         print(f"Processing file: {f_name} with extension: {extention}")

#     if extention in finder:
#         target_folder = finder[extention]
#         new_path = os.path.join (folder_path,target_folder)

#         # if the folder doesn't extis, make it
#         if not os.path.exists(new_path):
#             os.makedirs(new_path)

#         current_path = os.path.join(folder_path,f_name)
#         new_path_with_file = os.path.join(new_path,f_name)

#         # moving the file
#         shutil.move(current_path,new_path_with_file)

""" I found it to be quite a pain to use a dictionary with this project, since there are a lot
of diffrent file names for diffrent types, so i am thinking of switching to using mimetypes """

for f_name in os.listdir(folder_path):
    # getting the full file path
    file_path = os.path.join(folder_path,f_name)

    if os.path.isfile(file_path):
        # using mimetypes to guess the type of the file
        mime_type, _ = mimetypes.guess_type(f_name)
        # debug print
        #print(f"name of file: {f_name}| type: {mime_type}")

    # sorting the files
    if mime_type:
        if mime_type.startswith("image/"):
            target_folder = "Pictures"
        elif mime_type.startswith("video/"):
            target_folder = "Videos"
        elif mime_type.startswith("audio/"):
            target_folder = "Music"
        elif mime_type in ["application/pdf", "application/zip"]:
            print(f"Skipping file: {f_name}")
            continue  # Skip to the next file
        else:
            print(f"Unkown MIME file type for {f_name}")
            continue

        new_path = os.path.join(folder_path,target_folder)

        # make the folder if it doens't exits

        if not os.path.exists(target_folder):
            os.makedirs(new_path)
            print(f"Created folder: {new_path}")

            new_path_file = os.path.join(new_path,f_name)

            # move the files 
            try: 
                shutil.move(file_path,new_path_file)
                # debug print
                print(f"Moved file: {f_name} to folder: {new_path_file}")
            except Exception as e:
                print(f"Error while moving file {f_name}")

        else:
            print(f"Unkown MIME file type for {f_name}")
