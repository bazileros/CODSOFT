import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Querybox
from tkinter import simpledialog


def add_task():
    task_name = simpledialog.askstring("Input", "Enter task name:")
    if task_name:
        cal = Querybox()
        start_date = cal.get_date(
            parent=app, title=" ", firstweekday=6, startdate=None, bootstyle="primary"
        )
        end_date = cal.get_date(
            parent=app, title=" ", firstweekday=6, startdate=None, bootstyle="primary"
        )
        priority = get_priority()

        task_details = f"Task: {task_name}   🕧 Start Date: {start_date}   🕧 End Date: {end_date}   ⚠️  Priority: {priority}"
        task_listbox.insert(tk.END, task_details)

        if task_details:
            get_start_date = tb.Label(
                master=task_frame, text=f"Start Date: {start_date}"
            )
            get_start_date.pack(side="right", padx=10, pady=5)


def get_date(title):
    top = tb.Toplevel(app.master)
    top.title("choose date")

    # Use themed calendar widget from ttkbootstrap
    cal = DateEntry(top, width=12, borderwidth=2, date_pattern="yyyy-mm-dd")
    cal.pack(padx=10, pady=10)

    ok_button = tb.Button(top, text="OK", command=top.destroy)
    ok_button.pack(pady=10)
    top.wait_window()
    return cal.get()


def get_priority():
    top = tb.Toplevel(app.master)
    top.title("Select Priority")

    # Use themed radiobuttons from ttkbootstrap
    priority_var = tk.StringVar(value="High")
    for priority in ["High", "Medium", "Low"]:
        tb.Radiobutton(
            top,
            bootstyle="danger",
            text=priority,
            variable=priority_var,
            value=priority,
        ).pack(padx=10, pady=5, anchor="w", ipadx=10, ipady=5)

    ok_button = tb.Button(top, text="OK", command=top.destroy)
    ok_button.pack(pady=10)

    top.wait_window()
    return priority_var.get()


def place_window_center(self):
    self.update_idletasks()
    app_height, app_width = 800, 600
    screen_height = self.winfo_screenheight()
    screen_width = self.winfo_screenwidth()
    xpos = (screen_width // 2) - (app_width // 2)
    ypos = (screen_height // 2) - (app_height // 2)
    self.geometry(f"{app_width}x{app_height}+{xpos}+{ypos}")


# Create the main Tkinter window with ttkbootstrap tb
app = tb.Window(themename="vapor")  # You can choose a different Bootstrap theme
place_window_center(app)
app.title("hire@codewitheros.tech")

# Create a button to add tasks
add_task_button = tb.Button(
    app, text="Add Task", command=add_task, bootstyle="primary, outline", width=150
)
add_task_button.pack(padx=10, pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(app, width=800, height=100)
task_listbox.pack(padx=10, pady=10)

# create a frame container
task_frame = tb.Frame(
    task_listbox, width=100, height=100, borderwidth=2, relief="groove"
)
# task_frame.pack_propagate(False)
task_frame.pack(padx=[10, 30], pady=10)


# Start the Tkinter event loop
app.mainloop()
