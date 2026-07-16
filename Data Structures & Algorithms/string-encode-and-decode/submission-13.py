class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            num = len(strs[i])
            encoded += (str(num) + "#")
            encoded += strs[i]
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            
            num = int(s[i:j])

            decoded.append(s[j+1:j+num+1])
            i = j + num + 1
        
        return decoded



