class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_prod = 1
        non_zero_prod = 1
        zero_count = 0
        for num in nums:
            if num != 0: 
                total_prod *= num
                non_zero_prod *= num
            else: 
                zero_count += 1
                total_prod *= num
        
        print(zero_count)
        print(total_prod)
        print(non_zero_prod)
                

        for i in range(len(nums)):
            if zero_count < 2:
                if nums[i] != 0:
                    nums[i] = total_prod // nums[i]
                else:
                    nums[i] = non_zero_prod
            
            else:
                nums = [0]*(len(nums))

        return nums

        
        