from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (
    ZusaetzlicheHerausforderungenFuerStudierende_data as ZusaetzlicheHerausforderungenFuerStudierende,
    VereinbarkeitVomStudium_data as VereinbarkeitVomStudium,
    SozialeUndEmotionaleHerausforderungen_data as SozialeUndEmotionaleHerausforderungen,
    NetzwerkbildungKarriereplanung_data as NetzwerkbildungKarriereplanung,
    TeamarbeitSoftwareentwicklung_data as TeamarbeitSoftwareentwicklung,
    VeraenderungInProgrammiersprachenFramework_data as VeraenderungInProgrammiersprachenFramework,
    WorkLifeBalance_data as WorkLifeBalance, )


class ZusaetlicheHerausforderungenFuerStudierendeTree:
    def __init__(self, graph: Graph):
        self.work_life_balance_node = None
        self.veraenderung_in_programmiersprachen_framework_node = None
        self.teamarbeit_softwareentwicklung_node = None
        self.netzwerkbildung_karriereplanung_node = None
        self.zusaetzliche_herausforderungen_fuer_studierende_node = None
        self.vereinbarkeit_vom_studium_node = None
        self.soziale_und_emotionale_herausforderungen_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.zusaetzliche_herausforderungen_fuer_studierende_node = Node(
            ZusaetzlicheHerausforderungenFuerStudierende.CONTENT,
            ZusaetzlicheHerausforderungenFuerStudierende.TITEL)

        self.vereinbarkeit_vom_studium_node = Node(VereinbarkeitVomStudium.CONTENT,
                                                   VereinbarkeitVomStudium.TITEL)

        self.soziale_und_emotionale_herausforderungen_node = Node(SozialeUndEmotionaleHerausforderungen.CONTENT,
                                                                  SozialeUndEmotionaleHerausforderungen.TITEL)

        self.netzwerkbildung_karriereplanung_node = Node(NetzwerkbildungKarriereplanung.CONTENT,
                                                         NetzwerkbildungKarriereplanung.TITEL)
        self.teamarbeit_softwareentwicklung_node = Node(TeamarbeitSoftwareentwicklung.CONTENT,
                                                        TeamarbeitSoftwareentwicklung.TITEL)
        self.veraenderung_in_programmiersprachen_framework_node = Node(
            VeraenderungInProgrammiersprachenFramework.CONTENT,
            VeraenderungInProgrammiersprachenFramework.TITEL)
        self.work_life_balance_node = Node(WorkLifeBalance.CONTENT,
                                           WorkLifeBalance.TITEL)

        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(self.vereinbarkeit_vom_studium_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(
            self.soziale_und_emotionale_herausforderungen_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(self.netzwerkbildung_karriereplanung_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(self.teamarbeit_softwareentwicklung_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(
            self.veraenderung_in_programmiersprachen_framework_node)
        self.zusaetzliche_herausforderungen_fuer_studierende_node.connect(self.work_life_balance_node)

        graph.add_new_node_to_graph(self.vereinbarkeit_vom_studium_node)
        graph.add_new_node_to_graph(self.soziale_und_emotionale_herausforderungen_node)
        graph.add_new_node_to_graph(self.zusaetzliche_herausforderungen_fuer_studierende_node)
        graph.add_new_node_to_graph(self.netzwerkbildung_karriereplanung_node)
        graph.add_new_node_to_graph(self.teamarbeit_softwareentwicklung_node)
        graph.add_new_node_to_graph(self.veraenderung_in_programmiersprachen_framework_node)
        graph.add_new_node_to_graph(self.work_life_balance_node)

    def get_parent_node(self):
        return self.zusaetzliche_herausforderungen_fuer_studierende_node
