class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #In order to have a profit the list must not be ordered in decreasing order
        #If it is ordered in decreasing order, has no numbers or one number return 0
        left, right = 0,1
        solution = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit  = prices[right]- prices[left]
                solution = max(solution, profit)
            else: 
                left = right #left has to be smaller 
            
            right +=1
        return solution
            
