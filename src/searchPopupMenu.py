from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App

class SearchPopupMenu(MDInputDialog):
    titel = "Cerca per Comune"
    text_button_ok = 'Cerca'
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def callback(self,*args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)
        #print(address)

    def geocode_get_lat_lon(self,address):
        with open('Musei-project/app_id.txt', 'r') as f:
            app_id = f.read()
        with open('Musei-project/app_code.txt', 'r') as f:
            app_code = f.read()
        address = parse.quote(address)
        #url = 'https://geocoder.api.here.com/6.2/geocode.json?app_id=%s&app_code=%s&searchtext=%s'%(app_id,app_code,address)
        url = 'https://geocode.search.hereapi.com/v1/geocode?q=%s+Italy&apiKey=%s'%(address,app_code)
        print(url)
        UrlRequest(url, on_success=self.success,on_failure=self.failure,on_error=self.error)

    def success(self,urlrequest,result):
        print('Successo')
        lat = result['items'][0]['position']['lat']
        lon = result['items'][0]['position']['lng']
        print(result)
        print(lat)
        #print(lon)
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(lat,lon)

    def failure(self,urlrequest,result):
        print('Failure')
        print(result)

    def error(self,urlrequest,result):
        print('Error')
        print(result)