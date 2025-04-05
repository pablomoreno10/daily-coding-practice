class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count the frequency of each number using a dictionary
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1  # Increment count if already seen
            else:
                count[num] = 1   # Initialize count if first time seeing the number
        #Convert the dictionary into a list of [frequency, number] pairs
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])  # Store as [frequency, number] to make sorting easier
        #Sort the list by frequency (ascending)
        arr.sort()  # After sorting, most frequent elements are at the end
        #Pop the last k elements from the sorted list (they're the most frequent)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  # Pop the most frequent and add the number (not the count) to the result
        #Return the top k frequent elements
        return res

