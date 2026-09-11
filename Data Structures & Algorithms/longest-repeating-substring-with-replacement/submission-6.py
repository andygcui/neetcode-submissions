class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        start = 0
        frequencies = {}
        longest = 0

        for end in range(len(s)):
            frequencies[s[end]] = frequencies.get(s[end], 0) + 1

            max_frequency = max(frequencies.values())
            replacements = (end - start + 1) - max_frequency

            while replacements > k:
                frequencies[s[start]] -= 1
                start += 1

                max_frequency = max(frequencies.values())
                replacements = (end - start + 1) - max_frequency

            longest = max(longest, end - start + 1)

        return longest