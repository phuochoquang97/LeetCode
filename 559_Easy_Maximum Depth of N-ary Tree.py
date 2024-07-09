"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:  # empty tree
            return 0

        q = deque()  # keep track of all nodes in the same level
        depth = 1  # root level included

        for child in root.children:
            q.append(child)

        while q:
            l = len(q)
            for i in range(l):  # iterate all nodes in the same level
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            depth += 1

        return depth
