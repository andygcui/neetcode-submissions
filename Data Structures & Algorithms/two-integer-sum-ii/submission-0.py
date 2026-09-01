class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = []
        front = 0
        end = len(numbers) - 1

        sum = numbers[front] + numbers[end]
        while sum != target:
            if sum < target:
                front += 1
            else:
                end -= 1
            sum = numbers[front] + numbers[end]
        
        sol.append(front+1)
        sol.append(end+1)

        return sol