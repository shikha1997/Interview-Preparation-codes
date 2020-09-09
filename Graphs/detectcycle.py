#detect cycle in undirected graph
from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graphs = defaultdict(list)
#     def addEdge(self,u,v):
#         self.graphs[u].append(v)
#         self.graphs[v].append(u)
#
#     def cycleutil(self,v,visited,parent):
#         visited[v] = True
#         for i in self.graphs[v]:
#             if visited[i] == False:
#                 if (self.cycleutil(i, visited, v)):
#                     return True
#             elif parent != i:
#                 return True
#
#         return False
#
#     def isCycle(self):
#         visited = [False for i in range(len(self.graphs))]
#         for i in range(len(self.graphs)):
#             if visited[i] == False:  # Don't recur for u if it is already visited
#                 if (self.cycleutil(i, visited, -1)) == True:
#                     return True
#
#         return False

##Directed Graph

class Graph:
    def __init__(self):
        self.graphs = defaultdict(list)
    def addEdge(self,u,v):
        self.graphs[u].append(v)

    def cycleutil(self,v,visited,recstk):
        visited[v] = True
        recstk[v] = True
        for i in self.graphs[v]:
            if visited[i] == False:
                if (self.cycleutil(i, visited, recstk)):
                    return True
            elif recstk[i]:
                return True

        return False

    def isCycle(self):
        visited = [False for i in range(len(self.graphs))]
        recstk = [False for i in range(len(self.graphs))]
        for i in range(len(self.graphs)):
            if visited[i] == False:  # Don't recur for u if it is already visited
                if (self.cycleutil(i, visited, recstk)) == True:
                    return True

        return False

if __name__ == '__main__':
    g = Graph()
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)


    if g.isCycle():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
T.C. - O(V+E)
S.C. - O(V)
