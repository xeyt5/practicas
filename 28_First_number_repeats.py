class Soulution:
    def first_repeated_number(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return None
    
    def first_number_not_repeated(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in nums:
            if count[num] == 1:
                return num
        return None
    
example = Soulution()
print(example.first_repeated_number([2, 3, 1, 5, 3, 2]))  
print(example.first_number_not_repeated([2, 3, 1, 5, 3, 2]))