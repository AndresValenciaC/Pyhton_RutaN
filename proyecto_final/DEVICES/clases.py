import random

class Mision:
    # CONSTRUCTOR DE LA CLASE ESTADO INICIAL
    def __init__(self):
        self.mission = random.choice(["ORBONE","CLNM","TMRS","GALXONE","UNKN"])
        
mission = Mision()


class Dispositivos:
    # CONSTRUCTOR DE LA CLASE ESTADO INICIAL
    def __init__(self):
        self.tipo_dispositivo = random.choice(["satelites", "naves", "trajes", "vehiculos"])

dispositivos = Dispositivos()