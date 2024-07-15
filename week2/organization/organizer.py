import os
import shutil

folder_path = 'img_txt' 

imgs_folder = os.path.join(folder_path, 'imgs')
text_folder = os.path.join(folder_path, 'text')

os.makedirs(imgs_folder, exist_ok=True)

os.makedirs(text_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        if filename.lower().endswith(('.jpg')):
            new_path = os.path.join(imgs_folder, filename)

        elif filename.lower().endswith(('.txt')):
            new_path = os.path.join(text_folder, filename)

        else:
            print(f'Unrecognized file type: {filename}')
            continue

        os.rename(file_path, new_path)
