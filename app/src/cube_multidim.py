from .file_selection import FileSelection
from datadict_toolbox import ExtractorMultidimCubeCatalog as emcc


class CubeMultidim(FileSelection):
    def __init__(self, master=None):
        super().__init__(master, button_label="Generate Cube Multidim Data Dict")

    # Override any necessary methods
    def browse_file_or_folder(self):
        super().browse_file_or_folder()
        return

    def browse_save_dir(self):
        super().browse_save_dir()
        return

    def get_files(self,file_type):
        return super().get_files(file_type)

    def reset_file_path(self):
        super().reset_file_path()
        return

    def show_warning_popup(self):
        super().show_warning_popup()
        return

    def generate_data_dict(self):
        if super().generate_data_dict():
            files_path_list = self.get_files(".xmla")
            for file_path in files_path_list:
                emcc_obj = emcc(file_path)
                emcc_obj.save(self.save_path_var)
        else:
            self.show_warning_popup()
        return