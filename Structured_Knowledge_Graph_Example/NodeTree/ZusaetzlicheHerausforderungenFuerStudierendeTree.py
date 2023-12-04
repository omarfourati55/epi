from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (
    ZusaetzlicheHerausforderungenFuerStudierende_data as ZusaetzlicheHerausforderungenFuerStudierende,
    VereinbarkeitVomStudium_data as VereinbarkeitVomStudium,
    SozialeUndEmotionaleHerausforderungen_data as SozialeUndEmotionaleHerausforderungen,
    FinanzielleAspekte_data as FinanzielleAspekte)


class ZusaetlicheHerausforderungenFuerStudierendeTree:
    def __init__(self, graph: Graph):
        self.zusaetzliche_herausforderungen_fuer_studierende_node = None
        self.vereinbarkeit_vom_studium_node = None
        self.soziale_und_emotionale_herausforderungen_node = None
        self.finanzielle_aspekte_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.zusaetzliche_herausforderungen_fuer_studierende_node = Node(
            ZusaetzlicheHerausforderungenFuerStudierende.CONTENT,
            ZusaetzlicheHerausforderungenFuerStudierende.TITEL)

        self.vereinbarkeit_vom_studium_node = Node(VereinbarkeitVomStudium.CONTENT,
                                                   VereinbarkeitVomStudium.TITEL)

        self.soziale_und_emotionale_herausforderungen_node = Node(SozialeUndEmotionaleHerausforderungen.CONTENT,
                                                                  SozialeUndEmotionaleHerausforderungen.TITEL)

        self.finanzielle_aspekte_node = Node(FinanzielleAspekte.CONTENT,
                                             FinanzielleAspekte.TITEL)

        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(self.vereinbarkeit_vom_studium_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(
            self.soziale_und_emotionale_herausforderungen_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(self.finanzielle_aspekte_node)

        graph.add_new_node_to_graph(self.vereinbarkeit_vom_studium_node)
        graph.add_new_node_to_graph(self.soziale_und_emotionale_herausforderungen_node)
        graph.add_new_node_to_graph(self.finanzielle_aspekte_node)
        graph.add_new_node_to_graph(self.zusaetzliche_herausforderungen_fuer_studierende_node)

    def get_parent_node(self):
        return self.zusaetzliche_herausforderungen_fuer_studierende_node
