from tkinter import *
from tkinter import messagebox

myspace = Tk()
myspace.geometry("300x300")
myspace.title("Exceptional Handling")

heading_label = Label(myspace, text="Please enter amount in your account")
heading_label.place(x=30,y=10)
amount_entry = Entry(myspace)
amount_entry.place(x=65,y=40)

def check():
    if amount_entry < 3000:
        messagebox.showinfo("ALERT", "Please add more funds")
    else:
        messagebox.showinfo("Alert","Thank you")
        import task

check_button = Button(myspace, text="Check Qualification",bg="skyblue", command=check)
check_button.place(x=70,y=70)

myspace.mainloop()