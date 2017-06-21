class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seenNums = {}

        # Switched to enumerate after looking up
        # the fastest array loop for Python
        # https://stackoverflow.com/questions/10929724/which-is-the-most-efficient-way-to-iterate-through-a-list-in-python
        for i, num in enumerate(nums):
            if target - num in seenNums:
                return [seenNums[target - num], i]
            seenNums[num] = i

print Solution().twoSum([2, 7, 11, 15], 9)
# [0, 1]
