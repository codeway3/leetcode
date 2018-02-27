"""
https://leetcode.com/problems/accounts-merge/description/
"""


# Difficulty: medium
# my solution 勉强不超时
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        acc_len = len(accounts)
        # 注意这里 每一条信息内 也是可能有邮件地址的冗余的 需要去重
        for i in range(acc_len):
            accounts[i] = accounts[i][:1] + sorted(list(set(accounts[i][1:])))
        flag = [True] * acc_len
        # 列表转集合 去重 集合合并 转回列表 给被合并的列表打上标记
        for i in range(acc_len):
            for j in range(acc_len):
                if i < j and flag[i] and flag[j] and accounts[i][0] == accounts[j][0]:
                    tmpn = list([accounts[i][0]])
                    tmp1 = accounts[i][1:]
                    tmp2 = accounts[j][1:]
                    tmpp = set(tmp1) | set(tmp2)
                    if len(tmpp) < len(tmp1) + len(tmp2):
                        # 这里注意 合并的方向 i j 交换会出问题 可能导致合并不完全
                        accounts[j] = tmpn + list(tmpp)
                        flag[i] = False
        ans = []
        for i in range(acc_len):
            if flag[i]:
                ans.append(accounts[i][:1] + sorted(list(set(accounts[i][1:]))))  # 合并后的去重
        return ans


# others solution
# 题解给出的两种方法，一种是抽象成图，用dfs，另一种（如下）是并查集
"""
Create two maps for fast query

email_to_id - email to the id unique for each email which is also used as the index for our disjoint set
id_to_name - the unique id to name (also means email to name)
For the disjoint set part, we use the negative values represent the size of the set, when we union two sets we link smaller set to bigger set, this potentially give us a relatively shorter path.
However if we call find more frequently this shouldn’t matter too much.
Also we are build the data structure on the fly by append id to ds every time we see a new email.

class Solution(object):
    def accountsMerge(self, accounts):
        
        def find(a):
            if ds[a] < 0:
                return a
            ds[a] = find(ds[a])
            return ds[a]
        
        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                if ds[a] < ds[b]:
                    ds[a] += ds[b]
                    ds[b] = a
                else:
                    ds[b] += ds[a]
                    ds[a] = b

        c, ds, email_to_id, id_to_name = 0, [], {}, {}
        for account in accounts:
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = c
                    id_to_name[c] = account[0]
                    ds.append(-1)
                    c += 1
                union(email_to_id[account[1]], email_to_id[email])
                
        res = {}
        for email, id in email_to_id.items():
            master = find(id)
            res[master] = res.get(master, []) + [email]
        return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]
"""
