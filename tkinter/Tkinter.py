'''basics of tkinter module'''
# from tkinter import * # just called kinter
#
# window = Tk() # instantiate an instance of a window
# window.geometry("420x540")
# window.title("Sushant Code For Tkinter")
#
# icon=PhotoImage(file="#Coders (1).png")
#
# window.iconphoto(True,icon)
# window.config(background="black")
# window.mainloop()# place window on computer screen , listen for events

'''GO FURTHER Now-Labels'''
# from tkinter import *
# #label=an area that area holds text and/or an image within a window
# window=Tk()
# photo=PhotoImage(file="#Coders (1).png")
# label=Label(window,text="Hello World!",font=("Arial",40,"bold"),
#             fg="green",bg="black",
#             relief=SUNKEN,bd=10,
#             padx=20,pady=20,
#             image=photo,compound="bottom")# we also used # value of colours
# label.pack()
# # label.place(x=0,y=0)
#
# window.mainloop()
'''Now Time's For -Button'''
# from tkinter import *
# count=0
# def click():
#     print("You Clicked the button!")
#     global count
#     count+=1
#     print(count)
#
#
# window=Tk()
# photo=PhotoImage(file="download.png")
# button=Button(window,text="Click Me",
#               command=click,
#               font=("Comic Sans",30),
#               fg="Green",bg="Red",
#               state=ACTIVE,
#               image=photo,compound="bottom")
#
# window.mainloop()

'''Time For Entry Widget'''
# from tkinter import *
#
# def submit():
#     username=entry.get()
#     print("Hello"+username)
# def delete():
#     entry.delete(0,END)#provides a range
# def backspace():
#     entry.delete(len(entry.get())-1,END)
#
# window=Tk()
# entry=Entry(window,font=("Arial",50),fg="green",bg="black",show="*")
# entry.pack(side=LEFT)
# submit_button=Button(window,text="Submit",command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button=Button(window,text="Delete",command=delete)
# delete_button.pack(side=RIGHT)
# backspace_button=Button(window,text="Backspace",command=backspace)
# backspace_button.pack(side=RIGHT)
#
#
# window.mainloop()

'''Check Buttons Time'''
# from tkinter import *
# def display():
#     if(x.get()==1):
#         print("You agree!")
#     else:
#         print("You disagree!")
# window=Tk()
# x=IntVar()
# icon=PhotoImage(file="#Coders (1).png")
#
#
# check_button=Checkbutton(window,
#                          text="I agree to something",
#                          variable=x,
#                          onvalue=1,
#                          offvalue=0
#                          ,command=display,
#                          font=("Arial",20),
#                          fg="#00FF00",
#                          bg="black",
#                          activeforeground="#00FF00",
#                          activebackground="black",
#                          padx=25,
#                          pady=10,
#                          image=icon,
#                          compound="left")
# check_button.pack()
#
# window.mainloop()

'''Radio Buttons'''
from tkinter import *

food = ["Pizza", "Hamburger", "samosa"]


def order():
    if (x.get() == 0):
        print("You Ordered Pizza")
    elif (x.get() == 1):
        print("You ordered a hamburger")
    elif (x.get() == 2):
        print("You ordered a samosa")
    else:
        print('huh?')


window = Tk()
pizzaimage = PhotoImage(file="pizzawala.png")
hamburgerimage = PhotoImage(file="burger.png")
samosaimage = PhotoImage(file="Samosa.png")
foodImage = [pizzaimage, hamburgerimage, samosaimage]

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index],
                              variable=x, value=index, padx=25,
                              font=("Impact", 30), image=foodImage[index],
                              compound="left",
                              indicatoron=0,  # eliminate circle indicators
                              width=375,
                              command=order)

    radiobutton.pack(anchor=W)

window.mainloop()
