class Solution():
    def generar_fibonacci(self, n: int):
        if n <= 0:
            return "el numero debe de ser mayor"
        
        terminos = [0, 1]
        for i in range(2, n):
            siguiente = terminos[-1] + terminos[-2]
            terminos.append(siguiente)
        return terminos[:n]

solucion = Solution()
entrada = int(input("cuantos terminos quieres generar: "))
resultado = solucion.generar_fibonacci(entrada)
print(f"los primeros {entrada} terminos de fibonacci son: {resultado}")