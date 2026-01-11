class Solution():
    def frequencySort(self, nums):
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        sorted_nums = sorted(nums, key=lambda x: (frequency[x], -x))
        return sorted_nums
    
example = Solution()
print(example.frequencySort([4, 4, 1, 2, 2, 3, 3, 3]))  