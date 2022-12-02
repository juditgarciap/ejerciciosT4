class Mision():
    def __init__(self, id, tipo, destino, general):
        self.id = id
        self.tipo = tipo
        self.destino = destino
        self.general = general

    def __str__(self):
        return 'Mision {} - tipo {} hacía {} comandada por el general {}'.format(self.id, self.tipo, self.destino, self.general)
