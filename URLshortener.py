import pyshorteners
import pyperclip
from tkinter import *




win = Tk()
win.geometry("500x300")
win.title("URL Shortener")
win.configure(bg="white")




Label(win,text="Enter Your URL",font="verdana 15 bold",bg="white",fg="purple").pack()

def urlshortener():
    url = entry1.get()
    url_short = pyshorteners.Shortener()
    entry2.insert(END,url_short.tinyurl.short(url))




entry1 = Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)

Button(win,text="Short link",font="impack 17 bold",bg="Red",fg="white",width=14,command=urlshortener).pack()


entry2 = Entry(win,font="impack 16 bold",width=24,bd=0)
entry2.pack(pady=30)

mainloop()
