class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s.lower():
            if char.isalnum():
                cleaned += char
        
        front = 0
        end = len(cleaned) - 1

        while front < end:
            if cleaned[front] != cleaned[end]: 
                return False
            front += 1
            end -= 1
        
        return True