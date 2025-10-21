from tkinter import *
from PIL import Image, ImageTk
from tkinter import font, ttk, messagebox
import os
import csv
from tkinter import filedialog


mydata=[]
class ManageAttendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Manage Attendance")

        self.var_S_ID=IntVar()
        self.var_Roll_No=StringVar()
        self.var_S_Name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance_status=StringVar()
        self.var_section=StringVar()

        # ---------------- Top Images ----------------
        img1 = Image.open(r"C:\all\Face Recognition System\smsimages\st1.jpg").resize((500, 130), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.img1).place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\all\Face Recognition System\smsimages\st2.jpg").resize((500, 130), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.img2).place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r"C:\all\Face Recognition System\smsimages\st3.jpg").resize((530, 130), Image.Resampling.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.img3).place(x=1000, y=0, width=530, height=130)

        # ---------------- Background ----------------
        bgimg = Image.open(r"C:\all\Face Recognition System\college_images\bgimage.jpg").resize((1530, 660), Image.Resampling.LANCZOS)
        self.bgimg = ImageTk.PhotoImage(bgimg)
        Label(self.root, image=self.bgimg).place(x=0, y=130, width=1530, height=660)



        # ---------------- Title ----------------
        Label(
            self.root,
            text="Manage Student Attendance",
            font=("Times New Roman", 24, "bold"),
            bg="#1e90ff",
            fg="white",
            bd=3,
            relief=RIDGE
        ).place(x=0, y=130, width=1530, height=50)


        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=40, y=200, width=1200, height=500)

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Manage Student Attendance",
                                font=("times new roman", 12, "bold"), bg="white")
        left_frame.place(x=20, y=5, width=640, height=560)

        leftbgframe=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        leftbgframe.place(x=0,y=0,width=620,height=130)

        llf=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        llf.place(x=0,y=140,width=630,height=460)

        imglf = Image.open(r"C:\all\Face Recognition System\smsimages\st1.jpg").resize((560,120), Image.Resampling.LANCZOS)
        self.imglf = ImageTk.PhotoImage(imglf)
        Label(leftbgframe, image=self.imglf).place(x=10, y=0, width=610, height=120)


        Label(llf, text="Student ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(llf, width=18,textvariable=self.var_S_ID,   font=("times new roman", 12,"bold")).grid(row=0, column=1, pady=10, sticky=W)

        Label(llf, text="Roll No:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(llf, width=18, textvariable=self.var_Roll_No,font=("times new roman", 12,"bold")).grid(row=0, column=3, pady=10, sticky=W)

        Label(llf, text="Name :", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(llf, width=18,textvariable=self.var_S_Name, font=("times new roman", 12,"bold")).grid(row=1, column=1, pady=10, sticky=W)
        
        Label(llf, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        dep_combo = ttk.Combobox(llf, textvariable=self.var_department,width=18, font=("times new roman", 12), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        Label(llf, text="Time :", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(llf, width=18,textvariable=self.var_time, font=("times new roman", 12,"bold")).grid(row=2, column=1, pady=10, sticky=W)

        Label(llf, text="Date :", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(llf, width=18,textvariable=self.var_date, font=("times new roman", 12,"bold")).grid(row=2, column=3, pady=10, sticky=W)


        Label(llf, text="Attendance Status :", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=8, sticky=W)
        status = ttk.Combobox(llf,width=15,textvariable=self.var_attendance_status, font=("times new roman", 12), state="readonly")
        status["values"] = ("Status", "Present", "Absent")
        status.current(0)
        status.grid(row=3, column=1, padx=10, pady=8, sticky=W)


        Label(llf, text="Section:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=2, padx=10, pady=5, sticky=W)
        section_combo = ttk.Combobox(llf,width=15,textvariable=self.var_section, font=("times new roman", 12), state="readonly")
        section_combo["values"] = ("Select Section", "A", "B", "C")
        section_combo.current(0)
        section_combo.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        btn_frame = Frame(llf, bd=2, relief=RIDGE, bg="darkgreen")
        btn_frame.place(x=5, y=200, width=660, height=40)  # adjusted position


        Button(btn_frame, text="Import csv",command=self.importcsv, width=13, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0, padx=3, pady=1)
        Button(btn_frame, text="Export csv",command=self.exportcsv, width=13, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=0, column=1, padx=3, pady=1)
        Button(btn_frame, text="Update",command=self.updatedata, width=13, font=("times new roman", 13, "bold"), bg="red", fg="white").grid(row=0, column=2, padx=3, pady=1)
        Button(btn_frame, text="Reset",command=self.reset,width=13, font=("times new roman", 13, "bold"), bg="purple", fg="white").grid(row=0, column=3, padx=3, pady=1)



        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"), bg="white")
        right_frame.place(x=650, y=5, width=550, height=530)


        tableframe = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        tableframe.place(x=5, y=0, width=520, height=380)

        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(tableframe, columns=("S_ID","S_Name","Roll_No","department","section","time","date","attendance_status"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("S_ID",text="Student_ID")
        self.AttendanceReportTable.heading("S_Name",text="Name")
        self.AttendanceReportTable.heading("Roll_No",text="Roll No")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("section",text="Section")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance_status",text="Status")



      


        
        for col in self.AttendanceReportTable["columns"]:
                self.AttendanceReportTable.column(col,width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
             self.AttendanceReportTable.insert("",END,value=i)

    def importcsv(self):
         global mydata
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
         with open(fln,encoding="utf-8-sig") as myfile:
              csvread=csv.reader(myfile,delimiter=",")
              for i in csvread:
                   mydata.append(i)
              self.fetchData(mydata)


    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                myfile=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    myfile.writerow(i)
                messagebox.showinfo("Success","Your Data has been exported to " + os.path.basename(fln)+"successfully")
        except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]


        self.var_S_ID.set(rows[0])
        self.var_S_Name.set(rows[1])
        self.var_Roll_No.set(rows[2])
        self.var_department.set(rows[3])
        self.var_section.set(rows[4])
        self.var_time.set(rows[5])
        self.var_date.set(rows[6])
        self.var_attendance_status.set(rows[7])

    def reset(self):
        reset=messagebox.askyesno("Reset","Do You want to reset all fill data")
        if reset>0:
            self.var_S_ID.set(""),
            self.var_S_Name.set(""),
            self.var_Roll_No.set(""),
            self.var_department.set("Select Department"),
            self.var_section.set("Select Section"),
            self.var_time.set(""),
            self.var_date.set("")
            self.var_attendance_status.set("Status")      
           
        else:
            if not reset:
                return
            
    def updatedata(self):
          if  self.var_S_Name.get() == "" or self.var_Roll_No.get() == "" or self.var_attendance_status=="" or self.var_section=="":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
          else:
               try:
                    selected = self.AttendanceReportTable.focus()
                    if not selected:
                        messagebox.showerror("Error", "Please select a record to update.", parent=self.root)
                        return

                    updated_row = (
                        self.var_S_ID.get(),
                        self.var_S_Name.get(),
                        self.var_Roll_No.get(),
                        self.var_department.get(),
                        self.var_section.get(),
                        self.var_time.get(),
                        self.var_date.get(),
                        self.var_attendance_status.get()
                    )
                    self.AttendanceReportTable.item(selected,values=updated_row)
                    messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)    
               except Exception as e:
                 messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)



      

if __name__ == "__main__":
    root = Tk()
    obj = ManageAttendance(root)
    root.mainloop()
