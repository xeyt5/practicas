import random

class adivinar_numero():
    def __init__(self):
        self.numero_a_adivinar = random.randint(1, 100)
        self.intentos = 0

    def jugar(self):
        print("Juego de adivinar el numero entre el 1 y el 100")
        while True:
            try:
                intento = int(input("Ingresa tu primer intento: "))
                self.intentos += 1
                if intento < 1 or intento > 100:
                    print("Por favor ingresa un numero entre 1 y 100.")
                    continue
                if intento < self.numero_a_adivinar:
                    print("Demasiado bajo. Intenta de nuevo.")
                elif intento > self.numero_a_adivinar:
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    print(f"Felicidades! Adivinaste el numero {self.numero_a_adivinar} en {self.intentos} intentos.")
                    break
            
            except ValueError:
                print("Entrada invalida. Por favor ingresa un numero entero.")
                print("Opción inválida. Por favor elige una opción del 1 al 100")
        
juego = adivinar_numero()
juego.jugar()
