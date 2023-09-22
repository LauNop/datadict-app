from file_selection import FileSelection
from datadict_toolbox import ExtractorMultidimCubeCatalog as emcc


class CubeMultidim(FileSelection):
    def __init__(self, master=None):
        super().__init__(master, button_label="Generate Cube Multidim Data Dict")

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
            emcc_obj = emcc(file_path)
            emcc_obj.save()
        return