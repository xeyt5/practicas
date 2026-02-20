#Dado un arreglo de enteros nums y un entero k, devuelve los k elementos más frecuentes.

#🔹 Debe ser mejor que O(n log n)
#🔹 No puedes simplemente ordenar todo el arreglo
#🔹 Ideal: usar heap o bucket sort
#sin usar librerias externas
class Solution():
    def frecuencinum(self, nums, k):
        frecuencia = {}
        for num in nums:
            if num in frecuencia:
                frecuencia[num] += 1
            else:
                frecuencia[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frecuencia.items():
            buckets[freq].append(num)
        resultado = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                resultado.append(num)
                if len(resultado) == k:
                    return resultado
        return resultado
    
sol = Solution()
print(sol.frecuencinum([1,1,1,2,2,3], 2))

