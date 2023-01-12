import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x450")

def buttonFunction():
    print("Burada")
    #radio buton
    m = method.get()
    if m == "1":
        print("Method1")
    elif m == "2":
        print("Medhod2")
    else:
        print("Seçim yapmadınız.")
    #comboBox
    print(problem.get())
    #checkbutton
    value = save_var.get()
    if value == 1:
        print("Save_")
    else:
        print("Not save")

button = tk.Button(window, text="BUTON", activebackground="Red",
                    bg="black",fg="white",activeforeground="black",
                    height=15, width=50, command=buttonFunction)
button.grid(row= 0, column= 0, pady=15)

#radio buton
method = tk.StringVar() # elde edeceğimiz veriyi tanımlamak için string veriable tanımladık
tk.Radiobutton(window, text="Method1: ",value="1",activebackground="red",
                bg="green",height=5,width=5,borderwidth=15,
                variable=method).grid(row=1,column=0)

tk.Radiobutton(window, text="Method2: ",value="2",
                variable=method).grid(row=1,column=1, pady=15)

#Combo Box
problem = tk.StringVar()
comboBox = ttk.Combobox(window, textvariable=problem, values=("1","2","3"), state="readonly")
comboBox.grid(row=2,column=0,pady=15)

#checkButton
def checkButtonFunction():
    print("Save")
save_var = tk.IntVar()
save_var.set(0)
c_button = tk.Checkbutton(window, text="Save", variable=save_var,
            font="Times 25", activebackground="green", activeforeground="white",
            bg="yellow", command=checkButtonFunction)
c_button.grid(row=2,column=1,pady=15)

window.mainloop()