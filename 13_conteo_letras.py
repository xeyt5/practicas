class Solution:
    def conteo(self, texto: str) -> dict:
        frecuencia = {}
        for char in texto:
            if char.isalpha():
                char = char.lower()
            if char in frecuencia:
                frecuencia[char] += 1
            else:
                frecuencia[char] = 1    
        return frecuencia

solucion = Solution()
entrada = input("ingrese una palabra: ")
resultado = solucion.conteo(entrada)

print("frecuencia de letra")
for letra in sorted(resultado):
    print(f"{letra}: {resultado[letra]}")