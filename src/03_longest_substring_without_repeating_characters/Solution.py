class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        current = 0
        best = 0
        seen = {}
        while current < len(s):
          char = s[current]
          if char in seen and seen[char] >= start:
            start = seen[char] + 1
            seen[char] = current
          else:
            seen[char] = current
          best = max(best, current - start + 1)
          current+=1
        return best

print Solution().lengthOfLongestSubstring("This is a test.");
# 5
