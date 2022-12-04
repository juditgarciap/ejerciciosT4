class Mision():
    def __init__(self, id, tipo, destino, general):
        self.id = id
        self.tipo = tipo
        self.destino = destino
        self.general = general

    def __str__(self):
        return 'Mision {} - tipo {} hacía {} comandada por el general {}'.format(self.id, self.tipo, self.destino, self.general)
        
class Asignador():
    def __init__(self, lista_misiones=[]):
        self.lista_misiones = lista_misiones
        self.asignaciones = {}

    def AsignacionRecursosAutomatica(self):
        for mision in self.lista_misiones:
            if mision.general in ['Palpatine', 'Darth Vader']:
                self.asignaciones[mision.id] = {'Prioridad':'Alta', 'tipo':mision.tipo, 'general':mision.general}
                self.AsignacionRecursosManual(mision)
            else:
                self.asignaciones[mision.id] = {'Prioridad':'Baja', 'tipo':mision.tipo, 'general':mision.general}

                if mision.tipo == 'exploración':
                    self.asignaciones[mision.id]['Scout Troopers'] = 15
                    self.asignaciones[mision.id]['Speeder Bike'] = 2
                    self.asignaciones[mision.id]['Stormtroopers'] = 0
                    self.asignaciones[mision.id]['Veh. aleatorios'] = []
