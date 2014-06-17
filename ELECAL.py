#element amount calculator.py
from Tkinter import *
import csv


fileobj=open("periodic_table.csv","rU")
#open the periodic table

datafile=csv.reader(fileobj)
mytable={}
#intialize mytable

for line in datafile:
    mytable[line[1]]=line[6]
#get information from the periodic table file

temparory={}
#which is a dictionary for the elements needed
result={}
#result

class calculator:

    def __init__(self,master):

        frame=Frame(master)
        frame.pack()

        self.label5=Label(frame,text='Elements and amount:')
        self.label5.grid(row=1,column=1)

        self.elements=Entry(frame,width=20)
        self.elements.grid(row=1,column=2)

        self.Calculate=Button(frame,text='Calculate',width=20,command=self.cal)
        self.Calculate.grid(row=1,column=4)
        
        
        self.label1=Label(frame,text='Input the fomular:')
        self.label1.grid(row=0,column=1)
        
        self.input=Entry(frame,width=20)
        self.input.grid(row=0,column=2)

        self.label3=Label(frame,text='Element needed:')
        self.label3.grid(row=2,column=1)
        
        self.element=Entry(frame,width=20)
        self.element.grid(row=2,column=2)

        self.label4=Label(frame,text='Weight:')
        self.label4.grid(row=2,column=3)
        
        self.amount=Entry(frame,width=20)
        self.amount.grid(row=2,column=4)
        
        self.go=Button(frame,text='Go',width=20,command=self.go)
        self.go.grid(row=0,column=4)

        self.label2=Label(frame,text='result:')
        self.label2.grid(row=4,column=1)

        self.quit=Button(frame,text='quit',width=20,command=frame.quit)
        self.quit.grid(row=4,column=4)

        self.result=Entry(frame,width=20)
        self.result.grid(row=4,column=2)

    def go(self):
        mystr=self.input.get()
        mylist=mystr.split('-')
        fomular=""
        for every in mylist:
            symbol=""      
            quality=""
            for c in every:
                fomular=fomular+c
                if c.isalpha():
                    symbol=symbol+c
                else:
                    quality=quality+c
            if quality=="":
                quality=1
                
            temparory[symbol]=quality
            
        self.elements.insert(0,fomular)

        

    def cal(self):
        element=self.element.get()
        weight=self.amount.get()

        for i in temparory.keys():
            result[i]=float(mytable[i])*float(temparory[i])*float(weight)/float(mytable[element])/float(temparory[element])

        Result=str(result)   
        self.result.insert(0,Result)

root =Tk()

app = calculator(root)

root.mainloop()
