#clas solution
class Solution:
    #funcion de multiplicar
    def tabla_multiplicar(self, x: int):
        #verifica si un numero es mayor que 0
        if x > 0:
            for i in range(1, 11):
                print(f"{x} x {i} = {x * i}")
        #si es menor que cero coloca un mensaje que dice que es mejor a cero
        else:
            print("el numero debe de ser mayor a 0")

numero = Solution()
x = int(input("que numero deseas multiplicar? "))
numero.tabla_multiplicar(x)
