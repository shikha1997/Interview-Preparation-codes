from collections import defaultdict
class Graph:
    def __init__(self):
        self.graphs = defaultdict(list)
    def addEdge(self,u,v):
        self.graphs[u].append(v)

    def DFSUtil(self,v,visited):
        visited[v] = True
        print(v,end = " ")
        for i in self.graphs[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    def DFS(self):
        V = len(self.graphs)
        visited = [False]*V
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i,visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS()
    print()

#T.C.-O(V+E)
#S.C. - O(V)