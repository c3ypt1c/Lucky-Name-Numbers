# WJEC Controlled Asessment
# Luck Name Numbers 2016 - 2017
# Python 3.3.2
# Import Time function
import tkinter

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Lucky Name Number Calculator")
#set the size.
root.geometry("600x400")

#add an instructions label.
instructions = tkinter.Label(root, text="Welcome to the lucky name number calculator", font=('Helvetica', 15))
instructions.pack()

#start the GUI
root.mainloop()
