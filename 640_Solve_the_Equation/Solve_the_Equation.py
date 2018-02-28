"""
https://leetcode.com/problems/solve-the-equation/description/
"""

# Difficulty: Medium
# my solution
class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        list = equation.split('=')
        str1 = '+' + list[0] + '+'
        str2 = '+' + list[1] + '+'
        x_coef = 0
        cons = 0
        # 要细心 注意存在0x=???这种情况
        tmp = 0
        neg = 1
        x_flag = 0
        # 建议抽象出函数对左右切分出的字符串进行操作
        for i in range(len(str1)):
            if str1[i] in ['-', '+']:
                tmp = tmp * neg
                if x_flag == 1:
                    x_coef += tmp
                else:
                    cons += tmp
                tmp = 0
                neg = 1
                x_flag = 0
            elif str1[i] == 'x':
                if tmp == 0 and str1[i-1] in ['-', '+']:
                    tmp = 1
                x_flag = 1
            else:
                tmp = tmp * 10 + int(str1[i])
            if str1[i] == '-':
                neg = -1
        for i in range(len(str2)):
            if str2[i] in ['-', '+']:
                neg *= -1
                tmp = tmp * neg
                if x_flag == 1:
                    x_coef += tmp
                else:
                    cons += tmp
                tmp = 0
                neg = 1
                x_flag = 0
            elif str2[i] == 'x':
                if tmp == 0 and str2[i-1] in ['-', '+']:
                    tmp = 1
                x_flag = 1
            else:
                tmp = tmp * 10 + int(str2[i])
            if str2[i] == '-':
                neg = -1
        cons *= -1
        if x_coef == 0 and cons == 0:
            return 'Infinite solutions'
        elif x_coef == 0:
            return 'No solution'
        else:
            return 'x=' + str(cons//x_coef)


# others solution
# 主流解法 模拟拆分 或者使用正则
# 下面这个写法比我写的清晰多了 我写的时候也没太想好 写烂了
"""
Here I used helper to convert left and right equations into the coef and const which represent the coefficient of x and remaining constant.

class Solution(object):
    def solveEquation(self, equation):
        def helper(s):
            sign, n = 1, len(s)
            # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
            i = coef = const = 0
            while i < n:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i].isdigit():
                    j = i
                    while j < n and s[j].isdigit():
                        j += 1
                    tmp = int(s[i:j])
                    if j < n and s[j] == 'x':
                        coef += tmp * sign
                        j += 1
                    else:
                        const += tmp * sign
                    i = j-1
                else:
                    coef += 1 * sign
                i += 1
            return coef, const
            
        left, right = equation.split('=')
        k1, b1 = helper(left)
        k2, b2 = helper(right)
        # k1x + b1 = k2x + b2
        ans = 'x=' + str((b2 - b1) / (k1 - k2)) if k1 != k2 and b1 != b2 \
              else "Infinite solutions" if k1 == k2 and b1 == b2 \
              else "No solution" if b2 != b1 else 'x=0'
        return ans
"""
