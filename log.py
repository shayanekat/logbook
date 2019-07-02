from tkinter import *
import os
import time

#=====BACKEND=====
#buttons functions
def creation():
    t = e1.get()
    c = open("logbook.txt","w")
    c.write(t+"\n\n")

def save():
    text = e2.get()
    f1 = open("logbook.txt","r")
    before = f1.read()
    f1.close()
    f2 = open("logbook.txt","w")
    f2.write(before)
    f2.write(time.strftime("%a %d %b %Y")+"\n")
    f2.write("================================\n")
    f2.write(text+"\n")
    f2.write("================================\n\n")
    f2.close()
    
    l4 = Label(I2,text="Enregistré".upper(),fg="red")
    l4.grid(row=0,column=1)

#other functions
def checkopened():
    #check if this app was ran today
    #input : none
    #output : none
    f1 = open("logbook.txt","r")
    before = f1.read()
    if time.strftime("%a %d %b %Y") in before:
        return False
    else:
        return True
    


#check existing file
L = os.listdir(".")
if "logbook.txt" not in L:
    #init file
    #=====FRONTEND=====
    I1 = Tk()
    I1.title("Logbook Creation")

    l1 = Label(I1,text="Entrer un titre : ")
    l1.grid(row=0,column=0)

    e1 = Entry(I1)
    e1.grid(row=0,column=1)

    b1 = Button(I1,text="Create",command=creation)
    b1.grid(row=1,column=1)
    
    I1.mainloop()

#update file
if checkopened():
    I2 = Tk()
    I2.title("LogBook")

    l2 = Label(I2,text=time.strftime("%a %d %b %Y"))
    l2.grid(row=0,column=0)

    l3 = Label(I2,text="Entrer ce que vous avez fait ici : ")
    l3.grid(row=1,column=0)

    e2 = Text(I2)
    e2.grid(row=1,column=1,rowspan=5)

    b2 = Button(I2,text="Enregistrer",command=save)
    b2.grid(row=7,column=1)

    I2.mainloop()