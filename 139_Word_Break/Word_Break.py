"""
https://leetcode.com/problems/word-break/description/
"""


# 开始写了个暴力dfs 超时 改用DP直接过了
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l = len(s)
        f = [False] * (l + 1)
        f[0] = True
        for i in range(l):
            if f[i]:
                for j in wordDict:
                    if s[i:i+len(j)] == j:
                        f[i+len(j)] = True
        return f[l]


# others solution
# 逆向dp
"""
# ok[i] tells whether s[:i] can be built.

def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]
"""
