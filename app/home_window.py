import tkinter as tk
from cube_multidim import CubeMultidim
from cube_tabulaire import CubeTabulaire
from requete_sql_select import RequeteSQLSelect

class HomeWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Home")

        # Create buttons
        self.button_cube_tabulaire = tk.Button(self, text="Cube Tabulaire", command=self.open_cube_tabulaire)
        self.button_cube_multidim = tk.Button(self, text="Cube Multidim", command=self.open_cube_multidim)
        self.button_requete_sql_select = tk.Button(self, text="Requête SQL Select", command=self.open_requete_sql_select)

        # Place buttons
        self.button_cube_tabulaire.pack(side=tk.LEFT, padx=10, pady=10)
        self.button_cube_multidim.pack(side=tk.LEFT, padx=10, pady=10)
        self.button_requete_sql_select.pack(side=tk.LEFT, padx=10, pady=10)

    def open_cube_tabulaire(self):
        cube_tabulaire_window = CubeTabulaire(self.master)
        return

    def open_cube_multidim(self):
        cube_multidim_window = CubeMultidim(self.master)
        return

    def open_requete_sql_select(self):
        requete_sql_select_window = RequeteSQLSelect(self.master)
        return
