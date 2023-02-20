from tkinter import *
from tkinter import ttk #theme of tk  ttk = Module ใน tk
from tkinter import messagebox
import math
GUI = Tk()    
GUI.title('โปรแกรมคำนวณกระแส Motor')  
GUI.geometry('800x600')  
#########
L1 = Label(GUI,text='โปรแกรมคำนวณกระแส Motor ชนิด 3 Phase',font=('Andsana New',16),fg='Blue')
L1.place(x=30,y=20)

L2 = Label(GUI,text='Rate Power ',font=('Andsana New',12),fg='blue')
L2.place(x=30,y=80)
L3 = Label(GUI,text='Rate Voltage ',font=('Andsana New',12),fg='blue')
L3.place(x=30,y=120)
L3 = Label(GUI,text='Rate Pf ',font=('Andsana New',12),fg='blue')
L3.place(x=30,y=160)
L4 = Label(GUI,text='kW',font=('Andsana New',12),fg='blue')
L4.place(x=400,y=80)
L5 = Label(GUI,text='Volt',font=('Andsana New',12),fg='blue')
L5.place(x=400,y=120)
#########
ent1 = Entry(GUI,fg="blue", bg="yellow", width=25)
ent1.place(x=200,y=80)
ent2 = Entry(GUI,fg="blue", bg="yellow", width=25)
ent2.place(x=200,y=120)
ent3 = Entry(GUI,fg="blue", bg="yellow", width=25)
ent3.place(x=200,y=160)
#########
def Button1():
    Value1 = ent1.get()
    X1 = int(Value1) 
    Value2  = ent2.get()
    X2 = int(Value2) 
    Value3  = ent3.get()
    X3 = float(Value3)
    X4  = X1*1000/(1.732*X2*X3)    
    messagebox.showinfo('กระแส Motor คือ',X4 +'Amp')    
FB1 = Frame(GUI)  
FB1.place(x=450,y=80)

B1 = ttk.Button(FB1,text='คำนวนกระแส Motor',command=Button1)
B1.pack(ipadx=25,ipady=10)
GUI.mainloop()
