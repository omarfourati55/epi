from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (EntscheidungenBeiKurzWahl_data as EntscheidungenBeiKurzWahl,
                                                         WahlModule_data as WahlModule,
                                                         KarriereEntscheidung_data as KarriereEntscheidung,
                                                         PersoenlicheIntressen_data as PersoenlicheInteressen)


class EntscheidungenBeiKurzWahlTree:
    def __init__(self, graph: Graph):
        self.entscheidungen_bei_kurz_wahl_node = None
        self.wahl_module_node = None
        self.karriere_entscheidung_node = None
        self.persoenliche_interessen_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.entscheidungen_bei_kurz_wahl_node = Node(EntscheidungenBeiKurzWahl.CONTENT,
                                                      EntscheidungenBeiKurzWahl.TITEL)
        self.wahl_module_node = Node(WahlModule.CONTENT,
                                     WahlModule.TITEL)
        self.karriere_entscheidung_node = Node(KarriereEntscheidung.CONTENT,
                                               KarriereEntscheidung.TITEL)
        self.persoenliche_interessen_node = Node(PersoenlicheInteressen.CONTENT,
                                                 PersoenlicheInteressen.TITEL)

        self.entscheidungen_bei_kurz_wahl_node.connect(self.wahl_module_node)
        self.entscheidungen_bei_kurz_wahl_node.connect(self.karriere_entscheidung_node)
        self.entscheidungen_bei_kurz_wahl_node.connect(self.persoenliche_interessen_node)

        graph.add_new_node_to_graph(self.entscheidungen_bei_kurz_wahl_node)
        graph.add_new_node_to_graph(self.wahl_module_node)
        graph.add_new_node_to_graph(self.karriere_entscheidung_node)
        graph.add_new_node_to_graph(self.persoenliche_interessen_node)

    def get_parent_node(self):
        return self.entscheidungen_bei_kurz_wahl_node
