class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(a,b):
            if len(a) != len(b):
                return False
            counts = [0]*26
            for i in range(len(a)):
                counts[ord(a[i])-ord('a')] += 1
                counts[ord(b[i])-ord('a')] -= 1
            
            for value in counts:
                if value != 0:
                    return False
            
            return True


        uniques = []
        for string in strs:
            found = False
            for unique in range(len(uniques)):
                if is_anagram(string, uniques[unique][0]):
                    uniques[unique].append(string)
                    found = True
                    break
            if not found:
                uniques.append([string])

        return uniques
        
    