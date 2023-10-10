import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from tktooltip import ToolTip
import gui.constants as cons

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title(cons.LOGIN_TITLE)
        self.root.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):

        # Create a frame to contain email and password entry widgets with an groove border
        frame = ttk.Frame(self.root, padding=10, relief="groove")
        frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.email_label = ttk.Label(frame, text=cons.EMAIL_LABEL)
        self.password_label = ttk.Label(frame, text=cons.PWD_LABEL)
        self.email_entry = ttk.Entry(frame)
        self.password_entry = ttk.Entry(frame, show="*")

        self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Create a frame to contain buttons
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=2, sticky="s")

        self.login_button = ttk.Button(button_frame, text=cons.LOGIN_BTN, command=self.on_login_click)
        self.cancel_button = ttk.Button(button_frame, text=cons.CANCEL_BTN, command=self.on_cancel_click)
        self.register_label = ttk.Label(button_frame, text="Not registered?")
        self.register_button = ttk.Button(button_frame, text=cons.CREATE_BTN, command=self.register_user)

        self.login_button.grid(row=0, column=0, padx=5, pady=5)
        self.cancel_button.grid(row=0, column=1, padx=5, pady=5)
        self.register_label.grid(row=1, column=0, columnspan=2, pady=5)
        self.register_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Add tooltips
        ToolTip(self.email_entry, msg=cons.EMAIL_TOOLTIP)
        ToolTip(self.password_entry, msg=cons.PWD_TOOLTIP)

        # Add padding to outer frames for better appearance
        ttk.Style().configure("TFrame", padding=10)

        # Set style for labels
        ttk.Style().configure("TLabel", font=(cons.FONT_NAME, cons.FONT_SIZE))

        # Set style for buttons
        ttk.Style().configure("TButton", font=(cons.FONT_NAME, cons.FONT_SIZE))

        self.email_entry.focus()

    def on_login_click(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not self.validate_email(email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            self.email_entry.focus()
        else:
            # Perform authentication logic here (dummy validation)
            if email == "user@example.com" and password == "password":
                messagebox.showinfo("Login Successful", "Welcome, User!")
            else:
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
                

    def on_cancel_click(self):
        self.root.quit()

    def register_user(self):
        messagebox.showinfo("Register", "Redirect to registration page.")

    def validate_email(self, email):
        pattern = cons.EMAIL_REGEX
        return re.match(pattern, email)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LoginScreen(root)

#     # Set the login screen size
#     root.geometry(cons.LOGIN_SCREEN_SIZE)

#     # Center the window on the screen
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     x = (screen_width - cons.LOGIN_SCREEN_WIDTH) // 2
#     y = (screen_height - cons.LOGIN_SCREEN_HEIGHT) // 2
#     root.geometry(f"{cons.LOGIN_SCREEN_WIDTH}x{cons.LOGIN_SCREEN_HEIGHT}+{x}+{y}")

#     root.mainloop()
