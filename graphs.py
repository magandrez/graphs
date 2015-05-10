#!graphs/bin/python
import random

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in
        self.connectedTo])

    def getConnections(self):
        return self.connections.keys()

    def setConnection(self, node, weight=0):
        self.connections[node] = weight

    def getKey(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertices ={}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVert = Vertex(key)
        self.vertices[key] = newVert
        return newVert

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].setConnection(self.vertices[t])

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


g = Graph()
print("Enter the number of nodes in the graph: ")
nodes = int(input())
keys = [int(i) for i in range(0, nodes)]
for i in range(nodes):
    g.addVertex(keys[i])

print("Enter the number of edges in the graph: ")
edges = int(input())

for i in range(edges):
    node1 = random.randrange(len(keys))
    node2 = random.randrange(len(keys))
    g.addEdge(node1, node2)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getKey(), w.getKey()))
