from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import tkinter.messagebox as mb
import cv2
import mysql.connector
from time import strftime
from datetime import datetime
from datetime import datetime, timedelta
import csv
import os

class fr_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state('zoomed')  # fullscreen
        self.marked_ids = set()  

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # ---------------- Background ----------------
        try:
            bg_img = Image.open(r"C:\all\Face Recognition System\college_images\bgimage.jpg")
            bg_img = bg_img.resize((self.screen_width, self.screen_height), Image.Resampling.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(bg_img)
            Label(self.root, image=self.bg_img).place(x=0, y=0, width=self.screen_width, height=self.screen_height)
        except:
            self.root.configure(bg="#f0f0f0")  # fallback color

        # ---------------- Title ----------------
        title_font = font.Font(family="Helvetica", size=32, weight="bold")
        Label(
            self.root,
            text="FACE RECOGNITION SYSTEM",
            font=title_font,
            bg="darkblue",
            fg="white",
            relief=RAISED,
            bd=5
        ).place(x=0, y=0, width=self.screen_width, height=80)

        # ---------------- Subtitle ----------------
        subtitle_font = font.Font(family="Arial", size=18, weight="bold")
        Label(
            self.root,
            text="Automated Attendance and Security System",
            font=subtitle_font,
            bg="#1e90ff",
            fg="white",
            bd=3,
            relief=RIDGE
        ).place(x=0, y=80, width=self.screen_width, height=40)

        # ---------------- Info Label ----------------
        self.info_label = Label(
            self.root,
            text="Click the button below to start face recognition",
            font=("Arial", 16),
            bg="#f0f0f0",
            fg="black"
        )
        self.info_label.place(x=0, y=130, width=self.screen_width, height=30)

        # ---------------- Face Recognition Button ----------------
        button_width = 300
        button_height = 80
        button_y = 180

        try:
            face_img = Image.open(r"C:\all\Face Recognition System\college_images\face_rcgnz.jpg")
            face_img = face_img.resize((button_width, button_height), Image.Resampling.LANCZOS)
            self.face_photo = ImageTk.PhotoImage(face_img)
        except:
            self.face_photo = None

        self.face_btn = Button(
            self.root,
            text="FACE RECOGNITION",
            image=self.face_photo,
            compound=TOP,
            command=self.face_recog,
            font=("Arial", 16, "bold"),
            bg="black",
            fg="green",
            cursor="hand2",
            relief=RAISED,
            bd=5,
        )
        self.face_btn.place(x=40, y=button_y, width=button_width, height=button_height+50)

        # ---------------- Help Button ----------------
        self.help_btn = Button(
            self.root,
            text="Help / Contact",
            font=("Arial", 14, "bold"),
            bg="#ff8c00",
            fg="white",
            cursor="hand2",
            relief=RAISED,
            bd=5,
            command=self.open_help
        )
        self.help_btn.place(x=50, y=480, width=200, height=50)

        # ---------------- Exit Button ----------------
        self.exit_btn = Button(
            self.root,
            text="Exit",
            font=("Arial", 14, "bold"),
            bg="black",
            fg="red",
            cursor="hand2",
            relief=RAISED,
            bd=5,
            command=self.go_to_root
        )
        self.exit_btn.place(x=300, y=480, width=200, height=50)


    def go_to_root(self):
        self.root.withdraw()          # hide current window
        self.main_root.deiconify()    # show the main window again



  
    # ---------------- Button Functions ----------------
    def open_help(self):
        mb.showinfo("Help", "Contact admin at 9125474036")



    def mark_attendence(self, n, r, d, s, i):
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%H:%M:%S")
        filename = "attendance.csv"

        # Skip if already marked in memory
        if i in self.marked_ids:
            print(f"⏱️ Attendance already marked for {n} ({i}) in this session — skipping")
            return

        # Check last attendance in CSV (optional, still keep 30 min gap)
        last_time = None
        if os.path.exists(filename):
            with open(filename, "r", newline="",encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if row and row[0] == str(i):
                        try:
                            last_time = datetime.strptime(f"{row[6]} {row[5]}", "%d/%m/%Y %H:%M:%S")
                        except:
                            continue

        if last_time and (now - last_time) < timedelta(minutes=30):
            print(f"⏱️ Attendance already marked {((now - last_time).seconds)//60} min ago — skipping")
            return

        # Append to CSV
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="",encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([i, n, r, d, s, time_str, date_str, "Present"])
            print(f"✅ Attendance marked for {n} ({i}) at {time_str}")

        # Add to marked IDs set
        self.marked_ids.add(i)


    # ---------------- Face Recognition Function ----------------
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                # Default values
                n = r = d = s = i = "Unknown"

                # Fetch student info safely
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="raj@9125",
                        database="face_recognition_system"
                    )
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT S_Name, Roll_No, department, section, S_ID FROM students WHERE S_ID=%s", (id,)
                    )
                    result = cursor.fetchone()
                    conn.close()
                    if result:
                        n, r, d, s, i = result
                        # Convert everything to string
                        n = str(n)
                        r = str(r)
                        d = str(d)
                        s = str(s)
                        i = str(i)
                except:
                    pass  # Keep Unknown if DB fails

                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y - 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Section: {s}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"ID: {i}", (x, y + 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendence(n,r,d,s,i)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord.append((x, y, w, h))

            return coord


        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (0,255,0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = fr_system(root)
    root.mainloop()
