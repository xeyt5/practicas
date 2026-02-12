class Solution():
    def groupAnagrams(self, strs):
        anagram_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []
            anagram_dict[sorted_word].append(word)
        return list(anagram_dict.values())
    
#example usage
solution = Solution()
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(input_strs))