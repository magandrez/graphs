from model import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy import *
from graphs import *
import random


def generate_graph():
    """
    This function generates a pseudo-random non-directed graph based on the
    number of nodes and edges requested by the user.

    Nodes are named in order from 0 up to the number input by the user.

    Edges are created upon the number input by the user. If
    # of edges is < the number of nodes, all edges are pseudo-randomly created.
    The range of the random function to generate nodes for the edges relies on the
    number of nodes previously inserted by the user, making the process less random.
    """
    g = Graph()
    print("Enter the number of nodes in the graph: ")
    nodes = int(input())
    keys = [int(i) for i in range(0, nodes)]
    for i in range(nodes):
        g.addVertex(keys[i])

    print("Enter the number of edges in the graph: ")
    edges = int(input())
    for i in range(edges):
        #using random.randrange()
        #used the number of nodes as top number of edges to be generated
        node1 = random.randrange(len(keys))
        node2 = random.randrange(len(keys))
        g.addEdge(node1, node2)
    print("Below, the list of all generated nodes, with its edges listed in the format (a, b) underneath.")
    for vert in g:
        #print the node ID
        print(vert.getKey())
        for e in vert.getConnections():
            #print the edge
            print("( %s , %s )" % (vert.getKey(), e.getKey()))

    return g

def save_toDB(graph):
    """
    This function receives as a parameter a previously generated graph and
    saves its nodes into a sqllite database created in memory (for performance) using
    SQLAlchemy ORM toolkit imported above.


    """
    engine = create_engine('sqlite:///:memory:', echo=False)
    Session = sessionmaker(bind=engine)
    meta = MetaData()
    n = Table('node', meta, Column('node_id', Integer, primary_key=True))
    e = Table('edge', meta,
            Column('node1', Integer, unique=True),
            Column('node2', Integer, unique=True),
            UniqueConstraint('node1','node2'))

    meta.create_all(engine)

    session = Session()
    for vert in graph:
        node = Node(vert.getKey())
        session.add(node)
        for ed in vert.getConnections():
            edge = node.add_neighbors(node)
    session.commit()

if __name__ == '__main__':
    graph = generate_graph()
    save_toDB(graph)
