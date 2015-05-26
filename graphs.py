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

    def __iter__(self):
        return iter(self.connections.values())


class Graph:
    def __init__(self):
        self.vertices ={}
        self.numVertices = 0

    def addNode(self, key):
        self.numVertices += 1
        node = Vertex(key)
        self.vertices[key] = node
        return node

    def addEdge(self, f, t):
        if f not in self.vertices:
            nv = self.addNode(f)
        if t not in self.vertices:
            nv = self.addNode(t)
        self.vertices[f].setConnection(self.vertices[t])

    def getEdges(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
