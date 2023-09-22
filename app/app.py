import tkinter as tk
from src import HomeWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Your App Name")

    # Create and display the home window
    home = HomeWindow(root)
    home.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
