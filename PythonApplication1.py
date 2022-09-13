from tkinter import *
import tkinter.messagebox
import tkinter as tk

'''__________________________________________________________________________'''

var=Tk()
var.geometry('300x300+500+100')
var.resizable(False,False)
var.title('calculator')
var.config(background='skyblue')

ph = PhotoImage(file='calculator.png')
var.iconphoto(False,ph)


b=Frame(width=300,height=100,bg='skyblue')
b.place(y=200,x=0)

w=Frame(width=299,height=100,bg='skyblue')
w.place(x=1,y=1)


lab=Label(var,text='Eslam El_turky',fg='black',bg='red',font=('Helvetica',10,'bold'))
lab.place(x=199,y=10)
'''_____________________________________________________________'''
En=Entry(w)
En.place(x=70,y=80)

frame = tk.Frame(master=var, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=w, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tk.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)

'''______________________________________________________________________________________________'''

bt1=Button(var,text='Clear',bg='gray',cursor='dot',width='9',height='2',command=clear)
bt1.place(x=40,y=60)

bt1=Button(var,text='.',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick('.'))
bt1.place(x=120,y=59)

bt1=Button(var,text='=',bg='gray',cursor='dot',width='9',height='2',command=equal)
bt1.place(x=195,y=60)


bt1=Button(var , text='6',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(6))
bt1.place(x=40,y=155)

bt1=Button(var,text='7',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(7))
bt1.place(x=80,y=155)

bt1=Button(var,text='8',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(8))
bt1.place(x=120,y=155)

bt1=Button(var,text='9',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(9))
bt1.place(x=40,y=110)

bt1=Button(var,text='Power',fg='black',bg='gray',cursor='dot',width='9',height='2',command=lambda:myclick('**'))
bt1.place(x=80,y=110)

bt1=Button(var,text='Multi (*)',fg='black',bg='gray',cursor='dot',width='6',height='5',command=lambda:myclick('*'))
bt1.place(x=180,y=108)

bt1=Button(var,text='div (/)',fg='black',bg='gray',cursor='dot',width='6',height='5',command=lambda:myclick('/'))
bt1.place(x=240,y=108)

'''_________________________________________________________________________________________________________________'''


bt1=Button(b,text='0',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(0))
bt1.place(x=40,y=50)

bt1=Button(b,text='1',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(1))
bt1.place(x=80,y=50)

bt1=Button(b,text='2',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(2))
bt1.place(x=120,y=50)

bt1=Button(b,text='3',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(3))
bt1.place(x=40,y=2)

bt1=Button(b,text='4',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(4))
bt1.place(x=80,y=2)

bt1=Button(b,text='5',fg='black',bg='gray',cursor='dot',width='3',height='2',command=lambda:myclick(5))
bt1.place(x=120,y=2)
'''_____________________________________________________________________________________________________________'''

bt1=Button(b,text='Sum (+)',fg='black',bg='gray',cursor='dot',width='6',height='5',command=lambda:myclick('+'))
bt1.place(x=241,y=8)

bt1=Button(b,text='Sub (-)',fg='black',bg='gray',cursor='dot',width='6',height='5',command=lambda:myclick('-'))
bt1.place(x=180,y=8)
'''_____________________________________________________________________________________________________________________'''


var.mainloop()


