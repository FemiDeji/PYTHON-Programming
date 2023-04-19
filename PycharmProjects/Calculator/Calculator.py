import tkinter
from tkinter import *

    #creating the text box
app = Tk()
app.title("Calculator")
app.geometry("291x360+70+120")
app.configure(bg="#17161b")
view = ""

    #function to get the text clicked and display it on the screen
def viw(show):
    global view
    view = view + show
    labe1_result.configure(text=view)

    #function to clear the expression displayed on the text box
def clear():
    global view
    view = ""
    labe1_result.configure(text=view)

    #evaluating the expresssions in the text box
def calculate():
     global view
     result = ""
     if view != "":
         try:
             result = eval(view)
         except:
             result = "error"
             view = ""
     labe1_result.configure(text=result)

    #creating the style of text diplayed in the text box
labe1_result = Label(app, text="", width=25, height=1, font=("Algerian", 30))
labe1_result.pack()

    #creating the buttons(no. of rows and cols)
Button(app, text="C", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda : clear()).place(x=10, y=60)
Button(app, text="/", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("/")).place(x=80, y=60)
Button(app, text="%", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("%")).place(x=150, y=60)
Button(app, text="*", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("*")).place(x=220, y=60)

Button(app, text="9", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("9")).place(x=10, y=121)
Button(app, text="8", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("8")).place(x=80, y=121)
Button(app, text="7", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("7")).place(x=150, y=121)
Button(app, text="-", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("-")).place(x=220, y=121)

Button(app, text="6", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("6")).place(x=10, y=182)
Button(app, text="5", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("5")).place(x=80, y=182)
Button(app, text="4", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("4")).place(x=150, y=182)
Button(app, text="+", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("+")).place(x=220, y=182)

Button(app, text="3", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("3")).place(x=10, y=243)
Button(app, text="2", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("2")).place(x=80, y=243)
Button(app, text="1", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("1")).place(x=150, y=243)
Button(app, text="0", width=7, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw("0")).place(x=10, y=304)

Button(app, text=".", width=3, height=1, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#2a2d35", command=lambda : viw(".")).place(x=150, y=304)
Button(app, text="=", width=3, height=3, font=("Algerian", 20,"bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda : calculate()).place(x=220, y=243)

    #to display the GUI
app.mainloop()