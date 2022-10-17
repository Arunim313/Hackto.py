class Solution:
    def lengthOfLongestSubstring(self, s):
        StartingPoint =0
        MAXIMUM_LENGTH = 0
        CHARACTER_USED = {}
        
        for inpu in range(len(s)):
            if s[inpu] in CHARACTER_USED and StartingPoint <= CHARACTER_USED[s[inpu]]:
                StartingPoint = CHARACTER_USED[s[inpu]] + 1
            else:
                MAXIMUM_LENGTH = max(MAXIMUM_LENGTH, inpu - StartingPoint + 1)

            CHARACTER_USED[s[inpu]] = inpu

        return MAXIMUM_LENGTH
        
        '''Runtime: 70 ms, faster than 89.96% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 49.57% of Python3 online submissions for Longest Substring Without Repeating Characters.'''
