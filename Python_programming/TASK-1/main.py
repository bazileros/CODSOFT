from tkinter import *
import ttkbootstrap as tb

app = tb.Window(title="To-Do List", themename="vapor")
app.resizable(False, False)
app.iconbitmap("")
app.geometry("800x600")


def place_window_center(self):
    """Position the toplevel in the center of the screen. Does not
    account for titlebar height."""
    self.update_idletasks()
    w_height = self.winfo_height()
    w_width = self.winfo_width()
    s_height = self.winfo_screenheight()
    s_width = self.winfo_screenwidth()
    xpos = (s_width - w_width) // 5
    ypos = (s_height - w_height) // 2
    self.geometry(f"+{xpos}-{ypos}")


title_lable = tb.Label(
    app, text="To-Do List", font=("UbuntuMono", 30), bootstyle="info, inverse"
)
title_lable.pack()
frame_style = tb.Frame(app, bootstyle="success")
frame_style.pack(pady=20)


# place_window_center(app)
app.mainloop()
