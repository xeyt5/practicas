class Solution():
    def eliminacion_vocales(self, texto: str):
        vocales = "aeiouAEIOU"
        resultado = ""
        
        for char in texto:
            if char not in vocales:
                resultado += char
        return resultado
        
                    
    
    
palabra = Solution()
entrada = input("ingresa la palabra: ")
resultado = palabra.eliminacion_vocales(entrada)
print(resultado)