from tkinter import *

root = Tk()

def operation():
   b1 = Button(frame2, text="Addition", command=add)
   b2 = Button(frame2, text="Subtraction", command=sub)
   b3 = Button(frame2, text="Multiplication", command=mul)
   b4 = Button(frame2, text="Division", command=div)

   b1.pack(side=LEFT)
   b2.pack(side=LEFT)
   b3.pack(side=LEFT)
   b4.pack(side=LEFT)

def add():
   c = 0
   label_operators = Label(frame3, text="Enter the number of Operators:")
   n_op = Entry(frame3)
   #converting input value to integer type
   num = int(n_op)
   for i in range(num):
       val = Entry(frame4)
       op = int(val)
       c += op
       val.pack()
   label_operators.grid(row=0, column=0, sticky=E)
   n_op.grid(row=0, column=1)
   print("Result = " + str(c))

def sub():
   c = 0
   label_operators = Label(frame3, text="Enter the number of Operators:")
   n_op = Entry(frame3)
   num = int(n_op)
   for i in range(num):
       val = Entry(frame4)
       op = int(val)
       if i is 0:
           c += op
       else:
           c -= op
       val.pack()
   label_operators.grid(row=0, column=0, sticky=E)
   n_op.grid(row=0, column=1)
   print("Result = " + str(c))

def mul():
   c = 1
   label_operators = Label(frame3, text="Enter the number of Operators:")
   n_op = Entry(frame3)
   num = int(n_op)
   for i in range(num):
       val = Entry(frame4)
       op = int(val)
       c *= op
       val.pack()
   label_operators.grid(row=0, column=0, sticky=E)
   n_op.grid(row=0, column=1)
   print("Result = " + str(c))

def div():
   c = 0
   label_operators = Label(frame3, text="Enter the number of Operators:")
   n_op = Entry(frame3)
   num = int(n_op)
   for i in range(num):
       val = Entry(frame4)
       op = int(val)
       if i is 0:
           c = op
       else:
           c /= op
       val.pack()
   label_operators.grid(row=0, column=0, sticky=E)
   n_op.grid(row=0, column=1)
   print("Result = " + str(c))


frame1 = Frame(root, height=300)
title = Label(frame1, text="BASIC CALCULATOR", bg="yellow", fg="red")
menu = Button(frame1, text="Operations", bg="black", fg="white", command=operation)
exit_button = Button(frame1, text="Quit", bg="black", fg="white", command=root.quit)
frame2 = Frame(root, height=100)
frame3 = Frame(root, height=200)
frame4 = Frame(root, height=300)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
title.pack(fill=X)
menu.pack()
exit_button.pack()

root.mainloop()