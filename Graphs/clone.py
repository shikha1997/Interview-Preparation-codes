"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# T.C.-=O(V+E)
# S.C. = O(V)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        visited = {}
        q = collections.deque([node])
        visited[node] = Node(val=node.val)
        while (q):
            t = q.popleft()
            for neigh in t.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    q.append(neigh)
                visited[t].neighbors.append(visited[neigh])
        return visited[node]
