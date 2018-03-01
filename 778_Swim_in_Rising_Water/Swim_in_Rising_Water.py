"""
https://leetcode.com/problems/swim-in-rising-water/description/
"""


class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        l, r = grid[0][0], n * n - 1

        def reachable(target):
            bfs = [(0, 0)]
            seen = set((0, 0))
            for x, y in bfs:
                if grid[x][y] <= target:
                    if x == y == n - 1:
                        return True
                    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= x + i < n and 0 <= y + j < n and (x + i, y + j) not in seen:
                            seen.add((x + i, y + j))
                            bfs.append((x + i, y + j))
            return False

        while l < r:
            mid = (l + r) // 2
            if reachable(mid):
                r = mid
            else:
                l = mid + 1
        return r

# others solutions
# 我开始写的也是二分检验的思路 但是后来运行时错误但是没有返回错误信息 就参考了讨论中的写法
# 另一种方法如下 使用内建的最小堆函数


"""
class Solution:
    def swimInWater(self, grid):
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))
"""
