import tkinter as tk
from ttkbootstrap.dialogs import Querybox
from tkinter import simpledialog
import ttkbootstrap as tb


def add_task():
    task_name = simpledialog.askstring("Input", "Enter task name:")
    if task_name:
        # Create a frame to hold the widgets for start date, end date, and priority
        task_frame = tb.Frame(task_listbox, borderwidth=2)
        task_frame.pack(padx=10, pady=5, fill=tk.X)

        # Start Date
        start_date_label = tk.Label(task_frame, text="Start Date:")
        start_date_label.pack(side=tk.LEFT, padx=(0, 5))
        startdate_popup = Querybox()
        start_date = startdate_popup.get_date("Start Date:")
        start_date_label = tk.Label(task_frame, text=start_date)
        start_date_label.pack(side=tk.LEFT, padx=(0, 10))

        # End Date
        end_date_label = tk.Label(task_frame, text="End Date:")
        end_date_label.pack(side=tk.LEFT, padx=(0, 5))
        enddate_popup = Querybox()
        end_date = enddate_popup.get_date("End Date:")
        end_date_label = tk.Label(task_frame, text=end_date)
        end_date_label.pack(side=tk.LEFT, padx=(0, 10))

        # Priority
        priority_label = tk.Label(task_frame, text="Priority:")
        priority_label.pack(side=tk.LEFT, padx=(0, 5))
        priority = get_priority()
        priority_label = tk.Label(task_frame, text=priority)
        priority_label.pack(side=tk.LEFT, padx=(0, 10))

        # Task Name
        task_details = f"Task: {task_name}"
        task_label = tk.Label(task_frame, text=task_details)
        task_label.pack(side=tk.LEFT, padx=(0, 10))

# Create the main Tkinter window with ttkbootstrap tb
app = tb.Window(themename="vapor")  # You can choose a different Bootstrap theme
app.geometry("800x600")
app.title("hire@codewitheros.tech")

# Create a button to add tasks
add_task_button = tb.Button(
    app, text="Add Task", command=add_task, bootstyle="primary, outline", width=150
)
add_task_button.pack(padx=10, pady=10)

# create a frame container
task_frame = tb.Frame(app, borderwidth=2)
task_frame.pack(padx=10, pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(task_frame, width=750, height=100)
task_listbox.pack(padx=10, pady=10)

# Start the Tkinter event loop
app.mainloop()

