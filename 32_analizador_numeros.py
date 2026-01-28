#El programa debe:
#Pedir números al usuario (hasta que escriba salir)
#Guardarlos en una lista
#Mostrar:
#Cantidad de números ingresados
#Número mayor
#Número menor
#Promedio
#Cuántos son pares y cuántos impares

class AnalizadorNumeros():
    def __init__(self):
        self.numeros = []

    def pedir_numeros(self):
        while True:
            entrada = input("Ingrese un numero o 'salir' para terminar: ")
            if entrada.lower() == 'salir':
                break
            try:
                numero = float(entrada)
                self.numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número válido o 'salir'.")

    def mostrar_numeros(self):
        if not self.numeros:
            print("No se ingresaron numeros.")
            return
        cantidad = len(self.numeros)
        numero_mayor = max(self.numeros)
        numero_menor = min(self.numeros)
        promedio = sum(self.numeros) / cantidad
        pares = sum(1 for num in self.numeros if num % 2 == 0)
        impares = cantidad - pares
        mediana = sorted(self.numeros)
        if cantidad % 2 == 1:
            mediana = mediana[cantidad // 2]
        else:
            mid_index = cantidad // 2
            mediana = (mediana[mid_index - 1] + mediana[mid_index]) / 2

        print(f"Cantidad de números ingresados: {cantidad}")
        print(f"Número mayor: {numero_mayor}")
        print(f"Número menor: {numero_menor}")
        print(f"Promedio: {promedio}")
        print(f"Números pares: {pares}")
        print(f"Números impares: {impares}")
        print(f"Mediana: {mediana}")

    def run(self):
        self.pedir_numeros()
        self.mostrar_numeros()

if __name__ == "__main__":
    app = AnalizadorNumeros()
    app.run()