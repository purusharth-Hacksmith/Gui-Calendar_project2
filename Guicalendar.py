from tkinter import *
from tkcalendar import *
root= Tk()
root.title()
root.geometry("600x400")
root.resizable(False,False)
root.config(bg="lightblue")

mycal= Calendar(root,setmode="day",date_pattern='d/m/yyyy')
mycal.pack(pady=20)


def get_info():
    myDate=mycal.get_date()
    current_date["text"]=myDate

Button(root,text="Submit",command=get_info,fg="blue",bg="lightGrey").pack(pady=7)
current_date=Label(root,text='',font=('Arial,18'),fg='black',bg="green")
current_date.pack(pady=5)

root.mainloop()