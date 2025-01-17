class Solution():
    def promedio(self, numeros: int):
        if not numeros:
            return "lista vacia"
        return sum(numeros) / len(numeros)
    
numero = Solution()
entrada = input("ingrese los numeros separados por una coma: ")

try:
    lista_numeros = list(map(int, entrada.split(",")))
    resultado = numero.promedio(lista_numeros)
    print(f"el promedio es {resultado}")
    
except ValueError:
    print("ingresa datos validos")
    
