from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (
    PraktikaUndBerufsErfahrung_data as PraktikaUndBerufsErfahrung,
    EntscheidungBeimPraktikumsPlatz_data as EntscheidungBeimPraktikumsPlatz,
    BedeutungVomPraktika_data as BedeutungVomPraktika,
    AuswirkungAufDenBeruflichenWerdegang_data as AuswirkungAufDenBeruflichenWerdegang)


class PraktikaUndBerufsErfahrungTree:
    def __init__(self, graph: Graph):
        self.praktika_und_berufs_erfahrung_node = None
        self.entscheidung_beim_praktikums_platz_node = None
        self.bedeutung_vom_praktika_node = None
        self.auswirkung_auf_den_beruflichen_werdegang_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.praktika_und_berufs_erfahrung_node = Node(PraktikaUndBerufsErfahrung.CONTENT,
                                                       PraktikaUndBerufsErfahrung.TITEL)
        self.entscheidung_beim_praktikums_platz_node = Node(EntscheidungBeimPraktikumsPlatz.CONTENT,
                                                            EntscheidungBeimPraktikumsPlatz.TITEL)
        self.bedeutung_vom_praktika_node = Node(BedeutungVomPraktika.CONTENT,
                                                BedeutungVomPraktika.TITEL)
        self.auswirkung_auf_den_beruflichen_werdegang_node = Node(AuswirkungAufDenBeruflichenWerdegang.CONTENT,
                                                                  AuswirkungAufDenBeruflichenWerdegang.TITEL)

        self.praktika_und_berufs_erfahrung_node.connect(self.entscheidung_beim_praktikums_platz_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.bedeutung_vom_praktika_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.auswirkung_auf_den_beruflichen_werdegang_node)

        graph.add_new_node_to_graph(self.praktika_und_berufs_erfahrung_node)
        graph.add_new_node_to_graph(self.entscheidung_beim_praktikums_platz_node)
        graph.add_new_node_to_graph(self.bedeutung_vom_praktika_node)
        graph.add_new_node_to_graph(self.auswirkung_auf_den_beruflichen_werdegang_node)

    def get_parent_node(self):
        return self.praktika_und_berufs_erfahrung_node
