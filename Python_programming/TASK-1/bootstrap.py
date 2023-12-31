import tkinter as tk
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import pickle

app = tb.Window(themename="vapor")
app.title("codewitheros.tech")


# Create functions
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tb.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        tb.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        tb.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


# Create GUI
frame_tasks = tb.Labelframe(app, padding="5")
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=60)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tb.Scrollbar(frame_tasks, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

entry_task = tb.Entry(frame_tasks, width=50)
entry_task.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

button_add_task = tb.Button(app, text="Add task", width=48, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tb.Button(app, text="Delete task", width=48, command=delete_task)
button_delete_task.pack(pady=5)

button_load_tasks = tb.Button(app, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack(pady=5)

button_save_tasks = tb.Button(app, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack(pady=5)

app.mainloop()
