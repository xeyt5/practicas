class Solution():
    def numero_primo(self, num:int):
        if num < 2:
            return f"el {num} es menor a 2"
        
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return f"el {num} no es primo"
        return f"el {num} es primo"


numero = Solution()
entrada = int(input("ingresa el nuemro: "))
resultado = numero.numero_primo(entrada)
print(resultado)