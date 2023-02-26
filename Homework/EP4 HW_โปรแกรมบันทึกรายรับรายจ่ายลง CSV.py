from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('บันทีกรายรับรายจ่ายลง CSV')
GUI.geometry('1000x400')

######## สร้าง Function CSV  ########

def writecsv1(datalist):
    with open('รายรับ.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser'] 

def writecsv2(datalist):
    with open('รายจ่าย.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser'] 


def readcsv1():
  with open('รายรับ.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file writer
        data = list(fr)
  return data


def readcsv2():
  with open('รายจ่าย.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file writer
        data = list(fr)
  return data

######## สร้าง Function Button  ########





def Savedata1():
    ti = datetime.now().strftime('%Y%m%d %H%M%S')
    dataI1 = VI1_data.get()                   # ดึงข้อมูลจากตัวแปร VI1_data มาใช้งาน
    dataI2 = VI2_data.get()   
    dataI3 = VI3_data.get()
    text = [dataI1,dataI2,dataI3,ti]          # [ช้อมูลในช่องกรอก , เวลาที่กรอก]
    writecsv1(text)                            # บันทึกลง CSV
    VI1_data.set('')                              # clear ข้อมูลในช่องกรอก
    VI2_data.set('')
    VI3_data.set('')
    
    

def Savedata2():
    to = datetime.now().strftime('%Y%m%d %H%M%S')
    dataO1 = VO1_data.get()                   # ดึงข้อมูลจากตัวแปร VIO_data มาใช้งาน
    dataO2 = VO2_data.get()   
    dataO3 = VO3_data.get()
    text = [dataO1,dataO2,dataO3,to]          # [ช้อมูลในช่องกรอก , เวลาที่กรอก]
    writecsv2(text)                            # บันทึกลง CSV
    VO1_data.set('')                              # clear ข้อมูลในช่องกรอก
    VO2_data.set('')
    VO3_data.set('')






########## บันทึกรายรับ ##################

LI0 = Label(GUI,text = 'บันทึกรายรับ',font=('Angsana New',24),fg='blue')
LI0.place(x=100,y=20)

LI1 = Label(GUI,text = 'วันที่',font=('Angsana New',18),fg='green')
LI1.place(x=60,y=100)

VI1_data = StringVar()
EI1 = ttk.Entry(GUI,textvariable=VI1_data,font=('Ansana New',16),width=20)
EI1.place(x=180,y=110)


LI2 = Label(GUI,text = 'รายการรายรับ',font=('Angsana New',18),fg='green')
LI2.place(x=60,y=150)

VI2_data = StringVar()
EI2 = ttk.Entry(GUI,textvariable=VI2_data,font=('Ansana New',16),width=20)
EI2.place(x=180,y=160)

LI3 = Label(GUI,text = 'จำนวน',font=('Angsana New',18),fg='green')
LI3.place(x=60,y=200)

VI3_data = StringVar()
EI3 = ttk.Entry(GUI,textvariable=VI3_data,font=('Ansana New',16),width=20)
EI3.place(x=180,y=210)

LI4 = Label(GUI,text = 'บาท',font=('Angsana New',18),fg='green')
LI4.place(x=450,y=200)

FBI1 = Frame(GUI)
FBI1.place(x=180,y=250)

BI1 = ttk.Button(FBI1,text = 'บันทึกข้อมูล',command=Savedata1)
BI1.pack(ipadx=20,ipady=10)


########## บันทึกรายจ่าย ########################

LO0 = Label(GUI,text = 'บันทึกรายจ่าย',font=('Angsana New',24),fg='blue')
LO0.place(x=600,y=20)

LO1 = Label(GUI,text = 'วันที่',font=('Angsana New',20),fg='green')
LO1.place(x=560,y=100)

VO1_data = StringVar()
EO1 = ttk.Entry(GUI,textvariable=VO1_data,font=('Ansana New',16),width=20)
EO1.place(x=680,y=110)

LO2 = Label(GUI,text = 'รายการรายจ่าย',font=('Angsana New',20),fg='green')
LO2.place(x=560,y=150)

VO2_data = StringVar()
EO2 = ttk.Entry(GUI,textvariable=VO2_data,font=('Ansana New',16),width=20)
EO2.place(x=680,y=160)

LO3 = Label(GUI,text = 'จำนวน',font=('Angsana New',20),fg='green')
LO3.place(x=560,y=200)

VO3_data = StringVar()
EO3 = ttk.Entry(GUI,textvariable=VO3_data,font=('Ansana New',16),width=20)
EO3.place(x=680,y=210)

LO4 = Label(GUI,text = 'บาท',font=('Angsana New',20),fg='green')
LO4.place(x=950,y=200)

FBO1 = Frame(GUI)
FBO1.place(x=680,y=250)

BO1 = ttk.Button(FBO1,text = 'บันทึกข้อมูล',command=Savedata2)
BO1.pack(ipadx=20,ipady=10)





GUI.mainloop()

