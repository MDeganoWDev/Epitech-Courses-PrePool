############################ EXERCICE 01 ###############################

# from tkinter import *

# def caps() :
#     print(entry.get().upper())

# main = Tk()

# labelFrame = LabelFrame(main, text="I'm the LabelFrame")
# labelFrame.pack(fill='both', expand="yes")

# entry = Entry(labelFrame, text="I'm the entry")
# entry.pack()

# button = Button(labelFrame, text='Accept',fg="white", bg="red", command=caps)
# button.pack()

# main.mainloop()

############################ EXERCICE 02 ###############################

# from tkinter import *
# from PIL import Image, ImageTk

# main = Tk()
# main.geometry("750x250")

# labelFrame = LabelFrame(main)
# labelFrame.pack(fill='both', expand="yes")

# canvas = Canvas(labelFrame, width=600, height=400)
# canvas.pack()

# img = ImageTk.PhotoImage(Image.open(r"C:\Users\DMatt\Images\PP.jpg"))
# canvas.create_image(10, 10, anchor=NW, image=img)

# main.mainloop()

############################ EXERCICE 03 ###############################

# from tkinter import *

# main = Tk()

# canvas = Canvas(main)
# canvas.pack()

# canvas.create_oval(75, 50, 125, 100, width=4, fill="green")
# canvas.create_line(100, 100, 100, 250, width=4, fill="green")
# canvas.create_line(100, 125, 50, 175, width=4, fill="red")
# canvas.create_line(100, 125, 150, 175, width=4, fill="blue")
# canvas.create_line(100, 250, 50, 300, width=4, fill="purple")
# canvas.create_line(100, 250, 150, 300, width=4, fill="yellow")

# label = Label(main, text="Hello world")
# label.place(x=10,y=25)

# main.mainloop()

############################ EXERCICE 04 ###############################

from tkinter import *
import time

main = Tk()
main.geometry("500x500")

canvas = Canvas(main)
canvas.pack(fill="both")

canvas.create_oval(75, 50, 125, 100, width=4, fill="green")
canvas.create_line(100, 100, 100, 250, width=4, fill="green")
canvas.create_line(100, 125, 50, 175, width=4, fill="red")

canvas.create_line(100, 125, 125, 150, width=4, fill="blue")

canvas.create_line(100, 250, 50, 300, width=4, fill="purple")
canvas.create_line(100, 250, 150, 300, width=4, fill="yellow")

def arm(i = 0) :
    canvas.create_line(125, 150, 125+i, 100+i, width=4, fill="blue")
    for i in range(25) :
        main.after(150, arm(i+1))
    for i in range(25) :
        main.after(150, arm(i-1))
    arm()
       
        
    

arm()
label = Label(main, text="Hello world")
label.place(x=10,y=25)


main.mainloop()

