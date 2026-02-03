# 37. Encontrar el número faltante en una lista
class Solution():
    def numero_faltante(self, nums, n):
        suma_total = n * (n + 1) // 2
        suma_lista = sum(nums)
        return suma_total - suma_lista
    

solucion = Solution()
nums = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]  
n = 10
faltante = solucion.numero_faltante(nums, n)
print(f"El número faltante es: {faltante}")  