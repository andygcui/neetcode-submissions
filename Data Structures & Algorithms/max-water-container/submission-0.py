class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0

        front = 0
        end = len(heights) - 1

        while front < end:
            water = (end - front) * (min(heights[front], heights[end]))
            if water > max:
                max = water
            if heights[front] < heights[end]:
                front += 1
            else:
                end -= 1
        
        return max
