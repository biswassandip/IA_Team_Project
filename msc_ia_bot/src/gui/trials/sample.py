import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

def file_new():
    label.config(text="New File Clicked")

def file_open():
    label.config(text="Open File Clicked")

root = tk.Tk()
root.title("GUI Example")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu with "New" and "Open" options
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

label = tk.Label(root, text="Hello, World!")
button = tk.Button(root, text="Click Me", command=on_button_click)

label.pack()
button.pack()

root.mainloop()
