from file_selection import FileSelection
from datadict_toolbox import SelectGPTDeduce


class RequeteSQLSelect(FileSelection):
    def __init__(self, master=None):
        super().__init__(master, button_label="Generate SQL Select Data Dict")

    # Override any necessary methods
    def browse_file_or_folder(self):
        super().browse_file_or_folder()
        return

    def get_files(self):
        super().get_files()
        return

    def generate_data_dict(self):
        files_path_list = super().generate_data_dict()
        for file_path in files_path_list:
            # Instance SelectGPTDeduce
            print(file_path)
        return