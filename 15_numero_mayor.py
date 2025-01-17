class Solution():
    def mayor(self, numero):
        if not numero:
            return "lista vacia"
        return max(numero)
        
    
numeros = Solution()
entrada = int(input("ingresa los numeros: "))
try:
    lista_numeros = list(map(int, entrada.split(",")))
    resultado = numeros.mayor(entrada)
    print(f"el numero mayor es: {resultado}")
except ValueError:
    print("por favor ingrese numeros validos")