#Crear procesos
#Asignarles memoria
#Liberar memoria
#Ver el estado actual de la RAM

#Reglas del sistema
#La RAM total es 1024 MB
#Cada proceso tiene:
#pid (entero)
#nombre
#memoria_usada (MB)
#No se puede asignar más memoria de la disponible
#Al eliminar un proceso, su memoria se libera

class Proceso:
    def __init__(self):
        self.ram_total = 1024
        self.ram_usada = 0
        self.procesos = {}
        self.pid_counter = 1

    def crear_proceso(self, nombre, memoria_usada):
        if self.ram_usada + memoria_usada > self.ram_total:
            return "Error: No hay suficiente memoria disponible."
        pid = self.pid_counter
        self.procesos[pid] = {
            'nombre': nombre,
            'memoria_usada': memoria_usada
        }
        self.ram_usada += memoria_usada
        self.pid_counter += 1
        return f"Proceso {nombre} creado con PID {pid} usando {memoria_usada} MB."
    
    def eliminar_proceso(self, pid):
        if pid not in self.procesos:
            return "Error: Proceso no encontrado."
        memoria_liberada = self.procesos[pid]['memoria_usada']
        del self.procesos[pid]
        self.ram_usada -= memoria_liberada
        return f"Proceso con PID {pid} eliminado, liberando {memoria_liberada} MB."
    
    def estado_ram(self):
        memoria_disponible = self.ram_total - self.ram_usada
        return {
            'RAM Total (MB)': self.ram_total,
            'RAM Usada (MB)': self.ram_usada,
            'RAM Disponible (MB)': memoria_disponible,
            'Procesos Activos': self.procesos
        }
    
simulador = Proceso()
print(simulador.crear_proceso("Proceso1", 200))
print(simulador.crear_proceso("Proceso2", 500))
print(simulador.estado_ram())
print(simulador.eliminar_proceso(1))
print(simulador.estado_ram())

    