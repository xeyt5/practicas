#Mostrar un menú con opciones:
#   1. Agregar gasto
#   2. Ver total de gastos
#   3. Ver gasto más alto
#   4. Salir
#El programa debe repetirse hasta que el usuario elija Salir.
#Cada gasto tiene:
#   Descripción (texto)
#   Monto (número)
#Guardar los gastos en una lista de diccionarios.
#Calcular:
#   Total gastado
#   Gasto más alto (descripción y monto)

class GestorGastos():
    def __init__(self):
        self.gastos=[]

    def agregar_gastos(self, descripcion: str, monto: float) -> None:
        gastos = {"descripcion": descripcion, "monto": monto}
        self.gastos.append(gastos)
        print("Gasto agregado exitosamente.")

    def ver_total_gastor(self) -> None:
        if not self.gastos:
            print("No hay gastos registrados.")
            return
        total_general = 0
        print("\nLista de gastos:")
        for gasto in self.gastos:
            print(f"- {gasto['descripcion']}: ${gasto['monto']:.2f}")
            total_general += gasto["monto"]

        print(f"\nTotal de todos los gastos: ${total_general:.2f}")

    
    def ver_gasto_mas_alto(self) -> None:
        if not self.gastos:
            print("No hay gastos registrados.")
            return
        gasto_mas_alto = max(self.gastos, key=lambda x: x["monto"])
        print(f"Gasto más alto: {gasto_mas_alto['descripcion']} - ${gasto_mas_alto['monto']:.2f}")

    def monstrar_menu(self):
        while True:
            print("\nMenu de opciones:")
            print("1. Agregar gastos")
            print("2. Ver gastos totales")
            print("3. Ver gasto mas alto")
            print("4. Salir")
            opcion = input("Elige una opción (1-4): ")
            if opcion == "1":
                descripcion = input("Ingrese la descripción del gasto: ")
                try:
                    monto = float(input("Ingrese el monto del gasto: "))
                    self.agregar_gastos(descripcion, monto)
                except ValueError:
                    print("Monto inválido. Por favor ingrese un número.")
            elif opcion == "2":
                self.ver_total_gastor()
            elif opcion == "3":
                self.ver_gasto_mas_alto()
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor elige una opción del 1 al 4.")

gestor = GestorGastos()
gestor.monstrar_menu()

