import tkinter as tk

root = tk.Tk()

root.geometry("170x230")
root.title("Calculator")
root.maxsize(180,230)
root.minsize(180,230)

ent = tk.Entry(root, width=16, borderwidth=3, relief=tk.RIDGE)
ent.grid(pady=10,row=0,sticky="w",padx=15)

def delete():
        a = ent.get()
        ent.delete(first=len(a)-1,last="end")
def fresult():
        if ent.get() == "":
                pass
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
        else:
                c_res = ent.get()
                c_res = eval(c_res)
                clearf()
                ent.insert("end",c_res)
def clearf():
        ent.delete(0,"end")

clean = tk.Button(root,text="C",width=2,command=clearf,bg="green",fg="white",relief=tk.RIDGE)
clean.grid(row=0,sticky="w",padx=125)
Char_nine = tk.Button(text="9",width=2,command=lambda : ent.insert("end","9"),borderwidth=3,relief=tk.RIDGE)
Char_nine.grid(row=1,sticky="w",padx=15)
Char_eight = tk.Button(text="8",width=2,command=lambda : ent.insert("end","8"),borderwidth=3,relief=tk.RIDGE)
Char_eight.grid(row=1,sticky="w",padx=45)
Char_seven = tk.Button(root,text="7",width=2,command=lambda : ent.insert("end","7"),borderwidth=3,relief=tk.RIDGE)
Char_seven.grid(row=1,sticky="w",padx=75)
Char_plus = tk.Button(root,text="+",width=2,command=lambda : ent.insert("end","+"),borderwidth=3,relief=tk.RIDGE)
Char_plus.grid(row=1,sticky="e",padx=125)
Char_six = tk.Button(text="6",width=2,command=lambda : ent.insert("end","6"),borderwidth=3,relief=tk.RIDGE)
Char_six.grid(row=2,sticky="w",padx=15,pady=5)
Char_five = tk.Button(text="5",width=2,command=lambda : ent.insert("end","5"),borderwidth=3,relief=tk.RIDGE)
Char_five.grid(row=2,sticky="w",padx=45,pady=5)
Char_four = tk.Button(root,text="4",width=2,command=lambda : ent.insert("end","4"),borderwidth=3,relief=tk.RIDGE)
Char_four.grid(row=2,sticky="w",padx=75,pady=5)
Char_minus = tk.Button(root,text="-",width=2,command=lambda : ent.insert("end","-"),borderwidth=3,relief=tk.RIDGE)
Char_minus.grid(row=2,sticky="e",padx=125,pady=5)
Char_three = tk.Button(text="3",width=2,command=lambda : ent.insert("end","3"),borderwidth=3,relief=tk.RIDGE)
Char_three.grid(row=3,sticky="w",padx=15,pady=5)
Char_two = tk.Button(text="2",width=2,command=lambda : ent.insert("end","2"),borderwidth=3,relief=tk.RIDGE)
Char_two.grid(row=3,sticky="w",padx=45,pady=5)
Char_one = tk.Button(root,text="1",width=2,command=lambda : ent.insert("end","1"),borderwidth=3,relief=tk.RIDGE)
Char_one.grid(row=3,sticky="w",padx=75,pady=5)
Char_multiply = tk.Button(root,text="*",width=2,command=lambda : ent.insert("end","*"),borderwidth=3,relief=tk.RIDGE)
Char_multiply.grid(row=3,sticky="e",padx=125,pady=5)
Char_zero = tk.Button(text="0",width=2,command=lambda : ent.insert("end","0"),borderwidth=3,relief=tk.RIDGE)
Char_zero.grid(row=4,sticky="w",padx=15,pady=5)
Char_double_zero = tk.Button(text="00",width=2,command=lambda : ent.insert("end","00"),borderwidth=3,relief=tk.RIDGE)
Char_double_zero.grid(row=4,sticky="w",padx=45,pady=5)
Char_dot = tk.Button(root,text=".",width=2,command=lambda : ent.insert("end","."),borderwidth=3,relief=tk.RIDGE)
Char_dot.grid(row=4,sticky="w",padx=75,pady=5)
Char_divide = tk.Button(root,text="/",width=2,command=lambda : ent.insert("end","/"),borderwidth=3,relief=tk.RIDGE)
Char_divide.grid(row=4,sticky="e",padx=125,pady=5)
result = tk.Button(root,text="=",width=10,command=fresult,bg="green",fg="white",borderwidth=3,relief=tk.RIDGE)
result.grid(row=5,sticky="w",padx=15,pady=5)
Char_modulus = tk.Button(root,text="%",width=2,command=lambda : ent.insert("end","%"),borderwidth=3,relief=tk.RIDGE)
Char_modulus.grid(row=5,sticky="e",padx=125,pady=5)
delete = tk.Button(root,text="del",width=2,command=delete,borderwidth=3,relief=tk.RIDGE)
delete.grid(row=5,sticky="w",padx=80,pady=5)

root.mainloop()