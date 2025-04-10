class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort() #sort elements
        n = len(nums) #get the lenght of array
        return nums[n//2] #the majority element will appear more than n/2 times and it always exists - // for int
