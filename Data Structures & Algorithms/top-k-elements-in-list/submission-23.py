class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        ordered = sorted(freq, key=lambda num: freq[num], reverse=True)
        
        return ordered[:k]
