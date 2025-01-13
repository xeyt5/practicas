#verificar si un numero es par o impar.
#clase solution
class solution:
    #funcion para comprobar si el numero es par o impar
    def numeroparoimpar(self, x: int):
        #verifica si el residuo del numero 0 entonces dara par de lo contrario saldra impar
        if x % 2 == 0:
            return f"Tu número {x} es par"
        else:
            return f"Tu número {x} es impar"
        
#pasamos un numero mediante consola y despues mediante la funcion verificara si es numero par o impar
numero = solution()
num = int(input("ingrese el numero: "))
print(numero.numeroparoimpar(num))