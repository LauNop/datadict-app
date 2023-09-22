import os
import tkinter as tk
from tkinter import filedialog
from abc import ABC, abstractmethod

class FileSelection(tk.Toplevel,ABC):
    def __init__(self, master=None, button_label="Generate Data Dict"):
        super().__init__(master)
        self.master = master
        self.title("File Selection")

        # Create a non-editable text area
        self.file_path_var = tk.StringVar()
        self.directory_path_var = tk.StringVar()
        self.file_path_entry = tk.Entry(self, textvariable=self.file_path_var, state="readonly", width=40)
        self.file_path_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create radio buttons for File and Folder selection
        self.selection_mode = tk.IntVar()
        self.radio_file = tk.Radiobutton(self, text="File", variable=self.selection_mode, value=1)
        self.radio_folder = tk.Radiobutton(self, text="Folder", variable=self.selection_mode, value=2)
        self.radio_file.grid(row=1, column=0, padx=10, pady=10)
        self.radio_folder.grid(row=2, column=0, padx=10, pady=10)

        # Create a Browse button for file selection
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file_or_folder)
        self.browse_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        # Create a Generate Data Dict button
        self.generate_button = tk.Button(self, text=button_label, command=self.generate_data_dict)
        self.generate_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    @abstractmethod
    def browse_file_or_folder(self):
        file_path =""
        directory_path=""
        if self.selection_mode.get() == 1:
            file_path = filedialog.askopenfilename()
        elif self.selection_mode.get() == 2:
            directory_path = filedialog.askdirectory()
        else:
            return

        if file_path:
            self.file_path_var.set(file_path)
        elif directory_path:
            self.directory_path_var.set(directory_path)

    @abstractmethod
    def get_files(self):
        if self.file_path_var.get():
            selected_file = self.file_path_var.get()
            return [selected_file]
        elif self.directory_path_var.get():
            selected_folder = self.directory_path_var.get()
            selected_files = [os.path.join(selected_folder, f) for f in os.listdir(selected_folder)
                              if os.path.isfile(os.path.join(selected_folder, f))]
            return selected_files
        else:
            return

    @abstractmethod
    def generate_data_dict(self):
        return self.get_files()
