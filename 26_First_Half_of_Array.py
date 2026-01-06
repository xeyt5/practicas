from typing import List

class Solution:
    def reverseFirstHalf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        half = n // 2
        reversed_half = nums[half-1::-1] + nums[half:]
        return reversed_half
    
    def changeOrder(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mitad = n // 2
        nueva_lista = nums[mitad:] + nums[:mitad]
        return nueva_lista
 

example = Solution()
print(example.reverseFirstHalf([1, 2, 3, 4, 5, 6]))


example2 = Solution()
print(example.changeOrder([1, 2, 3, 4, 5, 6]))
