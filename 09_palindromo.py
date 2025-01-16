#clase solucion
class Solution:
    #funcion para invetir la palabra
    def palindromo(self, paralabra: str):
        #verifica si la palabra es igual
        if paralabra == paralabra [::-1]:
            print ("es un palindromo")
        else:
            print("no es palindromo")

#instancia de la clase
palabra_invertida = Solution()
#solicita la palabra al ususario y elimina espacios al inicio y al final
invertir = input("ingrese la palabra: ").strip()
#convierte la cadena en minusculas
palindromo = invertir.lower()
#verifica si es un palindromo
pal = palabra_invertida.palindromo(palindromo)
    
