# Kruskal's MST algorithm
'''
Used edge list to represent the graph as it is simpler to work with in kruskals algorithm (where we add edges to the spanning tree).
'''
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def printMST(self, mst):
        print("Edge \tWeight")
        for i in range(len(mst)):
            print(mst[i][0], "-", mst[i][1], "\t", mst[i][2])

    def kruskalMST(self):
        visited = []
        mst = []
        self.graph = sorted(self.graph, key = lambda x: x[2])
        for g in self.graph:
            if g[0] not in visited and g[1] not in visited:
                visited.append(g[0])
                visited.append(g[1])
                mst.append(g)
            elif g[0] in visited and g[1] not in visited:
                visited.append(g[1])
                mst.append(g)
            elif g[0] not in visited and g[1] in visited:
                visited.append(g[0])
                mst.append(g)
            else:
                continue
        self.printMST(mst)

graph = Graph(4)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 2, 3)
graph.addEdge(1, 2, 1) 
graph.kruskalMST()
