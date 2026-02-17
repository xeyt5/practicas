class Solution():
    def twosum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
    

solution = Solution()
input_nums = [2, 7, 11, 15]
input_target = 9
print(solution.twosum(input_nums, input_target))