from kivymd.app import MDApp
from museiMapView import MuseiMapView
from searchPopupMenu import SearchPopupMenu

import sqlite3





class MainAPP(MDApp):
    connection = None
    cursor = None
    search_menu = None
    def on_start(self):
        #inizializzare gps

        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"
        #conessione a db
        self.connection = sqlite3.connect("musei_lazio.db")
        self.cursor = self.connection.cursor()

        #chiamare SearchPopupMenu
        self.search_menu = SearchPopupMenu()


MainAPP().run()
