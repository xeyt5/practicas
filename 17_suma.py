class Solution ():
    def suma(self, numeros: int):
        suma = 0
        cadena = str(numeros)
        for i in cadena:
            suma += int(i)        
        return suma


digitos = Solution()
entrada = int(input("ingrese la cadena de numeros: "))
respuesta = digitos.suma(entrada)
print(f"la suma de los numeros es {respuesta}")
