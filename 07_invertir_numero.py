#craer un programa donde se tenga que invertir el numero
class Solution:
    #funcion invertir numero
    def invertir(self, num: int):
        #retorna el numero ingresado pero invertido
        return int(str(num)[::-1])
#asignacion y llamado de la funcion    
numero = Solution()
invertir = int(input("ingrese un numero: "))
resultado = numero.invertir(invertir)
print(f"el numero invertido es: {resultado}")
    
