# https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150
# 시간: 58분
# 난이도: medium
# 설명: dfs에서 edge를 찾은 다음 카피

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        s = []
        clone_stack = []
        for neig in node.neighbors:
            s.append((node, neig))
        visited = set()

        while s:
            src, dst = s.pop()
            visited.add((src, dst))
    
            for neig in src.neighbors:
                if not (src, neig) in visited:
                    s.append((src, neig))
            for neig in dst.neighbors:
                if not (dst, neig) in visited:
                    s.append((dst, neig))


        node_dic = {}
        new_node_dic = {}
        for s, d in visited:
            # print("val: ", s.val, d.val)
            node_dic[s.val] = s
            node_dic[d.val] = d
            new_node_dic[s.val] = Node(val=s.val)
            new_node_dic[d.val] = Node(val=d.val)

        for k in node_dic.keys():
            # print(k)
            vn = node_dic[k]
            new_node = new_node_dic[k]
            for neig in vn.neighbors:
                new_node_dic[k].neighbors.append(new_node_dic[neig.val])
        
        # print(new_node_dic, node.val, node.neighbors)
        if node.val in new_node_dic:
            return new_node_dic[node.val]
        else:
            return Node(node.val)
            