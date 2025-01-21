class Solution():
    def perfecto(self, numero: int):
        divisores = []
        if numero > 0:
            for i in range(1, numero // 2 + 1):
                if numero % i == 0:
                    divisores.append(i)
        else:
            print("ingrese un numero valido")
        return f"los divisores de {numero} son {divisores}"
        
        return x
numero = Solution()
entrada = int(input("ingrese un numero: "))
respuesta = numero.perfecto(entrada)
print(respuesta)