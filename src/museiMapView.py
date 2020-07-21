from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from museoMarker import MuseoMarker


class MuseiMapView(MapView):
    getting_monuments_timer = None
    museo_names = []

    def start_getting_musei_in_fov(self):
        # dopo un secondo prende la psizione del field of view
        try:
            self.getting_monuments_timer.cancel()
        except:
            pass

        self.getting_monuments_timer = Clock.schedule_once(self.get_musei_in_fov, 1)

    def get_musei_in_fov(self, *args):
        #prende la reference da main app e il cursore di db
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()

        app = App.get_running_app()
        sql_statement = "SELECT * FROM musei_lazio WHERE longitudine > %s AND longitudine < %s AND latitudine > %s AND latitudine < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        musei = app.cursor.fetchall()
        for museo in musei:
            name = museo[2]
            #print(name)
            if name in self.museo_names:
                continue
            else:
                self.add_museo(museo)

    def add_museo(self, museo):
        #creazione marker per ogni sito
        # da monument prendiamo latitudine e longitudine
        lat, lon = museo[-2], museo[-1]

        # passiamo al marker posizione dei siti
        marker = MuseoMarker(lat=lat,lon=lon)
        marker.musei_data = museo[2:-2]

        #aggiungere il marker alla mappa
        self.add_widget(marker)

        #tenere la traccia di ogni sito solo una volta per evitare di replicare
        name = museo[2]
        self.museo_names.append(name)


