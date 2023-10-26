from tkinter import StringVar, TOP
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_ALL
from PyPDF2 import PdfReader
import customtkinter as ctk
import re

class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

ctk.set_appearance_mode("dark")

def get_path(event):
    pathLabel.configure(text=event.data)

def extract_and_display_dates(pdf_path):
    dates = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'  # A basic date pattern, modify as needed
        date_regex = re.compile(date_pattern)

        for page_num in range(pdf_reader.pages):
            page_text = pdf_reader.getPage(page_num).extractText()
            dates.extend(date_regex.findall(page_text))

    # Handle the extracted dates as needed (e.g., display them)

root = Tk()
root.geometry("750x360")
root.title("Get file path")

nameVar = StringVar()

entryWidget = ctk.CTkEntry(root)
entryWidget.pack(side=TOP, padx=5, pady=5)

pathLabel = ctk.CTkLabel(root, text="Drag and drop file in the entry box")
pathLabel.pack(side=TOP, padx=5, pady=5)

entryWidget.drop_target_register(DND_ALL)
entryWidget.dnd_bind("<<Drop>>", get_path)

# Button to trigger PDF processing
button = ctk.CTkButton(root, text="Read my PDF", command=lambda: extract_and_display_dates(pathLabel.cget("text")))
button.pack(side=tk.TOP, padx=5, pady=5)

root.mainloop()
