import os
import tkinter as tk
from tkinter import filedialog, messagebox
from abc import ABC, abstractmethod

class FileSelection(tk.Toplevel,ABC):
    def __init__(self, master=None, button_label="Generate Data Dict"):
        super().__init__(master)
        self.master = master
        self.title("File Selection")

        # Create a non-editable text area
        self.path_var = tk.StringVar()
        self.file_path_entry = tk.Entry(self, textvariable=self.path_var, state="readonly", width=40)
        self.file_path_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create radio buttons for File and Folder selection
        self.selection_mode = tk.IntVar()
        self.radio_file = tk.Radiobutton(self, text="File", variable=self.selection_mode, value=1,
                                         command=self.reset_file_path)
        self.radio_folder = tk.Radiobutton(self, text="Folder", variable=self.selection_mode, value=2,
                                           command=self.reset_file_path)
        self.radio_file.grid(row=2, column=0, padx=10, pady=10)
        self.radio_folder.grid(row=2, column=1, padx=10, pady=10)

        # Create a Browse button for file selection
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file_or_folder)
        self.browse_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Create a non-editable text area
        self.save_path_var = tk.StringVar()
        self.save_path_entry = tk.Entry(self, textvariable=self.save_path_var, state="readonly", width=40)
        self.save_path_entry.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        # Create a Browse button for file selection
        self.save_browse_button = tk.Button(self, text="Browse save folder", command=self.browse_file_or_folder)
        self.save_browse_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        # Create a Generate Data Dict button
        self.generate_button = tk.Button(self, text=button_label, command=self.generate_data_dict)
        self.generate_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

    @abstractmethod
    def browse_file_or_folder(self):
        path =""
        if self.selection_mode.get() == 1:
            path = filedialog.askopenfilename()
        elif self.selection_mode.get() == 2:
            path = filedialog.askdirectory()
        else:
            return

        self.path_var.set(path)
        return

    @abstractmethod
    def browse_save_dir(self):
        path = filedialog.askdirectory()
        self.save_path_var.set(path)
        return

    @abstractmethod
    def get_files(self,file_type):
        if self.path_var.get():
            selected_folder = self.path_var.get()
            selected_files = [os.path.join(selected_folder, f) for f in os.listdir(selected_folder)
                              if os.path.isfile(os.path.join(selected_folder, f)) and f.endswith(file_type)]
            return selected_files
        else:
            return

    @abstractmethod
    def reset_file_path(self):
        self.path_var.set("")  # Reset the file path variable when a radio button is clicked
        return

    @abstractmethod
    def show_warning_popup(self):
        messagebox.showwarning("Warning", "Please choose a file or folder before generating the data dictionary.")

    @abstractmethod
    def generate_data_dict(self):
        if self.path_var.get() and self.save_path_var.get():
            return True
        else:
            return False
