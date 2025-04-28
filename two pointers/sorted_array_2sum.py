class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #To solve this problem, a simple two pointer approach can suffice
        #We just need to keep track of the sum of left and right in relation to target since the array is already sorted
        right = len(numbers) - 1
        left = 0
        while left < right:
            # If sum is greater than target, move right pointer left
            if numbers[left] + numbers[right] > target:
                right -= 1
            # If sum is smaller than target, move left pointer right
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:  #When sum equals target, return the indices
                return [left + 1, right + 1] #There is exactly one solution so this is enough
