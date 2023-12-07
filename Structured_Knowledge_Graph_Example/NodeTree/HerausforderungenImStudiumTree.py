from GraphModel.Graph import Graph
from GraphModel.Node import Node

from Structured_Knowledge_Graph_Example.NodeData import (HerausforderungenImStudium_data as HerausforderungenImStudium,
                                                         ZeitManagementBelastung_data as ZeitManagementBelastung,
                                                         SchwierigkeitGradBestimmterKurse_data as SchwierigkeitGradBestimmterKurse,
                                                         PraktischeProjekte_data as PraktischeProjekte,
                                                         AkademischeStressDruck_data as AkademischeStressDruck,
                                                         IntegrationPraxiserfahrung_data as IntegrationPraxiserfahrung,
                                                         KarriereplanungBerufseinstieg_data as KarriereplanungBerufseinstieg,
                                                         KomplexenDatenstrukturenAlgorithmen_data as KomplexenDatenstrukturenAlgorithmen,
                                                         ManagementITProjekt_data as ManagementITProjekt,
                                                         MCIBenutzererfahrung_data as MCIBenutzererfahrung,
                                                         TheoriePraxisKluft_data as TheoriePraxisKluft,
                                                         UXInformatik_data as UXInformatik, )


class HerausforderungenImStudiumTree:
    def __init__(self, graph: Graph):
        self.m_c_i_benutzererfahrung_node = None
        self.komplexen_datenstrukturen_algorithmen_node = None
        self.theorie_praxis_kluft_node = None
        self.u_x_informatik_node = None
        self.management_i_t_projekt_node = None
        self.karriereplanung_berufseinstieg_node = None
        self.integration_praxiserfahrung_node = None
        self.akademische_stress_druck_node = None
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
        self.akademische_stress_druck_node = Node(AkademischeStressDruck.CONTENT,
                                                  AkademischeStressDruck.TITEL)
        self.integration_praxiserfahrung_node = Node(IntegrationPraxiserfahrung.CONTENT,
                                                     IntegrationPraxiserfahrung.TITEL)
        self.karriereplanung_berufseinstieg_node = Node(KarriereplanungBerufseinstieg.CONTENT,
                                                        KarriereplanungBerufseinstieg.TITEL)
        self.komplexen_datenstrukturen_algorithmen_node = Node(KomplexenDatenstrukturenAlgorithmen.CONTENT,
                                                               KomplexenDatenstrukturenAlgorithmen.TITEL)
        self.management_i_t_projekt_node = Node(ManagementITProjekt.CONTENT,
                                                ManagementITProjekt.TITEL)
        self.m_c_i_benutzererfahrung_node = Node(MCIBenutzererfahrung.CONTENT,
                                                MCIBenutzererfahrung.TITEL)
        self.theorie_praxis_kluft_node = Node(TheoriePraxisKluft.CONTENT,
                                                 TheoriePraxisKluft.TITEL)
        self.u_x_informatik_node = Node(UXInformatik.CONTENT,
                                              UXInformatik.TITEL)

        self.herausforderungen_im_studium_node.connect(self.zeit_management_belastung_node)
        self.herausforderungen_im_studium_node.connect(self.schwierigkeit_grad_bestimmter_kurse_node)
        self.herausforderungen_im_studium_node.connect(self.praktische_projekte_node)
        self.herausforderungen_im_studium_node.connect(self.akademische_stress_druck_node)
        self.herausforderungen_im_studium_node.connect(self.integration_praxiserfahrung_node)
        self.herausforderungen_im_studium_node.connect(self.karriereplanung_berufseinstieg_node)
        self.herausforderungen_im_studium_node.connect(self.komplexen_datenstrukturen_algorithmen_node)
        self.herausforderungen_im_studium_node.connect(self.management_i_t_projekt_node)
        self.herausforderungen_im_studium_node.connect(self.m_c_i_benutzererfahrung_node)
        self.herausforderungen_im_studium_node.connect(self.theorie_praxis_kluft_node)
        self.herausforderungen_im_studium_node.connect(self.u_x_informatik_node)

        graph.add_new_node_to_graph(self.zeit_management_belastung_node)
        graph.add_new_node_to_graph(self.schwierigkeit_grad_bestimmter_kurse_node)
        graph.add_new_node_to_graph(self.praktische_projekte_node)
        graph.add_new_node_to_graph(self.akademische_stress_druck_node)
        graph.add_new_node_to_graph(self.herausforderungen_im_studium_node)
        graph.add_new_node_to_graph(self.integration_praxiserfahrung_node)
        graph.add_new_node_to_graph(self.karriereplanung_berufseinstieg_node)
        graph.add_new_node_to_graph(self.komplexen_datenstrukturen_algorithmen_node)
        graph.add_new_node_to_graph(self.management_i_t_projekt_node)
        graph.add_new_node_to_graph(self.m_c_i_benutzererfahrung_node)
        graph.add_new_node_to_graph(self.theorie_praxis_kluft_node)
        graph.add_new_node_to_graph(self.u_x_informatik_node)

    def get_parent_node(self):
        return self.herausforderungen_im_studium_node
