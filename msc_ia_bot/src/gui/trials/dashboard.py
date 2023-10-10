import tkinter as tk
from tkinter import Menu, PhotoImage
from login_screen import LoginScreen

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.attributes('-topmost', True)  # Maximize the window
        
        # Create a login screen as a modal window
        # self.login_screen = LoginScreen(self)
        
        # Initialize the menubar
        self.menu = Menu(self)
        self.config(menu=self.menu)
        
        
        # Add menu items with icons and labels
        self.file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", image=self.new_icon, compound=tk.LEFT, command=self.on_new)
        self.file_menu.add_command(label="Open", image=self.open_icon, compound=tk.LEFT, command=self.on_open)
        self.file_menu.add_command(label="List", image=self.list_icon, compound=tk.LEFT, command=self.on_list)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close", image=self.close_icon, compound=tk.LEFT, command=self.on_close)
        
    def on_new(self):
        # Implement the action for the "New" menu item
        pass
    
    def on_open(self):
        # Implement the action for the "Open" menu item
        pass
    
    def on_list(self):
        # Implement the action for the "List" menu item
        pass
    
    def on_close(self):
        # Implement the action for the "Close" menu item
        self.destroy()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
