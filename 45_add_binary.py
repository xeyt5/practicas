#Given two binary strings a and b, return their sum as a binary string.
#Input: a = "11", b = "1"
#Output: "100"

class Solution():
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            
            carry = sum // 2
            result.append(str(sum % 2))
        
        return ''.join(reversed(result))
    
sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))
