import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_ALL
from PyPDF2 import PdfFileReader
import customtkinter as ctk
from customtkinter import filedialog

ctk.set_appearance_mode("dark")

def Upload_action():
    filename = filedialog.askopenfilename()
    print ('Selceted', filename)

def extract_and_display_dates(pdf_path, re):
    dates = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)

        date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'  # A basic date pattern, modify as needed
        date_regex = re.compile(date_pattern)

        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.getPage(page_num).extractText()
            dates.extend(date_regex.findall(page_text))

    # Handle the extracted dates as needed (e.g., display them)

#Size and Name on interface
root = Tk()
root = ctk.CTkFrame("750x360")
root.title("Get file path")

# Button to upload pdf
button = ctk.CTkButton(root, text="Upload PDF", command=Upload_action)
button.pack(side=tk.TOP, padx=5, pady=5)

#File pdf processor
File_pro = ctk.CTkButton(root, text="ReadPdf", command=extract_and_display_dates)
File_pro.pack()
root.mainloop()
