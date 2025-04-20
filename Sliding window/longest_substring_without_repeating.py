class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        left = 0
        count = 0

        for i in range(len(s)): 
            while s[i] in track:
                track.remove(s[left])
                left +=1
            track.add(s[i])
            count = max(count, i - left + 1)
        return count
      
