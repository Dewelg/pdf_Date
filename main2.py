import tkinter
import customtkinter
from tkinter import filedialog


root = tkinter.Tk()
root.geometry("780x360")
root.title("PDF reader")
customtkinter.set_appearance_mode("Dark")

fileInput = filedialog.askopenfile()

button = customtkinter.CTkButton(master=fileInput, text="Open file")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



root.mainloop()