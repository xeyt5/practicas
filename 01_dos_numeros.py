#1. Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#code
class Solution:
    def twoSum(self, nums, target):
        # diccionario para almacenar los números vistos y sus índices
        seen = {}
        # iterar sobre la lista
        for i, num in enumerate(nums):
            # calcular la diferencia necesaria para llegar al target
            complement = target - num
            # verificar si la diferencia ya está en el diccionario
            if complement in seen:
                return [seen[complement], i]
            # si no, almacenar el número actual con su índice
            seen[num] = i
# ejemplo
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target)) 

