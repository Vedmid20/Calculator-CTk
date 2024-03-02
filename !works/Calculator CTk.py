import tkinter.messagebox
import customtkinter
import math

root = customtkinter.CTk()
w = root.winfo_screenwidth() / 2 - 125
h = root.winfo_screenheight() / 2 - 103
root.geometry(f'250x206+{int(w)}+{int(h)}')
root.title('Calculator')
root.resizable(width=False, height=False)
lang = tkinter.StringVar()

def f(btnText):
    try:
        if btnText == '=':
            res = eval(ent.get())
            ent.delete('0','end')
            ent.insert(tkinter.END, round(res, 2))
        elif btnText == 'C':
            ent.delete('0', 'end')
        elif btnText == 'Exit':
            askYN = tkinter.messagebox.askyesno(title='Вихід', message='Ви справді хочете вийти?')
            if askYN == True:
                root.destroy()
            else:
                root.mainloop()
        elif btnText == 'sin':
            try:
                valueSin = float(ent.get())
                resSin = math.sin(valueSin)
                ent.delete(0, tkinter.END)
                resSin1 = round(resSin, 2)
                ent.insert(0, str(resSin1))
            except ValueError:
                tkinter.messagebox.showerror(title='Помилка', message='Некоректне введення')
        elif btnText == "←":
            ent.delete(len(ent.get())-1)
        else:
            ent.insert(tkinter.END, btnText)
    except SyntaxError:
        tkinter.messagebox.showerror(title='Помилка', message='Некоректне введення')
        ent.delete('0', 'end')
    except NameError:
        tkinter.messagebox.showerror(title='Помилка', message='Некоректне введення')
        ent.delete('0', 'end')

lst = ["1", "2", "3", "+", "*", "4", "5", "6", "-", "/", "7", "8", "9", "sin", "←", ".", "0", "C", "=", "Exit"]
ent = customtkinter.CTkEntry(root, font=('Lucida Console', 13), textvariable=lang, )
ent.grid(row=0, column=0, columnspan=6, padx=20, pady=7, ipadx=50, ipady=6)
rowIter = 1
colIter = 0
for i in lst:
    colIter += 1
    btn = customtkinter.CTkButton(root, text=f'{i}', command=lambda btnText=i: f(btnText), bg_color='grey34', fg_color='grey34',
                                  font=('Lucida Console', 12), corner_radius=4, hover_color='#497DF2')
    btn.grid(row=rowIter, column=colIter, ipady=7)
    root.grid_columnconfigure(colIter, weight=1)
    if colIter == 5:
        colIter = 0
        rowIter += 1

root.mainloop()
