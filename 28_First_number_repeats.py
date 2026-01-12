class Soulution:
    def first_repeated_number(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return None
    
example = Soulution()
print(example.first_repeated_number([2, 3, 1, 5, 3, 2]))  