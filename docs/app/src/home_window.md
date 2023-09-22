home_window.py
This documentation file was created on 22 September 2023 at 14:55:08

## File path

.\app\src\home_window.py

## Purpose of file

This file is responsible for creating the main window of the application and handling the button clicks to open different windows.

## Codebase

### Imports:

1. `import tkinter as tk`

   This imports the `tkinter` module and assigns it the alias `tk`. The `tkinter` module is a standard Python library for creating GUI applications.

2. `from tkinter import messagebox`

   This imports the `messagebox` module from the `tkinter` package. The `messagebox` module provides functions for displaying various types of message boxes in a GUI application.

3. `from .cube_multidim import CubeMultidim`

   This imports the `CubeMultidim` class from the `cube_multidim` module in the same package. The `CubeMultidim` class is responsible for creating the window for the multidimensional cube.

4. `from .cube_tabulaire import CubeTabulaire`

   This imports the `CubeTabulaire` class from the `cube_tabulaire` module in the same package. The `CubeTabulaire` class is responsible for creating the window for the tabular cube.

5. `from .requete_sql_select import RequeteSQLSelect`

   This imports the `RequeteSQLSelect` class from the `requete_sql_select` module in the same package. The `RequeteSQLSelect` class is responsible for creating the window for the SQL select query.

### Classes

#### Class: HomeWindow

Purpose: This class represents the main window of the application.

##### Methods:

1. `__init__(self, master=None)`

   Initializes the `HomeWindow` class.

   - `self.master`: The master window object.
   
   Variables:
   
   - `self.button_cube_tabulaire`: A button widget for opening the tabular cube window.
   - `self.button_cube_multidim`: A button widget for opening the multidimensional cube window.
   - `self.button_requete_sql_select`: A button widget for opening the SQL select query window.

2. `open_cube_tabulaire(self)`

   Opens the tabular cube window.

   - `cube_tabulaire_window`: An instance of the `CubeTabulaire` class.

3. `open_cube_multidim(self)`

   Opens the multidimensional cube window.

   - `cube_multidim_window`: An instance of the `CubeMultidim` class.

4. `open_requete_sql_select(self)`

   Opens the SQL select query window and shows an information popup.

   - `self.show_information_popup()`: Calls the `show_information_popup` method.

5. `show_information_popup(self)`

   Shows an information popup with a message.

   - `messagebox.showinfo("Work in progress", "Feature not operational.")`: Displays an information message box with the given title and message.

### Variables:

There are no global variables in this file.
