class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def getConnections(self):
        return self.connections.keys()

    def setConnection(self, node):
        #weigth = 0
        self.connections[node] = 0

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

    def addEdge(self, f, t):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].setConnection(self.vertices[t])

    def __iter__(self):
        return iter(self.vertices.values())
