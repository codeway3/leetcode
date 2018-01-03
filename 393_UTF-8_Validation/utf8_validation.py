"""
https://leetcode.com/problems/utf-8-validation/description/
"""


# my solution
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        flag = 0
        for d in data:
            tmp = [0, 0, 0]
            d = d // 8
            for i in range(5):
                tmp.append(d % 2)
                d //= 2
            tmp.reverse()
            if flag > 0:
                if tmp[0] == 1 and tmp[1] == 0:
                    flag -= 1
                    continue
                else:
                    return False
            else:
                if tmp[0] == 0:
                    flag = 0
                elif tmp[0] == 1 and tmp[1] == 1 and tmp[2] == 0:
                    flag = 1
                elif tmp[0] == 1 and tmp[1] == 1 and tmp[2] == 1 and tmp[3] == 0:
                    flag = 2
                elif tmp[0] == 1 and tmp[1] == 1 and tmp[2] == 1 and tmp[3] == 1 and tmp[4] == 0:
                    flag = 3
                else:
                    return False
        if flag > 0:
            return False  # 开始忘了判定这种情况了
        else:
            return True


# other solution
# 使用位运算和二进制写法如0bxxxxx直接进行比对 不进行人工进制转换
"""
def check(nums, start, size):
    for i in range(start + 1, start + size + 1):
        if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
    return True

class Solution(object):
    def validUtf8(self, nums, start=0):
        while start < len(nums):
            first = nums[start]
            if   (first >> 3) == 0b11110 and check(nums, start, 3): start += 4
            elif (first >> 4) == 0b1110  and check(nums, start, 2): start += 3
            elif (first >> 5) == 0b110   and check(nums, start, 1): start += 2
            elif (first >> 7) == 0:                                 start += 1
            else:                                                   return False
        return True
"""
