from model import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy import *
from graphs import *
from strong_components import *
import random


@profile
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
    print("=== Pseudo-random graph generator ===")
    print("Enter the number of nodes in the graph: ")
    nodes = int(input())
    keys = [int(i) for i in range(0, nodes)]
    for i in range(nodes):
        g.addNode(keys[i])

    print("Enter the number of edges in the graph: ")
    edges = int(input())
    for i in range(edges):
        #using random.randrange()
        #number of nodes as top number of edges to be generated
        node1 = random.randrange(len(keys))
        node2 = random.randrange(len(keys))
        g.addEdge(node1, node2)
    print("Below, the list of all generated nodes (a,b):")
    for vert in g.getEdges():
        #print the node ID
        print(vert.getKey())
        for e in vert.getConnections():
            #print the edge
            print("( %s , %s )" % (vert.getKey(), e.getKey()))

    return g

@profile
def save_toDB(graph):
    """
    This function receives as a parameter a previously generated graph and
    saves its nodes into a sqllite database created in memory (for performance) using
    SQLAlchemy ORM toolkit imported above.
    """
    print("=== Saving generated graph to DB (SQLite) ===")
    #defining engine and debug mode
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for vert in graph.getEdges():
        node = Node(vert.getKey())
        session.add(node)
        #node.add_neighbors(vert)
        #TO-DO
        #Find a way to retrieve and create edges in the database

    session.commit()

@profile
def strong_calculation(vertices,edges):
    """
    This is a caller to strongly_connected_components_iterative implemented in
    strong_components module.

    Original code was found here: http://code.activestate.com/recipes/578507-strongly-connected-components-of-a-directed-graph/
    based on Tarjan's algorithm: http://www.wikiwand.com/en/Tarjan%27s_strongly_connected_components_algorithm

    Used a function in main to be able to profile using line_profiler package
    with decorator @profile in main.py
    """
    print("=== Calculating strongly connected components")
    print(list(strongly_connected_components_iterative(vertices, edges)))

if __name__ == '__main__':
    graph = generate_graph()
    #TO-DO
    #Fix db commit (no edges are commited to DB)
    save_toDB(graph)
    #TO-DO
    #Fix algorithm. At the moment returns all nodes
    #as strongly connected components
    strong_calculation(graph.getNodes(), graph)
