"""https://leetcode.com/problems/k-diff-pairs-in-an-array/description/"""


class Solution:
    # 这个方法刚刚不超时
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        s = sorted(list(set(nums)))
        if k > 0:
            for num in s:
                if num + k in s:
                    ans += 1
        elif k == 0:
            for num in s:
                if nums.count(num) > 1:
                    ans += 1
        return ans


# others solution
"""
def findPairs(self, nums, k):
        c = collections.Counter(nums)
        return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
# Counter用法参考 http://www.pythoner.com/205.html
"""
