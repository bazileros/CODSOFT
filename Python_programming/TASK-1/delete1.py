import tkinter as tk
from ttkbootstrap.dialogs import Querybox
from tkinter import simpledialog
import ttkbootstrap as tb


count = 0

# def add_task():
#     """
#     Adds a task to the task list.

#     This function prompts the user to enter a task name and then collects the start date, end date, and priority
#     for the task. It then generates a task details string and inserts it into the task listbox.
#     """
#     global count
#     task_name = simpledialog.askstring("Input", "Enter task name:", parent=app)
#     if task_name:
#         start_date = get_start_date()
#         end_date = get_end_date()
#         priority = get_priority()

#         count += 1
#         task_details = f"{count}. Task: {task_name}   🕧 Start Date: {start_date}   🕧 End Date: {end_date}   ⚠️  Priority: {priority}</span>"
#         task_listbox.insert(tk.END, task_details)
def add_task():
    """
    Adds a task to the task list.

    This function prompts the user to enter a task name and then collects the start date, end date, and priority
    for the task. It then generates a task details string and inserts it into the task listbox.
    """
    global count
    task_name = simpledialog.askstring("Input", "Enter task name:", parent=app)
    if task_name:
        start_date = get_start_date()
        end_date = get_end_date()
        priority = get_priority()

        count += 1
        task_frame = tk.Frame(task_listbox)
        task_frame.pack(fill=tk.X)

        task_label = tk.Label(task_frame, text=f"{count}. Task: {task_name}", width=30)
        task_label.pack(side=tk.LEFT)

        start_date_button = tk.Button(task_frame, text=f"Start Date: {start_date}")
        start_date_button.pack(side=tk.LEFT)

        end_date_button = tk.Button(task_frame, text=f"End Date: {end_date}")
        end_date_button.pack(side=tk.LEFT)

        priority_label = tk.Label(task_frame, text=f"Priority: {priority}")
        priority_label.pack(side=tk.LEFT)

def get_start_date():
    """
    Get the start date for a task.

    This function displays a date picker dialog and returns the selected start date.
    """
    get_start_date = Querybox()
    get_start_date.get_date(
        parent=task_frame,
        title=" ",
        firstweekday=6,
        startdate=None,
        bootstyle="primary",
    )


def get_end_date(): 
    """
    Get the end date for a task.

    This function displays a date picker dialog and returns the selected end date.
    """
    end_date_popup = Querybox()
    end_date_popup.get_date(
        parent=task_frame,
        title=" ",
        firstweekday=6,
        bootstyle="primary"
    )    


def place_window_center(self):
    """
    Position the toplevel window in the center of the screen.

    This function calculates the position of the toplevel window based
    on the screen size and sets its geometry accordingly.
    """
    app_height = 800
    app_width = 800
    self.update_idletasks()
    screen_height = self.winfo_screenheight()
    screen_width = self.winfo_screenwidth()
    xpos = (screen_width // 2) - (app_width // 2)
    ypos = (screen_height // 2) - (app_height // 2)
    self.geometry(f"{app_width}x{app_height}+{xpos}+{ypos}")


def get_priority():
    """
    Get the priority for a task.

    This function displays a dialog with radio buttons to select the priority of the task.
    It returns the selected priority.
    """
    top = tb.Toplevel(app.master)
    top.title("Select Priority")

    priority_var = tb.StringVar(value="High")
    for priority in ["High", "Medium", "Low"]:
        tb.Radiobutton(
            top,
            bootstyle="danger",
            text=priority,
            variable=priority_var,
            value=priority,
        ).pack(padx=10, pady=5, anchor="w", ipadx=10, ipady=5)

    ok_button = tb.Button(top, text="OK", command=top.destroy)
    ok_button.pack(pady=5)
    return priority_var.get()


# Create the main Tkinter window with ttkbootstrap tb
app = tb.Window(themename="vapor")  # You can choose a different Bootstrap theme
place_window_center(app)
app.title("hire@codewitheros.tech")

# Create a button to add tasks
add_task_button = tb.Button(
    app, text="Add Task", command=add_task, bootstyle="primary, outline", width=150
)
add_task_button.pack(padx=10, pady=10)

# Create a frame container
task_frame = tb.Frame(app, borderwidth=2)
task_frame.pack(padx=10, pady=10)



# Create a listbox to display tasks
task_listbox = tk.Listbox(app, width=750, height=100)
task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)



# Start the Tkinter event loop
app.mainloop()
