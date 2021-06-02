from tkinter import *
from tkinter import messagebox

myspace = Tk()
myspace.geometry("300x300")
myspace.title("Authentication")

heading = Label(myspace, text="Please enter login details")
heading.place(x=60,y=10)
username = Label(myspace, text="Username")
username.place(x=110,y=40)
username_entry = Entry(myspace)
username_entry.place(x=65,y=60)
password = Label(myspace, text="Password")
password.place(x=110,y=90)
password_entry = Entry(myspace, show="-")
password_entry.place(x=65,y=110)

def access():
    username = ["Joyce","Velaphi","Nombi","BraDakie"]
    password = ["10111","11111","12111","13111"]
    found = False

    for x1 in range(len(username)):
        if username_entry.get() == username[x1] and password_entry.get() == password[x1]:
            found = True
            if found == True:
                messagebox.showinfo("ALERT","Access Granted")
                myspace.destroy()
                import task_two
        else:
                messagebox.showinfo("ERROR","Access denied")

# Button
login_button = Button(myspace, text="Login", bg="skyblue", command=access)
login_button.place(x=110,y=150)

myspace.mainloop()