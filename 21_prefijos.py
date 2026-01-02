class Solution():
    def prefixCount(self, lista):
        if not lista:
            return ""
        
        prefix = lista[0]
        for palabra in lista[1:]:
            while not palabra.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

Solution = Solution()
entrada = ["ra", "rana", "raton"]
print(Solution.prefixCount(entrada))  