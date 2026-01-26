class tareas(object):
    def __init__(self):
        self.tareas = []

    def menu_tareas(self):
        print("\nGestionar tareas:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
            

    def agregar_tarea(self):
        nombre = input("Ingrese el nombre de la tarea: ")
        tarea = {"nombre": nombre, "completada": False}
        self.tareas.append(tarea)
        print(f"Tarea '{nombre}' agregada.")

    def ver_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        print("\nTareas pendientes:")
        for idx, tarea in enumerate(self.tareas, start=1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{idx}. {tarea['nombre']} - {estado}")

    def eliminar_tarea(self, indice: int):
        if 0 <= indice < len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['nombre']}' eliminada.")
        else:
            print("Índice de tarea inválido.")

    def completar_tarea(self):
        self.ver_tareas()
        try:
            num = int(input("Ingrese el número de la tarea a completar: ")) - 1
            self.tareas[num]["completada"] = True
            print(f"Tarea '{self.tareas[num]['nombre']}' marcada como completada.")
        except:
            print("Número inválido.")

    def run(self):
        while True:
            self.menu_tareas()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.ver_tareas()
            elif opcion == "3":
                self.completar_tarea()
            elif opcion == "4":
                try:
                    indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
                    self.eliminar_tarea(indice)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            elif opcion == "5":
                print("Saliendo del gestor de tareas.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
                
example = tareas()
example.run()