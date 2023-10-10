import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Screen")
        self.root.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to contain email and password entry widgets with an inset border
        frame = ttk.Frame(self.root, padding=10, relief="sunken")
        frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.email_label = ttk.Label(frame, text="Email:")
        self.password_label = ttk.Label(frame, text="Password:")
        self.email_entry = ttk.Entry(frame)
        self.password_entry = ttk.Entry(frame, show="*")

        self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Create a frame to contain buttons
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=2, sticky="se")

        self.login_button = ttk.Button(button_frame, text="Login", command=self.on_login_click)
        self.cancel_button = ttk.Button(button_frame, text="Cancel", command=self.on_cancel_click)
        
        self.register_label = ttk.Label(button_frame, text="Not registered? Click")
        self.register_button = ttk.Button(button_frame, text="Here", command=self.register_user)

        self.login_button.grid(row=0, column=0, padx=5, pady=5)
        self.cancel_button.grid(row=0, column=1, padx=5, pady=5)
        self.register_label.grid(row=1, column=0, columnspan=2, pady=5)
        self.register_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Add padding to outer frames for better appearance
        ttk.Style().configure("TFrame", padding=10)

        # Set style for labels
        ttk.Style().configure("TLabel", font=("Helvetica", 12))

        # Set style for buttons
        ttk.Style().configure("TButton", font=("Helvetica", 12))

        # Set focus on email entry by default
        self.email_entry.focus()

    def on_login_click(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not self.validate_email(email):
            # Highlight the email textbox with a red border for validation error
            self.email_entry.configure({"background": "pink"})
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        else:
            # Reset the email textbox background color
            self.email_entry.configure({"background": "white"})

            # Password validation
            if not self.validate_password(password):
                messagebox.showerror("Invalid Password", "Password should contain a capital character, a number, a special character, and be 6-12 characters long.")
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
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def validate_password(self, password):
        # Password should contain a capital character, a number, a special character, and be 6-12 characters long
        return re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,12}$', password)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)

    # Set the login screen size
    root.geometry("400x300")

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 300) // 2
    root.geometry(f"400x300+{x}+{y}")

    root.mainloop()
