import tkinter
import random
import tkinter.messagebox

root = tkinter.Tk()


root.geometry("600x350")
root.configure(bg="coral", padx=20, pady=20)
root.title("ToDo List")

tasks = []


def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    pass

lb_tasks = tkinter.Listbox(root, width=35, font=('Times New Roman', 12, 'bold'))
lb_tasks.grid(row=2, column=1, rowspan=10)

root.mainloop()
