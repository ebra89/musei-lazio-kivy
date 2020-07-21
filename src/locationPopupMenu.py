from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, musei_data):
        super().__init__()
        # settare il nome del monumento
        headers = "nome_museo,sito_web,statale_non_statale,omr,sistema_museale_territoriale,sistema_museale_urbano," \
                  "sistema_museale_tematico,casa_museo,indirizzo,localita,ubicazione,cap,telefno,fax,email"
        headers = headers.split(',')
        for i in range(len(headers)):
            attribut_name = headers[i]
            attribut_value = musei_data[i]
            setattr(self,attribut_name,attribut_value)
