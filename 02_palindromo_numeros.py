#9. palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x) 
        return num == num[::-1]

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(423))

