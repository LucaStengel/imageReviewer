#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import shutil

currentFolder = "None selected."
jpgList = []
jpgCount = 0
count = "0/0"

def getFolder():
    currentFolder = filedialog.askdirectory(title="Select your image folder")
    l2.config(text=currentFolder)
    fileList = os.listdir(currentFolder)
    jpgList = [file for file in fileList if file.lower().endswith('.jpg')]
    jpgCount = len(jpgList)
    LjpgList.config(text="JPG's found: " + str(jpgCount))
    LjpgList.list = jpgList
    if jpgCount > 0:
        showImage(currentFolder + "/" + jpgList[0])
        LImagecount.config(text="1/"+str(jpgCount))

def startFolderAgain(start):
    currentFolder = l2.cget("text")
    fileList = os.listdir(currentFolder)
    jpgList = [file for file in fileList if file.lower().endswith('.jpg')]
    jpgCount = len(jpgList)
    LjpgList.config(text="JPG's found: " + str(jpgCount))
    LjpgList.list = jpgList
    if jpgCount > 0:
        showImage(currentFolder + "/" + jpgList[start-1])
        LImagecount.config(text=str(start) + "/"+str(jpgCount))

def nextImage():
    count = LImagecount.cget("text")
    parts = count.split('/')
    erste = int(parts[0])
    zweite = int(parts[1])
    if erste == zweite:
        None
    else:
        showImage(l2.cget("text") + "/" + LjpgList.list[erste])
        LImagecount.config(text=str(erste+1)+"/"+str(zweite))

def previousImage():
    count = LImagecount.cget("text")
    parts = count.split('/')
    erste = int(parts[0])
    zweite = int(parts[1])
    if erste == 1:
        None
    else:
        showImage(l2.cget("text") + "/" + LjpgList.list[erste-2])
        LImagecount.config(text=str(erste-1)+"/"+str(zweite))
        
def pushFolder():
    folder = filedialog.askdirectory(title="Select your image folder")
    l4.config(text=str(folder))

def resize_image(image, max_width, max_height):
    # Originalgröße des Bildes
    width, height = image.size
    
    # Berechnung des Skalierungsfaktors
    ratio = min(max_width / width, max_height / height)
    
    # Neue Größe basierend auf dem Skalierungsfaktor
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    
    return image.resize((new_width, new_height), Image.LANCZOS)

def showImage(imagePath):
    image = Image.open(imagePath)
    image = resize_image(image, 750, 500)
    tkImage = ImageTk.PhotoImage(image)
    Limage.image = tkImage
    Limage.config(image=tkImage, anchor="center")

def move():
    LjpgList
    count = LImagecount.cget("text")
    parts = count.split('/')
    erste = int(parts[0])
    path = l2.cget("text") + "/" + LjpgList.list[erste-1]
    print(path)
    print(l4.cget("text"))
    shutil.move(path, l4.cget("text"))
    startFolderAgain(erste)


root = tk.Tk()
root.title("Image review")
root.geometry('1200x800')
root.resizable(False, False)

selectionFrame = tk.Frame(root, width=300, height=720, highlightbackground='gray', highlightthickness=2)
selectionFrame.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)

l1 = tk.Label(selectionFrame, text="Select image folder:", anchor="nw")
l1.place(x=20, y=20, width=150, height=50)

button1 = tk.Button(selectionFrame, text='Search folder', anchor="center", command=getFolder)
button1.place(x=190, y=15)

l2 = tk.Label(selectionFrame, text=currentFolder,background='grey', anchor='nw')
l2.place(x=20, y=50, width=300, height=25)

LjpgList = tk.Label(selectionFrame, text="JPG's found: " + str(jpgCount), anchor='nw')
LjpgList.place(x=20, y=80)

canvas3 = tk.Canvas(selectionFrame)
canvas3.place(x=0, y=105, width=335, height=20)
canvas3.create_line(0, 10, 796, 10, fill="grey", width=2)


l3 = tk.Label(selectionFrame, text="Select destiny folder: ")
l3.place(x=20, y=130)

button2 = tk.Button(selectionFrame, text='Search folder', anchor="center", command=pushFolder)
button2.place(x=190,y=125)

l4 = tk.Label(selectionFrame, text="None selected.", background='grey', anchor='nw')
l4.place(x=20, y=160, width=300, height=25)









imageFrame = tk.Frame(root, width=760, height=720, highlightbackground='gray', highlightthickness=2)
imageFrame.grid(row=0, column=1, padx=0, pady=20, ipadx=20, ipady=20)

LImagecount = tk.Label(imageFrame, text=count, anchor="center")
LImagecount.place(x=0, y=2, width=796)

canvas1 = tk.Canvas(imageFrame)
canvas1.place(x=0, y=20, width=796, height=20)
canvas1.create_line(0, 10, 796, 10, fill="grey", width=2)

Limage = tk.Label(imageFrame, anchor="center")
Limage.place(x=20,y=50)

canvas1 = tk.Canvas(imageFrame)
canvas1.place(x=0, y=564, width=796, height=20)
canvas1.create_line(0, 10, 796, 10, fill="grey", width=2)

Bnext = tk.Button(imageFrame, text="previous", anchor="center", command=previousImage)
Bnext.place(x=20, y=585)
Bnext = tk.Button(imageFrame, text="next", anchor="center", command=nextImage)
Bnext.place(x=120, y=585)



Bmove = tk.Button(imageFrame, text="move image", anchor="center", command=move)
Bmove.place(x=250, y=585)


root.mainloop() 