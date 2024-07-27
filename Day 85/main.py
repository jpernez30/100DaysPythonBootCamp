import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        self.watermark_text = tk.Entry(root, width=50)
        self.watermark_text.pack(pady=10)
        self.watermark_text.insert(0, "Enter watermark text here")

        self.add_watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.pack(pady=20)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=20)

        self.image_path = None

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.display_image(self.image_path)

    def display_image(self, path):
        image = Image.open(path)
        image.thumbnail((300, 300))
        image = image.convert("RGB")
        self.image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.image)

    def add_watermark(self):
        if self.image_path and self.watermark_text.get():
            image = Image.open(self.image_path)
            watermark_text = self.watermark_text.get()

            width, height = image.size
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 36)
            text_width, text_height = draw.textsize(watermark_text, font)

            x = width - text_width - 10
            y = height - text_height - 10

            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                image.save(save_path)

                self.display_image(save_path)
                tk.messagebox.showinfo("Success", "Watermark added and image saved!")

if __name__ == "__main__":
    from PIL import ImageTk
    import tkinter.messagebox

    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()