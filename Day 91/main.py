import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import StringVar
from PyPDF2 import PdfReader
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return text

def text_to_speech(text, output_path):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)
        messagebox.showinfo("Success", f"Speech saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while converting text to speech: {e}")

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_path_var.set(file_path)

def convert_pdf_to_speech():
    pdf_path = pdf_path_var.get()
    if not pdf_path:
        messagebox.showwarning("Warning", "Please select a PDF file.")
        return

    audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not audio_path:
        return

    text = pdf_to_text(pdf_path)
    if text:
        text_to_speech(text, audio_path)
    else:
        messagebox.showwarning("Warning", "No text extracted from the PDF.")

# GUI Setup
root = tk.Tk()
root.title("PDF to Speech Converter")
root.configure(bg='#1e3c72')
pdf_path_var = StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)
frame.configure(bg='#1e3c72')

tk.Label(frame, text="PDF File:").grid(row=0, column=0, sticky="e")
tk.Entry(frame, textvariable=pdf_path_var, width=50).grid(row=0, column=1)
tk.Button(frame, text="Browse", command=select_pdf_file).grid(row=0, column=2)

tk.Button(frame, text="Convert to Speech", command=convert_pdf_to_speech).grid(row=1, columnspan=3, pady=10)

root.mainloop()
