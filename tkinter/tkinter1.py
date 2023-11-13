from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Sushant Tkinter 1")
icon = PhotoImage(file="#Coders (1).png")
window.iconphoto(True, icon)
window.config(background="white")
label = Label(text="INTRODUCTION",
              fg="yellow", bg="red",
              relief=SUNKEN, bd=10,
              padx=20, pady=20,
              image=icon, compound=BOTTOM
              )
entry = Entry(window, font=("Arial", 20), fg="yellow", bg="red", width=400)


def submit():
    username = entry.get()
    print("Thanks" + username)


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=BOTTOM)


def back_space():
    entry.delete(len(entry.get()) - 1, END)


back_Space = Button(window, text="BackSpace", command=back_space)


def delete():
    entry.delete(0, END)


delete = Button(window, text="Delete", command=delete)
label.pack()
entry.pack(side=TOP)
back_Space.pack(side=TOP)
delete.pack(side=TOP)
submit_button.pack(side=TOP)
window.mainloop()
