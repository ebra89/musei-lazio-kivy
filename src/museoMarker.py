from kivy.garden.mapview import MapMarkerPopup
from locationPopupMenu import LocationPopupMenu


class MuseoMarker(MapMarkerPopup):
    #source = "assets/geo-recinto.png"
    source = "assets/segnaposto-40.png"
    musei_data = []
    def on_release(self):
        #aprire popup di location
        menu = LocationPopupMenu(self.musei_data)
        menu.size_hint = [.8, .9]
        menu.open()

