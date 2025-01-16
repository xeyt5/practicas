class Solution:
    def contador_vocales(self, palabra: str):
        contador = 0
        for vocales in palabra:
            if vocales in "aeiou":
                contador += 1
        return contador
    
vocales = Solution()
entrada = input("ingrese una palabra: ").strip()
if entrada:
    vocales = vocales.contador_vocales(entrada.lower())
    print(f"la palabra {entrada} tiene {vocales} vocales")
else:
    print("no ingresaste una palabra valida")    
