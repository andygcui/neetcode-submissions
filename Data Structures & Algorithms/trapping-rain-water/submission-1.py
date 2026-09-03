class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        l = [0] * len(height)
        r = [0] * len(height)
        
        l_max = 0
        r_max = 0

        for i in range(len(height)):
            if i == 0:
                continue
            if height[i-1] > l_max:
                l[i] = height[i-1]
                l_max = height[i-1]
            else:
                l[i] = l_max

        for j in reversed(range(len(height))):
            if j == len(height)-1:
                continue
            if height[j+1] > r_max:
                    r[j] = height[j+1]
                    r_max = height[j+1]
            else:
                r[j] = r_max

        for k in range(len(height)):
            water = max(0, min(l[k], r[k]) - height[k])
            total += water

        return total