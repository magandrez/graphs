from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Node(Base):
    __tablename__ = 'node'

    node_id = Column(Integer, primary_key=True)

    def __init__(self, id):
        self.node_id = id

    def add_neighbors(self, *nodes):
        for node in nodes:
            Edge(self, node)
        return self

    def higher_neighbors(self):
        return [x.higher_node for x in self.lower_edges]

    def lower_neighbors(self):
        return [x.lower_node for x in self.higher_edges]


class Edge(Base):
    __tablename__ = 'edge'

    lower_id = Column(Integer,
                        ForeignKey('node.node_id'),
                        primary_key=True)

    higher_id = Column(Integer,
                        ForeignKey('node.node_id'),
                        primary_key=True)

    lower_node = relationship(Node,
                                primaryjoin=lower_id==Node.node_id,
                                backref='lower_edges')
    higher_node = relationship(Node,
                                primaryjoin=higher_id==Node.node_id,
                                backref='higher_edges')

    def __init__(self, n1, n2):
        if n1.node_id < n2.node_id:
            self.lower_node = n1
            self.higher_node = n2
        else:
            self.lower_node = n2
            self.higher_node = n1
