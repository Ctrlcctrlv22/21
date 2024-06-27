from tkinter import *

root = Tk()
root.title("app")
root.geometry("900x600")
root.configure(bg='#ff5e00')

frame = Frame(bg='#ff5e00')
frame.pack(anchor='center')

def calculate():
    val1=  ent1.get()
    val2= ent2.get()
    val3= ent3.get()
    
    if val1 == '' or  val3  == '' or val2 == '':
        txt['text']= "заполните все поля"
        return
    if val2 == '/' or '//' and val3  == int(0):
        txt['text']= "на ноль делить нельзя "
        return
    if val3  == str or val3  == str:
        txt['text']= "введите число"
        return
    if val2 == '+':
        txt['text'] = float(val1) + float(val3)
    elif val2 == '-':
        txt['text'] = float(val1) - float(val3)
    elif val2 == '/':
        txt['text'] = float(val1) / float(val3)
    elif val2 == '*':
        txt['text'] = float(val1) * float(val3)
    elif val2 == '//':
        txt['text'] = float(val1) // float(val3)
    
    

lab1 = Label(frame, text= "число",font=('Comic Sans MS', 16, "bold"),bg='#ff5e00')
lab2 = Label(frame, text= "операция",font=('Comic Sans MS', 16, "bold"),bg='#ff5e00')
lab3 = Label(frame, text= "число",font=('Comic Sans MS', 16, "bold"),bg='#ff5e00')
ent1 = Entry(frame,font=('Comic Sans MS', 16, "bold", ),width=9,)
ent2 = Entry(frame,font=('Comic Sans MS', 16, "bold", ),width=9)
ent3 = Entry(frame,font=('Comic Sans MS', 16, "bold", ),width=9)
btn = Button(frame,text= "Вычислить",font=('Comic Sans MS', 16, "bold"), command=calculate)
txt = Label(frame,text=" ",font=('Comic Sans MS', 16, "bold"),bg='#ff5e00')

lab1.grid(row=0, column=0, padx=10, pady=10)
lab2.grid(row=0, column=1, padx=10, pady=10)
lab3.grid(row=0, column=2, padx=10, pady=10)
ent1.grid(row=1, column=0, padx=10, pady=10)
ent2.grid(row=1, column=1, padx=10, pady=10)
ent3.grid(row=1, column=2, padx=10, pady=10)
btn.grid(row=2, columnspan=10,sticky='we', column=0, padx=10, pady=10)
txt.grid(row=3, columnspan=10,sticky='we', column=0, padx=10, pady=10)

root.mainloop()