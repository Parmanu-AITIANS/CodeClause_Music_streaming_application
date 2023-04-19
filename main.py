import  pywhatkit
from tkinter import *
win=Tk()
win.geometry("500x300")

#button function
def play():
   song= e.get()
   pywhatkit.playonyt(song)

#Heading
Label(win,text="Online Music Player",font="impack 20 bold",bg="red",fg="white").pack(fill="x")
Label(win,text="Enter the song",font="impack 15 bold",bg="black",fg="white").pack(pady=39)
#Entry Box
e=Entry(win,bd=4,width=20,bg="grey")
e.place(x=160,y=200)

#button
Button(win,text="PLAY",font="chillar 14 bold",bg="black",fg="white",cursor="hand2",command=play).place(x=175,y=230) 


mainloop()



