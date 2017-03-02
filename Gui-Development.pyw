# WJEC Controlled Asessment
# Luck Name Numbers 2016 - 2017
# Python 3.3.2/3.5.2
# Import Time function
import tkinter
# Import fun's functions as engine (for lagacy)
import fun as engine
#Function for setting the meaning of the name to a label.
def calc():
    global textbox, nametext;
    nametext.configure(text = "Your lucky name meaning is: " + engine.calc(textbox.get()));

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Lucky Name Number Calculator")
#set the size.
root.geometry("600x400")

#add an instructions label.
instructions = tkinter.Label(root, text="Welcome to the lucky name number calculator", font=('Helvetica', 15))
instructions.pack()

#Creates a textbox
textbox = tkinter.Entry(root);
textbox.pack();

#creates a submit button
submitbutton = tkinter.Button(root, text="Submit", command=calc )
submitbutton.pack();

#Add a lable for the program to print what the meaning is.
nametext = tkinter.Label(root);
nametext.pack();

#start the GUI
root.mainloop()
