cube_multidim.py
This documentation file was created on 22 September 2023 at 14:53:28

## File path

.\app\src\cube_multidim.py

## Purpose of file

This file is responsible for defining a class called `CubeMultidim` that extends the `FileSelection` class. It also imports the `FileSelection` class from the `file_selection` module and the `ExtractorMultidimCubeCatalog` class from the `datadict_toolbox` module. The `CubeMultidim` class overrides some methods from the `FileSelection` class and adds a new method called `generate_data_dict`.

### Imports:

1. `from .file_selection import FileSelection`

   This import statement imports the `FileSelection` class from the `file_selection` module. The `FileSelection` class is used as a base class for the `CubeMultidim` class.

2. `from datadict_toolbox import ExtractorMultidimCubeCatalog as emcc`

   This import statement imports the `ExtractorMultidimCubeCatalog` class from the `datadict_toolbox` module and assigns it an alias `emcc`. The `ExtractorMultidimCubeCatalog` class is used to extract multidimensional cube catalog data.

### Classes

#### Class: CubeMultidim

Purpose: This class represents a cube multidimensional data dictionary generator. It extends the `FileSelection` class and overrides some of its methods.

##### Methods:

1. `__init__(self, master=None)`

   This method is the constructor of the `CubeMultidim` class. It calls the constructor of the `FileSelection` class with the `master` parameter and sets the `button_label` attribute to "Generate Cube Multidim Data Dict".

   ##### Variables:
   - `self.master`: The master widget for the `CubeMultidim` class.
   - `self.button_label`: The label for the button in the GUI.

2. `browse_file_or_folder(self)`

   This method overrides the `browse_file_or_folder` method of the `FileSelection` class. It calls the `browse_file_or_folder` method of the parent class and returns.

3. `browse_save_dir(self)`

   This method overrides the `browse_save_dir` method of the `FileSelection` class. It calls the `browse_save_dir` method of the parent class and returns.

4. `get_files(self, file_type)`

   This method overrides the `get_files` method of the `FileSelection` class. It calls the `get_files` method of the parent class and returns the result.

5. `reset_file_path(self)`

   This method overrides the `reset_file_path` method of the `FileSelection` class. It calls the `reset_file_path` method of the parent class and returns.

6. `show_warning_popup(self)`

   This method overrides the `show_warning_popup` method of the `FileSelection` class. It calls the `show_warning_popup` method of the parent class and returns.

7. `generate_data_dict(self)`

   This method generates the data dictionary for the cube multidimensional data. It first checks if the data dictionary generation is successful by calling the `generate_data_dict` method of the parent class. If successful, it gets a list of file paths with the ".xmla" extension using the `get_files` method of the parent class. Then, for each file path, it creates an instance of the `emcc` class (ExtractorMultidimCubeCatalog) with the file path and saves the cube structure to the specified save path. If the data dictionary generation is not successful, it calls the `show_warning_popup` method of the parent class. Finally, it returns.

### Variables:

There are no global variables defined in this file.
