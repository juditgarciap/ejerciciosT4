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

                elif mision.tipo == 'contención':
                    self.asignaciones[mision.id]['Scout Troopers'] = 0
                    self.asignaciones[mision.id]['Speeder Bike'] = 0
                    self.asignaciones[mision.id]['Stormtroopers'] = 30
                    self.asignaciones[mision.id]['Veh. aleatorios'] = random.choices(['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST'], k=3)

                elif mision.tipo == 'ataque':
                    self.asignaciones[mision.id]['Scout Troopers'] = 0
                    self.asignaciones[mision.id]['Speeder Bike'] = 0
                    self.asignaciones[mision.id]['Stormtroopers'] = 50
                    self.asignaciones[mision.id]['Veh. aleatorios'] = random.choices(['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST', 'AT-M6', 'AT-MP', 'AT-DT'], k=7)

                else:
                    print('Tipo misión no valida')

    def AsignacionRecursosManual(self, mision):
        print('Bienvenido general {} a la asignación manual de recursos para la mision {}'.format(mision.general, mision.id))
        Scout_Troopers = int(input('Cuantos Scout Troopers desea?:'))
        Speeder_Bike = int(input('Cuantos Speeder Bike desea?:'))
        Stormtroopers = int(input('Cuantos Stormtroopers desea?:'))
        aleatorios = list(input('Ingrese los Veh. aleatorios que desee, separe por ",":').split(','))

        self.asignaciones[mision.id]['Scout Troopers'] = Scout_Troopers
        self.asignaciones[mision.id]['Speeder Bike'] = Speeder_Bike
        self.asignaciones[mision.id]['Stormtroopers'] = Stormtroopers
        self.asignaciones[mision.id]['Veh. aleatorios'] = aleatorios

        print('Proceso terminado, buena suerte!\n')

    def consultar_recursos_totales(self, mision_id):
        print('Los recursos asignados a la misión: {} son: {}'.format(mision_id, self.asignaciones[mision_id].items()))

    def nuevo_pedido_recursos(self, mision_id):
        print('Proceso para pedir recursos nuevamente para la mision {}'.format(mision_id))
        for mision in self.lista_misiones:
            if mision.id == mision_id:
                self.AsignacionRecursosManual(mision)

    def print_asignaciones(self):
        print(' Asignaciones de recursos para Misiones')
        Scout_Troopers = []
        Speeder_Bike = []
        Stormtroopers = []
        aleatorios = []
