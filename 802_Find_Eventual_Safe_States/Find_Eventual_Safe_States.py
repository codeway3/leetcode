"""https://leetcode.com/problems/find-eventual-safe-states/description/"""


class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        rmap = collections.defaultdict(list)
        outdgree = [0]*len(graph)
        queue = []
        # 边反向存储
        for i in range(len(graph)):
            nlst = graph[i]
            for j in nlst:
                outdgree[i] += 1
                rmap[j].append(i)
            if outdgree[i] == 0:
                queue.append(i)
        # 取出度为0的点加入队列 最后排序输出
        for i in queue:
            for j in rmap[i]:
                outdgree[j] -= 1
                if outdgree[j] == 0:
                    queue.append(j)
        return sorted(queue)


# others solution which I referred
"""
Your ret and queue are exactly the same thing. Keep only one:

def eventualSafeNodes(self, graph):
        n = len(graph)
        out_degree = [0] * n
        in_nodes = collections.defaultdict(list) 
        queue = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0: queue.append(i)
            for j in graph[i]: in_nodes[j].append(i)  
        for term_node in queue:
            for in_node in in_nodes[term_node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0: queue.append(in_node)
        return sorted(queue)
"""