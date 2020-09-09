from collections import defaultdict
class Graph:
    def __init__(self):
        self.graphs = defaultdict(list)
    def addEdge(self,u,v):
        self.graphs[u].append(v)
        self.graphs[v].append(u)


    def isBipartite(self,pos,color,visited):
        for i in self.graphs[pos]:
            if visited[i] == False:
                color[i] = not color[pos]
                visited[i]= True
                if (self.isBipartite(i,color,visited)==False):
                    return False
            elif color[i]==color[pos]:
                return False
        return True


    def bipartite(self):
        color = [-1]*len(self.graphs)
        visited = [False]*len(self.graphs)
        color[0] = 1
        visited[0] = True
        if self.isBipartite(0,color,visited):
            return True
        else:
            return False

if __name__ == '__main__':
    g = Graph()
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    print(g.bipartite())
