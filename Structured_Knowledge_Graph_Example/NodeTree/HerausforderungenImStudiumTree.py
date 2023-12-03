from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (HerausforderungenImStudium_data as HerausforderungenImStudium,
                                                         ZeitManagementBelastung_data as ZeitManagementBelastung,
                                                         SchwierigkeitGradBestimmterKurse_data as SchwierigkeitGradBestimmterKurse,
                                                         PraktischeProjekte_data as PraktischeProjekte, )


class HerausforderungenImStudiumTree:
    def __init__(self, graph: Graph):
        self.herausforderungen_im_studium_node = None
        self.zeit_management_belastung_node = None
        self.schwierigkeit_grad_bestimmter_kurse_node = None
        self.praktische_projekte_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        self.herausforderungen_im_studium_node = Node(HerausforderungenImStudium.CONTENT,
                                                      HerausforderungenImStudium.TITEL)
        self.zeit_management_belastung_node = Node(ZeitManagementBelastung.CONTENT,
                                                   ZeitManagementBelastung.TITEL)
        self.schwierigkeit_grad_bestimmter_kurse_node = Node(SchwierigkeitGradBestimmterKurse.CONTENT,
                                                             SchwierigkeitGradBestimmterKurse.TITEL)
        self.praktische_projekte_node = Node(PraktischeProjekte.CONTENT,
                                             PraktischeProjekte.TITEL)

        self.herausforderungen_im_studium_node.connect(self.zeit_management_belastung_node)
        self.herausforderungen_im_studium_node.connect(self.schwierigkeit_grad_bestimmter_kurse_node)
        self.herausforderungen_im_studium_node.connect(self.praktische_projekte_node)

        graph.add_new_node_to_graph(self.zeit_management_belastung_node)
        graph.add_new_node_to_graph(self.schwierigkeit_grad_bestimmter_kurse_node)
        graph.add_new_node_to_graph(self.praktische_projekte_node)
        graph.add_new_node_to_graph(self.herausforderungen_im_studium_node)

    def get_parent_node(self):
        return self.herausforderungen_im_studium_node
