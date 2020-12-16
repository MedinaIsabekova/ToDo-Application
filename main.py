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
    lb_tasks.delete(0, "end")
    
    
def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task!"
        txt_input.delete(0, "end")
        
        
btn_add_task = tkinter.Button(root, text="Add Task",
                              fg="coral", bg="brown", width=15, command=add_task,
                              font=('Times New Roman', 10, 'bold'))

lb_tasks = tkinter.Listbox(root, width=35, font=('Times New Roman', 12, 'bold'))
lb_tasks.grid(row=2, column=1, rowspan=10)


root.mainloop()
