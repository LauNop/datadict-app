file_selection.py
This documentation file was created on 22 September 2023 at 14:54:32

## File path

.\app\src\file_selection.py

## Purpose of file

This file is responsible for creating a file selection window using the tkinter library in Python. It allows the user to select a file or folder, browse for a save folder, and generate a data dictionary.

## Codebase

### Imports:

1. ```python
import os
```
The `os` module provides a way to use operating system dependent functionality. In this file, it is used to check if a selected folder is a directory.

2. ```python
import tkinter as tk
```
The `tkinter` module is the standard Python interface to the Tk GUI toolkit. It is used to create the file selection window and its components.

3. ```python
from tkinter import filedialog, messagebox
```
The `filedialog` module provides a way to open file and directory selection dialogs. The `messagebox` module provides a way to display warning messages.

4. ```python
from abc import ABC, abstractmethod
```
The `ABC` class is a helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage. The `abstractmethod` decorator is used to indicate that a method is abstract and must be implemented by subclasses.

### Classes

#### Class: FileSelection

Purpose: This class represents the file selection window. It inherits from `tk.Toplevel` and `ABC` (Abstract Base Class).

##### Methods:

1. ```python
__init__(self, master=None, button_label="Generate Data Dict")
```
This method is the constructor of the `FileSelection` class. It initializes the class and creates the file selection window.

###### Variables:
- `self.master`: The master widget of the file selection window.
- `self.path_var`: A `tk.StringVar` object that stores the selected file or folder path.
- `self.file_path_entry`: A `tk.Entry` object that displays the selected file or folder path.
- `self.selection_mode`: A `tk.IntVar` object that stores the selection mode (file or folder).
- `self.radio_file`: A `tk.Radiobutton` object for selecting file mode.
- `self.radio_folder`: A `tk.Radiobutton` object for selecting folder mode.
- `self.browse_button`: A `tk.Button` object for browsing file or folder.
- `self.save_path_var`: A `tk.StringVar` object that stores the selected save folder path.
- `self.save_path_entry`: A `tk.Entry` object that displays the selected save folder path.
- `self.save_browse_button`: A `tk.Button` object for browsing save folder.
- `self.generate_button`: A `tk.Button` object for generating the data dictionary.

2. ```python
browse_file_or_folder(self)
```
This method is an abstract method that is called when the browse button is clicked. It opens a file or folder selection dialog based on the selection mode.

3. ```python
browse_save_dir(self)
```
This method is an abstract method that is called when the browse save folder button is clicked. It opens a save folder selection dialog.

4. ```python
get_files(self, file_type)
```
This method is an abstract method that returns a list of selected files based on the selected folder and file type.

5. ```python
reset_file_path(self)
```
This method is an abstract method that resets the file path variable when a radio button is clicked.

6. ```python
show_warning_popup(self)
```
This method is an abstract method that displays a warning message if no file or folder is selected before generating the data dictionary.

7. ```python
generate_data_dict(self)
```
This method is an abstract method that checks if both the file path and save path are selected before generating the data dictionary.

### Variables:

There are no global variables outside of functions and classes in this file.
