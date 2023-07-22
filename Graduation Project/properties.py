import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import euclidean
import hashlib
import PyInstaller.__main__
import pyfiglet
from termcolor import colored
import os

os.system('cls')
Project_Name = pyfiglet.figlet_format("                           P r o p e r t i e s  ")
Project_Name_Color = colored(Project_Name, "yellow")
print(Project_Name_Color)
def Converting_To_Binn(contentt):
        if type(contentt)==str:
            return ''.join([format(ord(i),"08b")for i in contentt])
        elif type(contentt)==bytes or type(contentt)==np.ndarray:
            return [format(i,"08b")for i in contentt ]
        elif type(contentt)==int or type(contentt)==np.uint8:
            return format(contentt,"08b")
        else:
            print(" * Please, Enter Your data as Text")  

 

img1 = cv2.imread('G:\\Graduarion Project\\4- Fourth Method\\AppData\\original.png')
img2 = cv2.imread('G:\\Graduarion Project\\4- Fourth Method\\AppData\\Image.png')
#f= open ("E:\\Graduation_Project\\AppData\\list1.txt","a")
my_list = []
for row in img1:
    for pixel in row:
        r, g, b = Converting_To_Binn(pixel)
        my_list.append(r)
        my_list.append(g)
        my_list.append(b) 
#f.write(str(my_list))
list_str = str(my_list)
unique_number = hashlib.sha256(list_str.encode()).hexdigest()
my_list2 = []
#m= open ("E:\\Graduation_Project\\AppData\\list2.txt","a")
for row in img2:
    for pixel in row:
        r, g, b = Converting_To_Binn(pixel)
        my_list2.append(r)
        my_list2.append(g)
        my_list2.append(b) 
#m.write(str(my_list2))
list_strr = str(my_list2)
unique_numberr = hashlib.sha256(list_strr.encode()).hexdigest()

print('\n\n\n * Hashing For The  Original Image is     ======>  ',unique_number)
print('\n * Hashing For The  Injected Image is     ======>  ',unique_numberr)



gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
mse = np.mean((gray1 - gray2) ** 2)
if mse ==0:
    print('\n\n * PSNR (Peak Signal-to-Noise Ratio)      ======>   infinite')
else:
    psnr = cv2.PSNR(img1, img2)
    print('\n\n * PSNR (Peak Signal-to-Noise Ratio)      ======>  ', psnr)

print("\n\n * MSE  (Mean Squared Error)              ======>  ", mse)

cos_sim = np.dot(gray1.ravel(), gray2.ravel()) / (np.linalg.norm(gray1.ravel()) * np.linalg.norm(gray2.ravel()))
print('\n\n * Cosine Similarity                      ======>  ', int(cos_sim))


dist = euclidean(img1.flatten(), img2.flatten())

# print the distance
print("\n\n * Euclidean Distance between the images  ======>  ", dist)


img1_channels = cv2.split(img1)
img2_channels = cv2.split(img2)

# Create a figure with four subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 7))

# Loop through each channel and plot the histograms for the first image
for i, color in enumerate(('r', 'g', 'b')):
    hist, bins = np.histogram(img1_channels[i].ravel(), 256, [0, 256])
    ax1.plot(hist, color=color)
    ax1.set_xlim([0, 256])
    ax1.set_ylim([0, max(hist)])
    ax1.set_title("Image 1 Color Histograms")


# Loop through each channel and plot the histograms for the second image
for i, color in enumerate(('r', 'g', 'b')):
    hist, bins = np.histogram(img2_channels[i].ravel(), 256, [0, 256])
    ax2.plot(hist, color=color)
    ax2.set_xlim([0, 256])
    ax2.set_ylim([0, max(hist)])
    ax2.set_title("Image 2 Color Histograms")


# Display the images
ax3.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))


ax4.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))


# Display the plot
plt.show()