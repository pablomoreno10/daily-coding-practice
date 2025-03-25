class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths are different
        # If they are, s and t cannot be anagrams
        if len(s) != len(t):
            return False

        # Create two dictionaries to count character frequencies
        countS, countT = {}, {}

        # Loop through the strings
        for i in range(len(s)):
            # For each character in s and t, update the frequency count
            # If the character is not already in the dictionary, use 0 as default
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare the two dictionaries
        # If they are equal, s and t are anagrams
        return countS == countT
