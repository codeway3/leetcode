"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
"""


# 分析清楚逻辑 找最大和第二大的数即可 图省事没有再给变量起名了 my fault
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, v1, v2 = 0, 0, 0
        for i, j in enumerate(nums):
            if j >= v1:
                p1, v1, v2 = i, j, v1
            elif j >= v2:
                v2 = j
        if v1 >= v2 * 2:
            return p1
        else:
            return -1
