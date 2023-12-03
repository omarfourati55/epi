from GraphModel.Graph import Graph
from GraphModel.Node import Node
from Structured_Knowledge_Graph_Example.NodeData import (StudienRichtungenInDerInformatik_data as St,
                                                         BachelorUndMasterStudienGaenge_data as Bm,
                                                         SchwerPunkteUndSpezialisierung_data as Sp)


class StudienRichtungTree:
    def __init__(self, graph: Graph):
        self.schwer_punkte_node = None
        self.bachelor_und_master_studien_gaenge_node = None
        self.studien_richtung_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.studien_richtung_node = Node(St.CONTENT, St.TITEL)
        self.bachelor_und_master_studien_gaenge_node = Node(Bm.CONTENT, Bm.TITEL)
        self.schwer_punkte_node = Node(Sp.CONTENT, Sp.TITEL)

        self.studien_richtung_node.connect(self.bachelor_und_master_studien_gaenge_node)
        self.studien_richtung_node.connect(self.schwer_punkte_node)

        graph.add_new_node_to_graph(self.studien_richtung_node)
        graph.add_new_node_to_graph(self.bachelor_und_master_studien_gaenge_node)
        graph.add_new_node_to_graph(self.schwer_punkte_node)

    def get_parent_node(self):
        return self.studien_richtung_node
