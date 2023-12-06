from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import MainNode_data as MainNode


class MainGraph:

    def __init__(self, graph: Graph):
        # Umwandeln in ein Attribut sie steht nun der gesamten Klasse zur Verfügung
        self.main_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        # Anlegen der Knoten
        self.main_node = Node(MainNode.CONTENT, MainNode.TITEL)

        # Hinzufügen des Knoten zum Graphen
        graph.add_new_node_to_graph(self.main_node)

    def get_main_node(self):
        return self.main_node
