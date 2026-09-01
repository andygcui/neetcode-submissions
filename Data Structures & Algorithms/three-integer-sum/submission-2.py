class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            first = i + 1
            end = len(nums) - 1
            target = -1 * nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while first < end:
                sum = nums[first] + nums[end]

                if sum < target:
                    first += 1
                elif sum > target:
                    end -= 1
                else:
                    output.append([nums[i], nums[first], nums[end]])
                    first += 1
                    end -= 1

                    while first < end and nums[end] == nums[end+1]:
                        end -= 1
        return output
            
            