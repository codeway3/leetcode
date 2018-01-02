"""
https://leetcode.com/problems/teemo-attacking/description/
"""


# my solution
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # timeSeries.sort() 1.注意题目里写明了升序 不用再进行排序了
        ans = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i]+duration > timeSeries[i+1]:
                ans += timeSeries[i+1] - timeSeries[i]
            else:
                ans += duration
        if len(timeSeries) > 0:  # 2.开始没有加这条判定 当timeSeries为[]时答案会错误
            ans += duration
        return ans


# others solution
"""
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans
参考第2条 他使用了减法来计算ans 不会发生多算一个duration的情况
"""

"""
    def findPoisonedDuration(self, s, d):
        return sum(min(d, b - a) for a, b in zip(s, s[1:] + [10e7]))
极简写法 注意复习一下zip用法
"""
