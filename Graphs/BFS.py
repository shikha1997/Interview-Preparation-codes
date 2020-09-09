from collections import defaultdict
class Graph:
    def __init__(self):
        self.graphs = defaultdict(list)
    def addEdge(self,u,v):
        self.graphs[u].append(v)
    def BFS(self,s):
        V = len(self.graphs)
        visited = [False]*V
        q = [s]
        visited[s] = True
        while(q):
            elm = q.pop(0)
            print(elm,end = " ")
            for node in self.graphs[elm]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.BFS(0)
    print()

#T.C.-O(V+E)
#S.C. - O(V)