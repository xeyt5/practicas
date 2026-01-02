class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map.keys():
                if not stack or stack[-1] != map[char]:
                    return False
                stack.pop()
        return not stack
Sol = Solution()
entrada = "()[{"
print(Sol.isValid(entrada))