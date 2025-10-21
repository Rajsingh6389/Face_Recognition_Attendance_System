from tkinter import *
from PIL import Image, ImageTk
from tkinter import font, ttk, messagebox
import mysql.connector
import os
import cv2


class StudentDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Student Details")

        # ------------------ Variables ------------------
        self.var_S_ID = IntVar()
        self.var_S_Name = StringVar()
        self.var_Roll_No = StringVar()
        self.var_course = StringVar()
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_mobilenumber = StringVar()
        self.var_emailid = StringVar()
        self.var_photosamplestatus = StringVar()
        self.var_teachername = StringVar()
        self.var_dob = StringVar()
        self.var_address = StringVar()
        self.var_section = StringVar()
        self.var_gender = StringVar()
        self.var_cam=StringVar()
        

        
        

        # ---------------- Top Images ----------------
        img1 = Image.open(r"C:\all\Face Recognition System\smsimages\st1.jpg").resize((500,130), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.img1).place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\all\Face Recognition System\smsimages\st2.jpg").resize((500,130), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.img2).place(x=450, y=0, width=500, height=130)

        img3 = Image.open(r"C:\all\Face Recognition System\smsimages\st3.jpg").resize((530,130), Image.Resampling.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.img3).place(x=900, y=0, width=400, height=130)

        # ---------------- Background ----------------
        bgimg = Image.open(r"C:\all\Face Recognition System\college_images\bgimage.jpg").resize((1530,660), Image.Resampling.LANCZOS)
        self.bgimg = ImageTk.PhotoImage(bgimg)
        Label(self.root, image=self.bgimg).place(x=0, y=130, width=1530, height=660)

        # ---------------- Title ----------------
        title_font = font.Font(family="Helvetica", size=30, weight="bold")
        Label(
            self.root,
            text="Student Management System",
            font=title_font,
            bg="darkblue",
            fg="white",
            relief=RAISED,
            padx=10, pady=10,
            anchor="center"
        ).place(x=0, y=120, width=1530, height=50)

        # ---------------- Main Frame ----------------
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=10, y=170, width=1500, height=560)

        # ---------------- Left Frame ----------------
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"), bg="white")
        left_frame.place(x=10, y=5, width=700, height=560)

        # ---------------- Current Course Frame ----------------
        curcourse = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course",
                               font=("times new roman", 12, "bold"))
        curcourse.place(x=5, y=5, width=680, height=150)  # increased height

        # Department
        Label(curcourse, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        dep_combo = ttk.Combobox(curcourse, textvariable=self.var_department, font=("times new roman", 12), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Section
        Label(curcourse, text="Section:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        section_combo = ttk.Combobox(curcourse, textvariable=self.var_section, font=("times new roman", 12), state="readonly")
        section_combo["values"] = ("Select Section", "A", "B", "C")
        section_combo.current(0)
        section_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Course
        Label(curcourse, text="Course:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        course_combo = ttk.Combobox(curcourse, textvariable=self.var_course, font=("times new roman", 12), state="readonly")
        course_combo["values"] = ("Select Course", "B-TECH", "M-TECH", "MCA", "MBA")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Year
        Label(curcourse, text="Year:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        year_combo = ttk.Combobox(curcourse, textvariable=self.var_year, font=("times new roman", 12), state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Semester
        Label(curcourse, text="Semester:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        semester_combo = ttk.Combobox(curcourse, textvariable=self.var_sem, font=("times new roman", 12), state="readonly")
        semester_combo["values"] = ("Select Semester", "Odd Sem", "Even Sem")
        semester_combo.current(0)
        semester_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(curcourse,text="Select Your Camera", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        cam_combo=ttk.Combobox(curcourse,textvariable=self.var_cam,font=("times new roman",12),state="readonly")
        cam_combo["values"]=("ClassRoom Camera","camera1","camera2")
        cam_combo.current(0)
        cam_combo.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # ---------------- Class Student Information Frame ----------------
        class_studentinfo = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                       font=("times new roman", 12, "bold"))
        class_studentinfo.place(x=5, y=160, width=680, height=380)  # increased height

        # Row 1
        Label(class_studentinfo, text="Student ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_S_ID, width=20, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=10, sticky=W)

        Label(class_studentinfo, text="Student Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_S_Name, width=20, font=("times new roman", 12)).grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Row 2
        Label(class_studentinfo, text="Roll No:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_Roll_No, width=20, font=("times new roman", 12)).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        Label(class_studentinfo, text="Email ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_emailid, width=20, font=("times new roman", 12)).grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Row 3
        Label(class_studentinfo, text="D.O.B:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_dob, width=20, font=("times new roman", 12)).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        Label(class_studentinfo, text="Phone No:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_mobilenumber, width=20, font=("times new roman", 12)).grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Row 4
        Label(class_studentinfo, text="Address:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=8, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_address, width=20, font=("times new roman", 12)).grid(row=3, column=1, padx=10, pady=8, sticky=W)

        Label(class_studentinfo, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=2, padx=10, pady=8, sticky=W)
        ttk.Entry(class_studentinfo, textvariable=self.var_teachername, width=20, font=("times new roman", 12)).grid(row=3, column=3, padx=10, pady=8)
        # Row 5 - Gender
        Label(class_studentinfo, text="Gender:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=0, padx=10, pady=8, sticky=W)
        gender_combo = ttk.Combobox(class_studentinfo, textvariable=self.var_gender, font=("times new roman", 12), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=4, column=1, padx=10, pady=8, sticky=W)

        # Radio Buttons for photo sample
        Radiobutton(class_studentinfo, text="Take Photo Sample", variable=self.var_photosamplestatus, value="Yes", bg="white",
                    font=("times new roman", 9)).grid(row=4, column=2, padx=10, sticky=W)
        Radiobutton(class_studentinfo, text="No Photo Sample", variable=self.var_photosamplestatus, value="No", bg="white",
                    font=("times new roman", 9)).grid(row=4, column=3, padx=10, sticky=W)

        # ---------------- Button Frame ----------------
        btn_frame = Frame(class_studentinfo, bd=2, relief=RIDGE, bg="darkgreen")
        btn_frame.place(x=5, y=220, width=660, height=40)  # adjusted position

        Button(btn_frame, text="Save", command=self.add_data, width=6, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0, padx=3, pady=1)
        Button(btn_frame, text="Update",command=self.updatedata, width=6, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=0, column=1, padx=3, pady=1)
        Button(btn_frame, text="Delete",command=self.deletedata, width=6, font=("times new roman", 13, "bold"), bg="red", fg="white").grid(row=0, column=2, padx=3, pady=1)
        Button(btn_frame, text="Reset", command=self.reset,width=6, font=("times new roman", 13, "bold"), bg="purple", fg="white").grid(row=0, column=3, padx=3, pady=1)
        Button(btn_frame, text="Take Photo Sample",command=self.gen_dataset, width=16, font=("times new roman", 13, "bold"), bg="orange", fg="white").grid(row=0, column=4, padx=3, pady=1)
        Button(btn_frame, text="Update Photo Sample", width=16, font=("times new roman", 13, "bold"), bg="darkblue", fg="white").grid(row=0, column=5, padx=2, pady=1)

        # ---------------- Right Frame ----------------
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Records",
                                 font=("times new roman", 12, "bold"), bg="white")
        right_frame.place(x=720, y=5, width=650, height=530)

        rightimg = Image.open(r"C:\all\Face Recognition System\smsimages\rightframe.jpg").resize((600,130), Image.Resampling.LANCZOS)
        self.rightimg = ImageTk.PhotoImage(rightimg)
        Label(right_frame, image=self.rightimg, bd=2).place(x=0, y=0, width=550, height=80)

        # ---------------- Search Frame ----------------
        searchframe = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        searchframe.place(x=5, y=90, width=680, height=70)

        Label(searchframe, text="Search By:", font=("times new roman", 12, "bold"), fg="white", bg="red").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        search_combo = ttk.Combobox(searchframe, width=15, font=("times new roman", 12), state="readonly")
        search_combo["values"] = ("Select", "Roll No", "Student ID", "Student Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        ttk.Entry(searchframe, width=15, font=("times new roman",13,"bold")).grid(row=0,column=2,padx=10)
        Button(searchframe, text="Search", bg="white", font=("times new roman",10,"bold")).grid(row=0,column=3)
        Button(searchframe, text="Show All", width=6, font=("times new roman",10,"bold"), bg="blue", fg="white").grid(row=0, column=4,padx=10)

        # ---------------- Table Frame ----------------
        tableframe = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        tableframe.place(x=5, y=170, width=520, height=270)

        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.student_table = ttk.Treeview(tableframe, columns=("S_ID","S_Name","Roll_No","department","course","year","sem",
                                                                "section","gender","dob","address","mobilenumber","emailid","teachername",
                                                                "photosamplestatus"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # ---------------- Table Headings ----------------
        self.student_table.heading("S_ID", text="Student ID")
        self.student_table.heading("S_Name", text="Student Name")
        self.student_table.heading("Roll_No", text="Roll Number")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date Of Birth")       
        self.student_table.heading("address", text="Address")
        self.student_table.heading("mobilenumber", text="Mobile Number")
        self.student_table.heading("emailid", text="Email ID")
        self.student_table.heading("photosamplestatus", text="Photo Sample Status")
        self.student_table.heading("teachername", text="Teacher")

        # ---------------- Table Column Widths ----------------
        for col in self.student_table["columns"]:
            if(col=="emailid" or col=="address"):
                self.student_table.column(col,width=150)
            else:
                self.student_table.column(col, width=120)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.getcursor)
        self.fetchdata()

    # ---------------- Add Data Function ----------------
    def add_data(self):
        if  self.var_S_Name.get() == "" or self.var_Roll_No.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="raj@9125",
                    database="face_recognition_system"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO students 
                    (S_ID, S_Name, Roll_No, department, course, year, sem, section, gender,
                     mobilenumber, emailid, photosamplestatus, address, dob, teachername)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.var_S_ID.get(),
                    self.var_S_Name.get(),
                    self.var_Roll_No.get(),
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_section.get(),
                    self.var_gender.get(),
                    self.var_mobilenumber.get(),
                    self.var_emailid.get(),
                    self.var_photosamplestatus.get(),
                    self.var_address.get(),
                    self.var_dob.get(),
                    self.var_teachername.get()
                ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Database Error", f"Error due to: {str(e)}", parent=self.root)

    def fetchdata(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="raj@9125",
                    database="face_recognition_system"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def getcursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_S_ID.set(data[0]),
        self.var_S_Name.set(data[1]),
        self.var_Roll_No.set(data[2]),
        self.var_department.set(data[3]),
        self.var_course.set(data[4]),
        self.var_year.set(data[5]),
        self.var_sem.set(data[6]),
        self.var_section.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_mobilenumber.set(data[11]),
        self.var_emailid.set(data[12]),
        self.var_teachername.set(data[13]),
        self.var_photosamplestatus.set(data[14]),
    
    def updatedata(self):
        if  self.var_S_Name.get() == "" or self.var_Roll_No.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if(update>0):
                    conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="raj@9125",
                    database="face_recognition_system"
                )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE students SET
                            S_Name=%s,
                            Roll_No=%s,
                            department=%s,
                            course=%s,
                            year=%s,
                            sem=%s,
                            section=%s,
                            gender=%s,
                            dob=%s,                            
                            address=%s,
                            mobilenumber=%s,
                            emailid=%s,
                            teachername=%s,
                            photosamplestatus=%s
                        WHERE S_ID=%s
                    """, (
                        self.var_S_Name.get(),
                        self.var_Roll_No.get(),
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_mobilenumber.get(),
                        self.var_emailid.get(),
                        self.var_teachername.get(),
                        self.var_photosamplestatus.get(),
                        self.var_S_ID.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
                conn.commit()
                self.fetchdata()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    def deletedata(self):
        if self.var_S_ID=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("delete","Do You Want to Delete Student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="raj@9125",
                    database="face_recognition_system"
                )
                    my_cursor = conn.cursor()
                    sql="delete from students where S_ID=%s"
                    val=(self.var_S_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.reset()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success","Successfully Deleted Student details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    def reset(self):
        reset=messagebox.askyesno("Reset","Do You want to reset all fill data")
        if reset>0:
            self.var_S_ID.set(""),
            self.var_S_Name.set(""),
            self.var_Roll_No.set(""),
            self.var_department.set("Select Department"),
            self.var_course.set("Select Course"),
            self.var_year.set("Select Year"),
            self.var_sem.set("Select Semester"),
            self.var_section.set("Select Section"),
            self.var_gender.set("Select Gender"),
            self.var_dob.set(""),
            self.var_address.set(""),
            self.var_mobilenumber.set(""),
            self.var_emailid.set(""),
            self.var_teachername.set(""),
            self.var_photosamplestatus.set("")
        else:
            if not reset:
                return
            
        # =================Generate data set or take photo samples====
   
    def gen_dataset(self):
        if self.var_S_Name.get() == "" or self.var_Roll_No.get() == "":
                messagebox.showerror("Error", "All fields are required!", parent=self.root)
                return
        else:
            try:
                # Connect to MySQL and update student record
                conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="raj@9125",
                            database="face_recognition_system"
                        )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                            UPDATE students SET
                                S_Name=%s,
                                Roll_No=%s,
                                department=%s,
                                course=%s,
                                year=%s,
                                sem=%s,
                                section=%s,
                                gender=%s,
                                dob=%s,
                                address=%s,
                                mobilenumber=%s,
                                emailid=%s,
                                teachername=%s,
                                photosamplestatus=%s
                            WHERE S_ID=%s
                        """, (
                            self.var_S_Name.get(),
                            self.var_Roll_No.get(),
                            self.var_department.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_section.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_address.get(),
                            self.var_mobilenumber.get(),
                            self.var_emailid.get(),
                            self.var_teachername.get(),
                            self.var_photosamplestatus.get(),
                            self.var_S_ID.get()
                        ))
                conn.commit()
                self.fetchdata()
                conn.close()

                        # Ensure data directory exists
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                                return img[y:y + h, x:x + w]
                    return None
                
                # print(self.var_cam.get())
                

                cap = cv2.VideoCapture(0) #local camera
                img_id = 0

                        # Zoom parameters
                zoom_factor = 1.0
                zoom_direction = 1
                zoom_step = 0.01
                min_zoom = 0.1
                max_zoom = 0.3

                while True:
                    ret, myframe = cap.read()
                    face_raw = face_cropped(myframe)
                    if face_raw is not None:
                        h, w = face_raw.shape[:2]
                        center_x, center_y = w // 2, h // 2
                        new_w, new_h = int(w * zoom_factor), int(h * zoom_factor)
                        x1 = max(center_x - new_w // 2, 0)
                        y1 = max(center_y - new_h // 2, 0)
                        x2 = min(center_x + new_w // 2, w)
                        y2 = min(center_y + new_h // 2, h)
                        zoomed_face = face_raw[y1:y2, x1:x2]
                        face = cv2.resize(zoomed_face, (250, 250))

                                # Update zoom factor
                        zoom_factor += zoom_direction * zoom_step
                        if zoom_factor >= max_zoom or zoom_factor <= min_zoom:
                            zoom_direction *= -1

                        img_id += 1
                        file_path = f"data/user.{self.var_S_ID.get()}.{img_id}.jpg"
                        cv2.imwrite(file_path, face)

                        cv2.putText(face, str(img_id), (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Auto Zoom Face Capture", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Dataset Completed Successfully!", parent=self.root)

            except Exception as e:
                try:
                    cap.release()
                    cv2.destroyAllWindows()
                except:
                    pass
                    messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)
        



if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.mainloop()
