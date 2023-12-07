from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (
    PraktikaUndBerufsErfahrung_data as PraktikaUndBerufsErfahrung,
    EntscheidungBeimPraktikumsPlatz_data as EntscheidungBeimPraktikumsPlatz,
    BedeutungVomPraktika_data as BedeutungVomPraktika,
    AuswirkungAufDenBeruflichenWerdegang_data as AuswirkungAufDenBeruflichenWerdegang,
    AuswahlProjektenPraktika_data as AuswahlProjektenPraktika,
    DigitaleArbeitswelt_data as DigitaleArbeitswelt,
    RemoteArbeit_data as RemoteArbeit,
    Weiterbildung_data as Weiterbildung,)


class PraktikaUndBerufsErfahrungTree:
    def __init__(self, graph: Graph):
        self.weiterbildung_node = None
        self.remote_arbeit_node = None
        self.digitale_arbeitswelt_node = None
        self.auswahl_projekten_praktika_node = None
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
        self.auswahl_projekten_praktika_node = Node(AuswahlProjektenPraktika.CONTENT,
                                                    AuswahlProjektenPraktika.TITEL)
        self.digitale_arbeitswelt_node = Node(DigitaleArbeitswelt.CONTENT,
                                              DigitaleArbeitswelt.TITEL)
        self.remote_arbeit_node = Node(RemoteArbeit.CONTENT,
                                       RemoteArbeit.TITEL)
        self.weiterbildung_node = Node(Weiterbildung.CONTENT,
                                       Weiterbildung.TITEL)

        self.praktika_und_berufs_erfahrung_node.connect(self.entscheidung_beim_praktikums_platz_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.bedeutung_vom_praktika_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.auswirkung_auf_den_beruflichen_werdegang_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.auswahl_projekten_praktika_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.digitale_arbeitswelt_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.remote_arbeit_node)
        self.praktika_und_berufs_erfahrung_node.connect(self.weiterbildung_node)

        graph.add_new_node_to_graph(self.praktika_und_berufs_erfahrung_node)
        graph.add_new_node_to_graph(self.entscheidung_beim_praktikums_platz_node)
        graph.add_new_node_to_graph(self.bedeutung_vom_praktika_node)
        graph.add_new_node_to_graph(self.auswirkung_auf_den_beruflichen_werdegang_node)
        graph.add_new_node_to_graph(self.auswahl_projekten_praktika_node)
        graph.add_new_node_to_graph(self.digitale_arbeitswelt_node)
        graph.add_new_node_to_graph(self.remote_arbeit_node)
        graph.add_new_node_to_graph(self.weiterbildung_node)

    def get_parent_node(self):
        return self.praktika_und_berufs_erfahrung_node
