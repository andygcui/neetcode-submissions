class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        uniques = {}
        starting_index = 0

        for i in range(len(s)):
            if s[i] in uniques and uniques[s[i]] >= starting_index:
                index = uniques.get(s[i])
                starting_index = index + 1
                
            uniques[s[i]] = i
        
            if (i - starting_index + 1) > longest:
                longest = i - starting_index + 1

        return longest