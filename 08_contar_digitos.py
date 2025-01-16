class Solution:
    def contar(self, num: int):
        return len(str(num))
    

numero = Solution()
ingresa = int(input("ingresa un numero para contarlo: "))
resultado = numero.contar(ingresa)
print(f"el numero tiene {resultado} digitos")