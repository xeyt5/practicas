class Solution():
    def factorial(self, num: int) -> str:
        if num == 0:
            return "el factorial de 0 es 1"
        if num < 0:
            return "no se pueden numeros negativos"
        
        resultado = 1          
        for i in range(1, num+1):
            resultado *= i 
        return f"el factorial de {num} es {resultado}: "

fac = Solution()
entrada = int(input("ingresa el numero: "))
resultado = fac.factorial(entrada)
print(resultado)