import tkinter
import customtkinter





root = tkinter.Tk()
root.geometry("780x360")
root.title("PDF reader")
customtkinter.set_appearance_mode("Dark")

fileInput = customtkinter.CTkInputDialog
fileInput.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=root, text="Run pdf file")()
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



root.mainloop()