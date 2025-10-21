from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import smtplib
from email.message import EmailMessage

class HelpDesk:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Help Desk - Shift Into Success")
        self.root.configure(bg="#0d0d0d")

        # ---------- Header ----------
        Label(
            self.root,
            text="🛠️ Help Desk – How Can We Assist You?",
            font=("Poppins SemiBold", 32, "bold"),
            bg="#0d0d0d",
            fg="#00FFF0",
            pady=20
        ).pack(anchor=N)

        # ---------- Form Frame ----------
        form_frame = Frame(self.root, bg="#1a1a1a", bd=2, relief=SOLID)
        form_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=500)

        # ---------- Neon Border ----------
        border_canvas = Canvas(form_frame, width=600, height=500, bg="#0d0d0d", highlightthickness=0)
        border_canvas.place(x=0, y=0)
        border_canvas.create_rectangle(10, 10, 590, 490, outline="#00FFF0", width=3)

        # ---------- Form Fields ----------
        Label(form_frame, text="Name", font=("Poppins", 14), bg="#1a1a1a", fg="#DDDDDD").place(x=40, y=40)
        self.name_entry = Entry(form_frame, font=("Poppins", 12), bg="#0d0d0d", fg="#00FFF0", insertbackground="#00FFF0")
        self.name_entry.place(x=40, y=70, width=520)

        Label(form_frame, text="Email", font=("Poppins", 14), bg="#1a1a1a", fg="#DDDDDD").place(x=40, y=120)
        self.email_entry = Entry(form_frame, font=("Poppins", 12), bg="#0d0d0d", fg="#00FFF0", insertbackground="#00FFF0")
        self.email_entry.place(x=40, y=150, width=520)

        Label(form_frame, text="Query Type", font=("Poppins", 14), bg="#1a1a1a", fg="#DDDDDD").place(x=40, y=200)
        self.query_type = StringVar()
        self.query_type.set("General")
        OptionMenu(form_frame, self.query_type, "General", "Technical", "Feedback", "Bug Report").place(x=40, y=230, width=520)

        Label(form_frame, text="Message", font=("Poppins", 14), bg="#1a1a1a", fg="#DDDDDD").place(x=40, y=280)
        self.message_box = Text(form_frame, font=("Poppins", 12), bg="#0d0d0d", fg="#00FFF0", insertbackground="#00FFF0")
        self.message_box.place(x=40, y=310, width=520, height=100)

        # ---------- Submit Button ----------
        Button(form_frame, text="Submit", font=("Poppins", 13, "bold"), bg="#00FFF0", fg="#0d0d0d",
               command=self.submit_form).place(x=250, y=430)

    def send_email(self, name, email, query, message):
        msg = EmailMessage()
        msg['Subject'] = f"New Help Desk Query: {query}"
        msg['From'] = "rm2739159@gmail.com"
        msg['To'] = "rm2739159@gmail.com"
        msg.set_content(f"""
Name: {name}
Email: {email}
Query Type: {query}
Message:
{message}
        """)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("rm2739159@gmail.com", "nmkjhrhtnpbrzsvn")  # Your App Password
                smtp.send_message(msg)
            return True
        except Exception as e:
            print("Email Error:", e)
            return False

    def submit_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        query = self.query_type.get().strip()
        message = self.message_box.get("1.0", END).strip()

        if not name or not email or not query or not message:
            messagebox.showwarning("Incomplete", "Please fill out all fields.")
        else:
            if self.send_email(name, email, query, message):
                messagebox.showinfo("Submitted", "Thank you! Your query has been emailed.")
                self.name_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.query_type.set("General")
                self.message_box.delete("1.0", END)
            else:
                messagebox.showerror("Error", "Failed to send email. Please check your internet or credentials.")

if __name__ == "__main__":
    root = Tk()
    app = HelpDesk(root)
    root.mainloop()