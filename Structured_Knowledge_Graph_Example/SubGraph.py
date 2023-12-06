from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeTree import (
    HerausforderungenImStudiumTree,
    ZusaetzlicheHerausforderungenFuerStudierendeTree,
    StudienRichtungTree,
    TechnologieEntwicklungUndTrendsTree,
    EntscheidungenBeiKurzWahlTree,
    PraktikaUndBerufsErfahrungTree)


class SubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.parent_node = parent_node
        self.herausforderungen_im_studium_tree = HerausforderungenImStudiumTree.HerausforderungenImStudiumTree(graph)
        self.zusaetzliche_herausforderungen_fuer_studierende_tree = ZusaetzlicheHerausforderungenFuerStudierendeTree.ZusaetlicheHerausforderungenFuerStudierendeTree(graph)
        self.studien_richtung_tree = StudienRichtungTree.StudienRichtungTree(graph)
        self.technologie_entwicklung_und_trends_tree = TechnologieEntwicklungUndTrendsTree.TechnologieEntwicklungUndTrendsTree(graph)
        self.entscheidungen_bei_kurz_wahl_tree = EntscheidungenBeiKurzWahlTree.EntscheidungenBeiKurzWahlTree(graph)
        self.praktika_und_berufs_erfahrung_tree = PraktikaUndBerufsErfahrungTree.PraktikaUndBerufsErfahrungTree(graph)
        self.create_sub_graph(graph)

    def create_sub_graph(self, graph: Graph):
        # Create Nodes
        self.parent_node.connect(self.herausforderungen_im_studium_tree.get_parent_node())
        self.parent_node.connect(self.zusaetzliche_herausforderungen_fuer_studierende_tree.get_parent_node())
        self.parent_node.connect(self.studien_richtung_tree.get_parent_node())
        self.parent_node.connect(self.technologie_entwicklung_und_trends_tree.get_parent_node())
        self.parent_node.connect(self.entscheidungen_bei_kurz_wahl_tree.get_parent_node())
        self.parent_node.connect(self.praktika_und_berufs_erfahrung_tree.get_parent_node())


