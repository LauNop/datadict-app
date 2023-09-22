cube_tabulaire.py
This documentation file was created on 22 September 2023 at 14:53:59

## File path

.\app\src\cube_tabulaire.py

## Purpose of file

This file is responsible for defining a class called `CubeTabulaire` that extends the `FileSelection` class. It overrides some methods from the parent class and adds a new method called `generate_data_dict`. The `CubeTabulaire` class is used to generate a data dictionary for tabular cubes.

### Imports:

1. `from .file_selection import FileSelection`

   This import brings in the `FileSelection` class from the `file_selection` module in the current package. The `FileSelection` class is used as the parent class for the `CubeTabulaire` class.

2. `from datadict_toolbox import ExtractorTabularCubeCatalog as etcc`

   This import brings in the `ExtractorTabularCubeCatalog` class from the `datadict_toolbox` module. It is aliased as `etcc` for convenience. The `ExtractorTabularCubeCatalog` class is used to extract data from tabular cube catalogs.

### Classes

#### Class: CubeTabulaire

Purpose: This class represents a data dictionary generator for tabular cubes. It extends the `FileSelection` class and overrides some of its methods.

##### Methods:

1. `__init__(self, master=None)`

   This method is the constructor of the `CubeTabulaire` class. It calls the constructor of the parent class `FileSelection` with the `master` parameter and sets the `button_label` attribute to "Generate Cube Tabulaire Data Dict".

   ##### Variables:
   - `self.master`: Represents the master widget.
   - `self.button_label`: Represents the label of the button.

2. `browse_file_or_folder(self)`

   This method overrides the `browse_file_or_folder` method of the parent class. It calls the `browse_file_or_folder` method of the parent class and returns.

3. `browse_save_dir(self)`

   This method overrides the `browse_save_dir` method of the parent class. It calls the `browse_save_dir` method of the parent class and returns.

4. `get_files(self, file_type)`

   This method overrides the `get_files` method of the parent class. It calls the `get_files` method of the parent class with the `file_type` parameter and returns the result.

5. `reset_file_path(self)`

   This method overrides the `reset_file_path` method of the parent class. It calls the `reset_file_path` method of the parent class and returns.

6. `show_warning_popup(self)`

   This method overrides the `show_warning_popup` method of the parent class. It calls the `show_warning_popup` method of the parent class and returns.

7. `generate_data_dict(self)`

   This method generates the data dictionary for tabular cubes. It first calls the `generate_data_dict` method of the parent class. If it returns `True`, it gets a list of files with the ".xmla" extension using the `get_files` method of the parent class. Then, for each file path in the list, it creates an instance of the `ExtractorTabularCubeCatalog` class with the file path and saves the extracted data to the save path specified by `self.save_path_var`. If the `generate_data_dict` method of the parent class returns `False`, it calls the `show_warning_popup` method of the parent class. Finally, it returns.

### Variables:

There are no global variables defined in this file.
