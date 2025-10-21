from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import os

class Developer:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Developer Info - Shift Into Success")
        self.root.configure(bg="#0d0d0d")

        # ---------- Background with Gaussian Blur ----------
        bg_path = r"C:\all\Face Recognition System\college_images\bgimage.jpg"
        bg_img = Image.open(bg_path).resize((screen_width, screen_height))
        bg_img = bg_img.convert("RGB").filter(ImageFilter.GaussianBlur(4))
        self.photo_bg = ImageTk.PhotoImage(bg_img)
        Label(self.root, image=self.photo_bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ---------- Gradient Overlay ----------
        gradient = Image.new("RGBA", (screen_width, screen_height))
        draw = ImageDraw.Draw(gradient)
        for i in range(screen_height):
            draw.line((0, i, screen_width, i), fill=(0, 0, 0, int(i / 3)))
        self.gradient_photo = ImageTk.PhotoImage(gradient)
        Label(self.root, image=self.gradient_photo).place(x=0, y=0, relwidth=1, relheight=1)

        # ---------- Title ----------
        Label(
            self.root,
            text="💻 Developer Portfolio",
            font=("Poppins SemiBold", 38, "bold"),
            bg="#0d0d0d",
            fg="#00FFF0",
            pady=20
        ).pack(anchor=N)

        # ---------- Left Frame (Profile Card) ----------
        left_frame = Frame(self.root, bg="#0d0d0d")
        left_frame.place(x=screen_width * 0.05, y=screen_height * 0.2, width=screen_width * 0.4, height=screen_height * 0.6)

        card_canvas = Canvas(left_frame, width=screen_width * 0.4, height=screen_height * 0.6, bg="#0d0d0d", highlightthickness=0)
        card_canvas.pack()

        def round_rect(x1, y1, x2, y2, r=20, **kwargs):
            points = [
                x1 + r, y1,
                x2 - r, y1,
                x2, y1,
                x2, y1 + r,
                x2, y2 - r,
                x2, y2,
                x2 - r, y2,
                x1 + r, y2,
                x1, y2,
                x1, y2 - r,
                x1, y1 + r,
                x1, y1
            ]
            return card_canvas.create_polygon(points, smooth=True, **kwargs)

        # Neon Glow Border
        round_rect(5, 5, screen_width * 0.4 - 5, screen_height * 0.6 - 5, r=40, outline="#00FFF0", width=4)
        round_rect(15, 15, screen_width * 0.4 - 15, screen_height * 0.6 - 15, r=35, fill="#1a1a1a")

        # Developer Photo
        img_path = r"C:\all\Face Recognition System\college_images\raj.jpeg"
        img = Image.open(img_path).resize((180, 180)).convert("RGB")
        self.photo = ImageTk.PhotoImage(img)
        Label(card_canvas, image=self.photo, bg="#1a1a1a", bd=0).place(x=screen_width * 0.4 / 2 - 90, y=40)

        # Developer Info
        Label(card_canvas, text="Raj Singh", font=("Poppins SemiBold", 26, "bold"),
              bg="#1a1a1a", fg="#00FFF0").place(x=screen_width * 0.4 / 2 - 90, y=240)
        Label(card_canvas, text="B.Tech (IT), 3rd Year", font=("Poppins", 16),
              bg="#1a1a1a", fg="#E0E0E0").place(x=screen_width * 0.4 / 2 - 110, y=280)
        Label(card_canvas, text="ABES Engineering College", font=("Poppins", 16),
              bg="#1a1a1a", fg="#E0E0E0").place(x=screen_width * 0.4 / 2 - 130, y=310)
        Label(card_canvas, text="🚀 'Code. Create. Inspire.'", font=("Poppins Italic", 14),
              bg="#1a1a1a", fg="#A0A0A0").place(x=screen_width * 0.4 / 2 - 100, y=340)

        # ---------- Right Frame (About / Description) ----------
        right_frame = Frame(self.root, bg="#0d0d0d")
        right_frame.place(x=screen_width * 0.5, y=screen_height * 0.2, width=screen_width * 0.45, height=screen_height * 0.6)

        about_text = (
            "Hi, I'm Raj Singh — a passionate developer and AI enthusiast from ABES Engineering College.\n"
            "I love blending creativity with code, transforming ideas into digital reality.\n"
            "Currently exploring Face Recognition Systems, AI applications, and Spring Boot projects."
        )
        Label(right_frame, text=about_text, font=("Poppins", 13), bg="#0d0d0d", fg="#DDDDDD",
              justify=LEFT, wraplength=screen_width * 0.43).pack(anchor=NW, pady=20)

        disclaimer_text = (
            "⚠️ Disclaimer: This project is developed for educational and innovation purposes only.\n"
            "All resources used belong to their respective owners. Unauthorized commercial use is prohibited."
        )
        Label(right_frame, text=disclaimer_text, font=("Poppins", 11),
              bg="#0d0d0d", fg="#999999", justify=LEFT, wraplength=screen_width * 0.43).pack(anchor=NW, pady=20)

        # ---------- Footer ----------
        Label(
            self.root,
            text="© 2025 Raj Singh | Shift Into Success | Innovating with AI & Code 💡",
            font=("Poppins", 12, "italic"),
            bg="#0d0d0d", fg="#00FFF0", pady=10
        ).pack(side=BOTTOM, fill=X)

if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()