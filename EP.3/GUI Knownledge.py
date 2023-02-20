from tkinter import *
from tkinter import ttk #theme of tk  ttk = Module ใน tk
from tkinter import messagebox

GUI = Tk()     # หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')  #ชื่อโปรแกรม
GUI.geometry('500x400')   #ขนาดโปรแกรม



L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Andsana New',30),fg='green')
L1.place(x=30,y=20)




#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)   #.pack จะอยู่ Center  บวก x และ y

########################################
def Button2():
    text = 'ตอนนี้มีเงินอยู่ในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

    

FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=100,y=300)

B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)    #วางตาม location x และ y
########################################





GUI.mainloop()
