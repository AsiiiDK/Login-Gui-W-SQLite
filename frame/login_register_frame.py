import tkinter as tk
from tkinter import messagebox

def validate_login(username, password):
    # Check if the username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

def open_registration(window):
    window.withdraw()  # Hide the login window
    register_window = tk.Toplevel(window)
    register_window.title("Registration Page")
    register_window.geometry("300x200")  # Set the size of the registration window (width x height)

    label_register = tk.Label(register_window, text="Register a new account:")
    label_register.pack()

    label_new_username = tk.Label(register_window, text="New Username:")
    label_new_username.pack()
    entry_new_username = tk.Entry(register_window)
    entry_new_username.pack()

    label_new_password = tk.Label(register_window, text="New Password:")
    label_new_password.pack()
    entry_new_password = tk.Entry(register_window, show="*")
    entry_new_password.pack()

    btn_register = tk.Button(register_window, text="Register")
    btn_register.pack()

def open_login_page():
    window = tk.Tk()
    window.title("Login Page")
    window.geometry("300x200")  # Set the initial size of the window (width x height)

    # Create labels and entry fields for username and password
    label_username = tk.Label(window, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    # Create a login button
    btn_login = tk.Button(window, text="Login", command=lambda: validate_login(entry_username.get(), entry_password.get()))
    btn_login.pack()

    # Create a register button
    btn_register = tk.Button(window, text="Register", command=lambda: open_registration(window))
    btn_register.pack()

    # Run the main event loop
    window.mainloop()