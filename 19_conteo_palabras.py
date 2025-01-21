class Solution:
    def conteo(self, texto: str) -> int:
        if not texto.strip():
            return 0
        palabras = texto.split()
        return len(palabras)


cadena = Solution()
entrada = input("ingresa tu frase: ")
respuesta = cadena.conteo(entrada)
if respuesta == 0:
    print("ingresa una respuesta correcta")
else:
    print(f"tu frase tiene  {respuesta} palabras")
