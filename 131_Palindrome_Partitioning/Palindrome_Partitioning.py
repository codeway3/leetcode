"""https://leetcode.com/problems/palindrome-partitioning/description/"""


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for tmp in self.partition(s[i:]):
                    ret.append(s[:i].split() + tmp)  # str->list可以直接用[str]
        if ret:
            return ret
        return [[]]


# others solution
"""
Broken into several physical lines for readability, but still one logical line and just one simple statement.

def partition(self, s):
    return [[s[:i]] + rest
            for i in xrange(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])] or [[]]
这个列表生成表达式有点难读
"""
