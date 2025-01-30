import tkinter
from tkinter import ttk, messagebox

screen = tkinter.Tk()
screen.title("MyApp")
screen.config(background="black")
screen.geometry("400x500")

"""lbl1 = tkinter.Label(text="Firstname:").pack()
lbl2 = tkinter.Label(text="Lastname:").pack()"""

"""lbl1 = tkinter.Label(text="Firstname:").place(x=0, y=0)
lbl2 = tkinter.Label(text="Lastname:").place(x=0, y=30)"""

lbl1 = tkinter.Label(
    text="Firstname:", bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=0, column=0, sticky="w")
lbl2 = tkinter.Label(
    text="Lastname:", bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=1, column=0, sticky="w")

txt1 = tkinter.Entry(font="Ebrima 12 bold", fg="red").grid(row=0, column=1, sticky="w")
txt2 = tkinter.Entry(font="Ebrima 12 bold", fg="red").grid(row=1, column=1, sticky="w")

male = tkinter.Radiobutton(
    text="Male", value=0, bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=2, column=0, sticky="w")
female = tkinter.Radiobutton(
    text="Female", value=1, bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=2, column=1, sticky="w")

ch1 = tkinter.Checkbutton(
    text="Gujarati", bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=3, column=0, sticky="w")
ch2 = tkinter.Checkbutton(
    text="Hindi", bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=4, column=0, sticky="w")
ch3 = tkinter.Checkbutton(
    text="English", bg="black", fg="orange", font="Ebrima 15 bold"
).grid(row=5, column=0, sticky="w")

city = ["Rajkot", "Ahmedabda", "Baroda", "Jamnagar", "Bhavnagar"]
ttk.Combobox(values=city).grid(row=6, column=0, sticky="w")


def btnclick():
    # print("Button Clicked!")
    # messagebox.showerror(title="Error", message="Something went wrong...!")
    # messagebox.showinfo(title="Success", message="Your account has been created!")
    messagebox.showwarning(title="Warning", message="Your disk is full!")


tkinter.Button(
    text="Submit", bg="black", fg="orange", font="Ebrima 15 bold", command=btnclick
).place(x=170, y=270)
screen.mainloop()
