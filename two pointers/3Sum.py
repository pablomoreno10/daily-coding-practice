class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Okay so we want to get a list of 3 numbers that when summed together equal to 0
        #1.Lists cannot be equal
        #2.Recommended time complexity is O(n^2) and space is O(n)
        
        #Solution
        #First we want to sort the array

        nums.sort() #O(nlogn)
        #-4,-1,-1,0,1,2
        #Now leets keep track of the solutions that we already passed through with a list
        visited = []

        #We want to iterate through entire array and ignore the numbers that we already used as targets to avoid duplicates
        #In this case if target is -1 then ignore the next -1
        
        #Let's start with the left target
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]: #if a(the number/value) has already been visited then ignore it
                continue
            left=i+1 #i+1 not 0 since array is already sorted
            right=len(nums)-1
            #Now its simply a matter of two sum
            while left<right:
                three = a+nums[left]+nums[right]
                if three < 0:
                    left+=1
                elif three >0:
                    right-=1
                else:                    
                    visited.append([a, nums[left], nums[right]])
                    left+=1 #now we increase the left pointer because we do not want duplicates in our answer 
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return visited
      #Final solution O(nlogn) + O(n^2) = O(n^2)
      #Space complexity O(n)
        
