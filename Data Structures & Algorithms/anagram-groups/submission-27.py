class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # default 
        uniques = defaultdict(list)

        for s in strs:
            count = [0]*26

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            uniques[tuple(count)].append(s)
            # need to change to tuple cause lists can't be keys
        
        return list(uniques.values())