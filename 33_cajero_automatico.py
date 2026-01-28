#Objetivo
#El programa debe permitir:
#Consultar saldo
#Depositar dinero
#Retirar dinero
#Ver historial de movimientos
#Salir

#Reglas
#El saldo inicial es $1,000
#No se puede retirar más de lo que hay
#No se aceptan depósitos negativos
#Guarda los movimientos en una lista

class CajeroAutomatico():
    def __init__(self):
        self.saldo = 1000.0
        self.historial = []

    def mostrar_saldo(self):
        print(f"su saldo actual es: ${self.saldo:.2f}")

    def depositar_dinero(self):
        try:
            monto = float(input("Ingrese el monto a depositar: $"))
            if monto <= 0:
                print("No se puede aceptar ese deposito")
                return
            self.saldo += monto
            self.historial.append(f"Depósito: +${monto:.2f}")
            print(f"Depósito de ${monto:.2f} realizado con éxito.")
        except ValueError:
            print("Monto inválido. Por favor, ingrese un número.")

    def retirar_dinero(self):
        try:
            monto = float(input("Ingrese el monto a retirar: $"))
            if monto <= 0:
                print("El monto a retirar debe de ser positivo.")
                return
            if monto > self.saldo:
                print("Fondos insuficientes para realizar el retiro.")
                return
            self.saldo -= monto
            self.historial.append(f"Retiro: -${monto:.2f}")
            print(f"Retiro de ${monto:.2f} realizado con éxito.")
        except ValueError:
            print("Monto inválido. Por favor, ingrese un número.")
    
    def ver_historia(self):
        if not self.historial:
            print("el monto no tiene movimientos.")
            return
        print("Historial de movimientos:")
        for movimiento in self.historial:
            print(movimiento)

    def run(self):
        while True:
            print("\n--- Cajero Automático ---")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Ver historial de movimientos")
            print("5. Salir")
            opcion = input("Seleccione una opción (1-5): ")
            if opcion == '1':
                self.mostrar_saldo()
            elif opcion == '2':
                self.depositar_dinero()
            elif opcion == '3':
                self.retirar_dinero()
            elif opcion == '4':
                self.ver_historia()
            elif opcion == '5':
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.run()