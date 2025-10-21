from tkinter import *
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import font
from studentdetails import StudentDetails
from tkinter import messagebox
import os
from train import TrainData
from face_recognition import fr_system
from attendance import ManageAttendance
from developer import Developer
from helpdesk import HelpDesk
import tkinter

class FaceRecognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("FaceRecognition_System")

        # ---------------- Top Images ----------------
        img1 = Image.open(r"C:\all\Face Recognition System\college_images\OIP.jpg").resize((500,130), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.img1).place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\all\Face Recognition System\college_images\face_rcgnz.jpeg").resize((500,130), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.img2).place(x=400, y=0, width=500, height=130)

        img3 = Image.open(r"C:\all\Face Recognition System\college_images\abesimg.jpeg").resize((500,130), Image.Resampling.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.img3).place(x=800, y=0, width=500, height=130)

        # ---------------- Background ----------------
        bgimg = Image.open(r"C:\all\Face Recognition System\college_images\bgimage.jpg").resize((1530,660), Image.Resampling.LANCZOS)
        self.bgimg = ImageTk.PhotoImage(bgimg)
        Label(self.root, image=self.bgimg).place(x=0, y=130, width=1530, height=660)

        # ---------------- Title ----------------
        title_font = font.Font(family="Helvetica", size=30, weight="bold")
        Label(
            self.root,
            text="Face Recognition Attendance System",
            font=title_font,
            bg="#f0f0f0",
            fg="#ff0000",
            relief=RAISED,
            padx=10, pady=10,
            anchor="center",
            justify="center"
        ).place(x=0, y=120, width=1530, height=48)

        # ---------------- Buttons ----------------
        button_info = [
            ("Student Details", r"C:\all\Face Recognition System\college_images\studentimage.jpg", self.StudentDetails),
            ("Face Recognition", r"C:\all\Face Recognition System\college_images\facedetect.jpg", self.fr_system),
            ("Attendance", r"C:\all\Face Recognition System\college_images\attendance.jpg", self.manageattendance),
            ("Train Face", r"C:\all\Face Recognition System\college_images\trainface.jpg", self.TrainData),
            ("Photos", r"C:\all\Face Recognition System\college_images\photos.jpg", self.open_img),
            ("Help Desk", r"C:\all\Face Recognition System\college_images\helpdesk.jpg", self.helpdesk),
            ("Developer", r"C:\all\Face Recognition System\college_images\developer.jpg", self.developer),
            ("Exit", r"C:\all\Face Recognition System\college_images\exit.jpg", self.iExit)
        ]
        # 4 buttons per row
        x_positions = [50, 350, 650, 950]  # X coordinates
        y_positions = [200, 420]           # Y coordinates for 2 rows
        btn_width = 200
        btn_height = 160
        text_height = 40

        btn_count = 0
        for text, img_path, cmd in button_info:
            try:
                img = Image.open(img_path).resize((btn_width, btn_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                setattr(self, f"{text.replace(' ','_').lower()}_img", photo)

                x = x_positions[btn_count % 4]
                y = y_positions[btn_count // 4]

                # Image Button
                b_img = Button(self.root, image=photo,command=cmd, cursor="hand2")
                b_img.place(x=x, y=y, width=btn_width, height=btn_height)

                # Text Button below image
                b_txt = Button(self.root, text=text, font="Arial 12 bold",command=cmd, bg="darkblue", fg="white", cursor="hand2",
                              )
                b_txt.place(x=x, y=y+btn_height, width=btn_width, height=text_height)

                btn_count += 1
            except:
                print(f"Image not found: {img_path}")
    
    def StudentDetails(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentDetails(self.new_window)

    def TrainData(self):
        self.new_window=Toplevel(self.root)
        self.app=TrainData(self.new_window)


    def fr_system(self):
        self.new_window=Toplevel(self.root)
        self.app=fr_system(self.new_window)


    def manageattendance(self):
        self.new_window=Toplevel(self.root)
        self.app=ManageAttendance(self.new_window)


    def open_img(self):
        os.startfile("data")

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def helpdesk(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit rhis project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    

    
        

    
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition_System(root)
    root.mainloop()
