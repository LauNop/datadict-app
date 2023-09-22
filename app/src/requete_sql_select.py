from .file_selection import FileSelection
from datadict_toolbox import SelectGPTDeduce


class RequeteSQLSelect(FileSelection):
    def __init__(self, master=None):
        super().__init__(master, button_label="Generate SQL Select Data Dict")

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
            # Instance SelectGPTDeduce
            # We need openai_organization, openai_api_key, sql_query=None, model_name="gpt-4",
            #         response_file_name="model_response", answer_file=None, excel_name = "data_dict",
            #         destination_table = None
            print("Processing")
        return