#Pedir al usuario que escriba una frase o texto.
#Mostrar:
#Cuántos caracteres tiene el texto (con espacios).
#Cuántas palabras tiene.
#Cuántas vocales hay en total.
#Cuántas veces aparece cada vocal (a, e, i, o, u).
#Mostrar el texto en mayúsculas y en minúsculas.

class AnalizadorPalabra():
    def __init__(self):
        pass

    def analizar_texto(self, texto: str) -> None:
        num_caracteres = len(texto)
        palabras = texto.split()
        num_palabras = len(palabras)

        vocales = 'AEIOUaeiou'
        conteo_vocales = {v: 0 for v in vocales}
        total_vocales = 0

        for char in texto:
            if char in vocales:
                conteo_vocales[char] += 1
                total_vocales += 1
        print(f"Número de caracteres (con espacios): {num_caracteres}")
        print(f"Número de palabras: {num_palabras}")
        print(f"Número total de vocales: {total_vocales}")
        for v in 'aeiou':
            print(f"Número de veces que aparece la vocal '{v}': {conteo_vocales[v] + conteo_vocales[v.upper()]}")
        print(f"Texto en mayúsculas: {texto.upper()}")
        print(f"Texto en minúsculas: {texto.lower()}")

analizador = AnalizadorPalabra()
texto_usuario = input("Escribe una frase o texto: ")
analizador.analizar_texto(texto_usuario)

