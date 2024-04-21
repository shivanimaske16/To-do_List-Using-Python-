import tkinter as tk
from tkinter import messagebox

def add_task():
    task=t1.get()
    if task!="":
        li.insert(tk.END,task)
        t1.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Please enter a task!")

def delete_task():
    selected_index=li.curselection()
    if selected_index:
        index=selected_index[0]
        li.delete(index)
        save_tasks()
    else:
        messagebox.showwarning("Warning","Please select a task to delete!")       

def update_task():
    selected_index=li.curselection()
    if selected_index:
        index=selected_index[0]
        new_task=t1.get()
        li.delete(index)
        li.insert(index, new_task)
        t1.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")



def save_tasks():
    file=open("Tasks.txt", "w")
    tasks = li.get(0, tk.END)
    for task in tasks:
        file.write(task + "\n")

def load_tasks():
    file= open("Tasks.txt", "r")
    for line in file:
        li.insert(tk.END, line.strip())


root=tk.Tk()
root.title("To-Do List")
root.geometry("700x400+200+100")
root.configure(bg="#78A083")

li=tk.Listbox(root,height=10,width=50,bg="#35374B",fg="white")
li.place(x=200,y=100)
t1=tk.Entry(root,width=50,bg="#35374B",fg="white")
t1.place(x=200,y=50)

b1=tk.Button(root,text="Add Task",width=10,command=add_task,bg="#344955",fg="White")
b1.place(x=200,y=300)

b2=tk.Button(root,text="Update Task",width=10,command=update_task,bg="#344955",fg="White")
b2.place(x=310,y=300)

b3=tk.Button(root,text="Delete Task",width=10,command=delete_task,bg="#344955",fg="White")
b3.place(x=420,y=300)

load_tasks()

root.mainloop()




