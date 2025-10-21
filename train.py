from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import os
import numpy as np
import cv2

class TrainData:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        self.root.title("Photo Sample Training")

        # -------------------- Top Title Bar --------------------
        title_lbl = Label(
            self.root,
            text="PHOTO SAMPLE TRAINING SYSTEM",
            font=("times new roman", 28, "bold"),
            bg="darkblue",
            fg="white"
        )
        title_lbl.place(x=0, y=0, width=1530, height=70)

        # -------------------- Back Button --------------------
        Button(
            self.root,
            text="Back",
            command=self.back,
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
            cursor="hand2"
        ).place(x=20, y=20, width=100, height=30)

        # -------------------- Description Section --------------------
        desc = (
            "This module is used to train facial data for the Face Recognition Attendance System.\n"
            "Ensure that you have collected multiple clear images for each student before training.\n"
            "Click on the 'Train Face Data' button below to start the model training process."
        )
        Label(
            self.root,
            text=desc,
            font=("times new roman", 14),
            bg="lightcyan",
            fg="black",
            justify="center"
        ).place(x=0, y=70, width=1530, height=100)

        # -------------------- Image Row --------------------
        img_paths = [
            r"C:\all\Face Recognition System\smsimages\trainface.jpg",
            r"C:\all\Face Recognition System\smsimages\trainface2.jpg",
            r"C:\all\Face Recognition System\smsimages\trainface3.jpg",
            r"C:\all\Face Recognition System\smsimages\trainface2.jpg",
            r"C:\all\Face Recognition System\smsimages\trainface2.jpg"
        ]

        x_pos = 0
        self.images = []
        for path in img_paths:
            img = Image.open(path).resize((306, 130), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.images.append(photo)
            Label(self.root, image=photo).place(x=x_pos, y=170, width=306, height=130)
            x_pos += 306

        # -------------------- Train Button --------------------
        Button(
            self.root,
            text="CLICK HERE TO TRAIN FACE DATA",
            command=self.train_classifier,
            bg="darkblue",
            fg="white",
            font=("arial", 26, "bold"),
            cursor="hand2"
        ).place(x=0, y=330, height=80, width=1350)

      
        # -------------------- Disclaimer Section --------------------
        disclaimer_text = (
            "This software is designed strictly for educational and institutional use. "
            "Ensure all data used is collected ethically .Unauthorized data collection, "
            "distribution, or storage of biometric information is strictly prohibited."
        )
        Label(
            self.root,
            text=disclaimer_text,
            wraplength=1280,
            justify="center",
            fg="gray15",
            bg="#FFF3CD",
            font=("times new roman", 12, "italic")
        ).place(x=0, y=420, width=1290, height=100)

        # -------------------- Footer --------------------
        Label(
            self.root,
            text="Developed by Raj Singh | Version 1.0 | © 2025 Face Recognition System",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        ).place(x=0, y=580, width=1530, height=40)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        npids=np.array(ids)
        
        #training classifier

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,npids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets completed")
            
    # -------------------- Back Function --------------------
    def back(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = TrainData(root)
    root.mainloop()
