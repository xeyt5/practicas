class Solution():
    def longestCommonPrefix(self, lista):
        if not lista:
            return ""
        
        prefix = lista[0]
        for palabra in lista[1:]:
            while not palabra.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

Sol = Solution()
entrada = ["flower", "flow", "flight"]
print(Sol.longestCommonPrefix(entrada))  