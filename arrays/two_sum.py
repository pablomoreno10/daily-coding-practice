# Problem: Two Sum
# Difficulty: Easy
#https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_set = {} 

        for i,n in enumerate(nums): #iterate through nums using enumerate i index, n value
            diff = target - n # diff between target and value of i
            if diff in hash_set: # if diff is in hashset 
                return [hash_set[diff],i] #return index of diff and of the number iterated
            hash_set[n] = i
