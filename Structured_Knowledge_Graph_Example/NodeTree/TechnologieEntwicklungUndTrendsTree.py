from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (
    TechnologieEntwicklungUndTrends_data as TechnologieEntwicklungUndTrends,
    AktuelleEntwicklungenInDerInformatik_data as AktuelleEntwicklungenInDerInformatik,
    AnpassungAnNeueTechnologie_data as AnpassungAnNeueTechnologie,
    AuswirkungAufDenLehrplan_data as AuswirkungAufDenLehrplan,
    Innovationsmanagement_data as Innovationsmanagement,
    KIInformatikStudium_data as KIInformatikStudium, )


class TechnologieEntwicklungUndTrendsTree:
    def __init__(self, graph: Graph):
        self.k_i_informatik_studium = None
        self.innovationsmanagement_node = None
        self.technologie_entwicklungen_und_trends_node = None
        self.aktuelle_entwicklungen_in_der_informatik_node = None
        self.anpassung_an_neue_technologie_node = None
        self.auswirkung_auf_den_lehrplan_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.technologie_entwicklungen_und_trends_node = Node(TechnologieEntwicklungUndTrends.CONTENT,
                                                              TechnologieEntwicklungUndTrends.TITEL)
        self.aktuelle_entwicklungen_in_der_informatik_node = Node(AktuelleEntwicklungenInDerInformatik.CONTENT,
                                                                  AktuelleEntwicklungenInDerInformatik.TITEL)
        self.anpassung_an_neue_technologie_node = Node(AnpassungAnNeueTechnologie.CONTENT,
                                                       AnpassungAnNeueTechnologie.TITEL)
        self.auswirkung_auf_den_lehrplan_node = Node(AuswirkungAufDenLehrplan.CONTENT,
                                                     AuswirkungAufDenLehrplan.TITEL)
        self.innovationsmanagement_node = Node(Innovationsmanagement.CONTENT,
                                               Innovationsmanagement.TITEL)
        self.k_i_informatik_studium = Node(KIInformatikStudium.CONTENT,
                                           KIInformatikStudium.TITEL)

        self.technologie_entwicklungen_und_trends_node.connect(self.aktuelle_entwicklungen_in_der_informatik_node)
        self.technologie_entwicklungen_und_trends_node.connect(self.anpassung_an_neue_technologie_node)
        self.technologie_entwicklungen_und_trends_node.connect(self.auswirkung_auf_den_lehrplan_node)
        self.technologie_entwicklungen_und_trends_node.connect(self.innovationsmanagement_node)
        self.technologie_entwicklungen_und_trends_node.connect(self.k_i_informatik_studium)

        graph.add_new_node_to_graph(self.technologie_entwicklungen_und_trends_node)
        graph.add_new_node_to_graph(self.aktuelle_entwicklungen_in_der_informatik_node)
        graph.add_new_node_to_graph(self.anpassung_an_neue_technologie_node)
        graph.add_new_node_to_graph(self.auswirkung_auf_den_lehrplan_node)
        graph.add_new_node_to_graph(self.innovationsmanagement_node)
        graph.add_new_node_to_graph(self.k_i_informatik_studium)

    def get_parent_node(self):
        return self.technologie_entwicklungen_und_trends_node
