from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V =V
        self.graphs = defaultdict(list)

    def addEdge(self,u,v):
        self.graphs[u].append(v)

    def DFSutil(self,v,visited):
        visited[v] = True
        print(v,end = "")
        for i in self.graphs[v]:
            if visited[i] == False:
                self.DFSutil(i,visited)


    def finishtimefilling(self,v,visited,stack):
        visited[v] = True
        for i in self.graphs[v]:
            if visited[i] == False:
                self.finishtimefilling(i,visited,stack)
        stack = stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graphs:
            for j in self.graphs[i]:
                g.addEdge(j,i)

        return g
    def printSCC(self):
        stack = []
        visited = [False]*(self.V)
        for i in range(self.V):
           # print(len(visited))
            if visited[i] == False:
                g.finishtimefilling(i, visited, stack)

        gr = g.transpose()
        visited = [False]*(self.V)
        while(stack):
            i = stack.pop()
            if visited[i]== False:
                gr.DFSutil(i,visited)
                print()


if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1,0)
    g.addEdge(0,2)
    g.addEdge(2,1)
    g.addEdge(0,3)
    g.addEdge(3,4)

    g.printSCC()








