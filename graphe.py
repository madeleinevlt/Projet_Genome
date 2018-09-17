#!/usr/bin/python3
# coding: utf-8
import copy
import random 
class Graph() :
    """
    L'initialisation et les méthodes qui s'appliquent sur un graphe sont regroupés ici. 
    Le graphe est sous forme d'un dictionnaire avec comme clé un sommet et comme définitions 2 listes qui contiennent les arcs entrants et sortants (le nom des sommets).
    """
    def __init__(self) :
        """
        Initialisation de la classe
        """
        self.graph={}
        self.number_edge=0

    def add_edge(self,vertex1,vertex2) : 
        """
        Cette méthode permet d'ajouter un sommet dans un graphe
        """
        if vertex1 in self.graph :
            if vertex2 not in self.graph[vertex1][1]  :
                # arc sortant pour vertex1
                self.graph[vertex1][1].append(vertex2)
                self.number_edge=self.number_edge+1  
        else :
            self.graph[vertex1]=[[],[vertex2]]
            self.number_edge=self.number_edge+1

        if vertex2 in self.graph :
            if vertex1 not in self.graph[vertex2][0]  :
                # arc entrant pour vertex2
                self.graph[vertex2][0].append(vertex1)  
        else :
            self.graph[vertex2]=[[vertex1],[]]


    def build_genome(self,edge_path) :
        """
        Cette méthode permet à partir d'une liste de sommet de reconstituer le génome
        """
        first=edge_path[0][0]
        genome=first
        for all_tuples in edge_path :
            genome=genome+all_tuples[1][-1:]
        print("TAILLE genome fin :",len(genome[:-len(first)]))
        return genome[:-len(first)]
        
    def is_connected(self) :
        """
        Cette méthode permet de vérifier que le graphe est connexe. L'algorithme utilisé ici est un algorithme BFS (recherche en largeur)
        """
        vertex_visited=[list(self.graph.keys())[0]] 
        # je prends un sommet au hasard (je prend la 1ere clé de la liste des clés)
        vertex_processing= copy.copy(self.graph[vertex_visited[0]][1])
        while vertex_processing :
            v=vertex_processing.pop()
            if v not in vertex_visited :
                vertex_visited.append(v)
                if v not in self.graph :
                    return False
                for elem in self.graph[v][1] :
                    vertex_processing.append(elem)
        return(len(vertex_visited)==len(self.graph))
    
    def making_cycle(self,start,end,edge_visited) :
        """
        Cette méthode permet de recherche un cycle à partir d'un sommet de départ et un sommet adjacent au sommet de départ (end).
        """
        keep_going=True
        while end!=start and keep_going==True :
            random_path=random.randint(0,len(self.graph[end][1])-1)
            # recherche d'un potentiel arc qui n'est pas connu
            new_end=self.graph[end][1][random_path]
            while ((end,new_end)) in edge_visited :
                random_path=random.randint(0,len(self.graph[end][1])-1)
                new_end=self.graph[end][1][random_path]
            edge_visited.append((end,new_end))
            end=new_end
            # si on est revenu à notre sommet de départ (donc nous avons fait un cycle)
            if start==end :
                keep_going=False
                for possible_next_step in self.graph[start][1] :
                    # s'il existe un autre arc adjacent au sommet de départ que l'on a pas visité
                    if ((start,possible_next_step) not in edge_visited) :
                        end=possible_next_step
                        edge_visited.append((start,end))
                        keep_going=True
        return edge_visited                
            
    def eulerian_cycle(self) : 
        """
        Cette méthode permet de voir s'il existe un cycle eulérian ou non, et s'il existe, renvoit le cycle d'arc correspondant au cycle eulérian.
        """
        # vérification que le nombre d'arc entrant = nombre d'arc sortant pour chaque sommet
        for elem in self.graph:
            edge_in=self.graph[elem][0]
            edge_out=self.graph[elem][1]
            if len(edge_in)!=len(edge_out):
                print("ERREUR : CE GRAPHE NE CONTIENT PAS DE CYCLE EULERIAN")
                exit()

        # recherche du cycle eulerian
        start=list(self.graph.keys())[0]
        random_path=random.randint(0,len(self.graph[start][1])-1 )
        end=self.graph[start][1][random_path]
        edge_visited=[(start,end)]
        edge_visited=self.making_cycle(start,end,edge_visited)

        # si notre cycle que l'on a trouvé n'est pas le cycle eulérien
        while len(edge_visited)!=self.number_edge :
            # je regarde mes arcs que j'ai visité
            found=False
            for tuples in edge_visited :
                # je regarde pour chaque sommet que j'ai traverse avec mes arcs s'ils ont un autre chemin
                for vertex in self.graph[tuples[0]][1] :
                    if ((tuples[0],vertex)) not in edge_visited :
                        # si oui : il devient mon nouveau sommet de départ
                        new_start = tuples[0]
                        found=True
                        break
                if found==True :
                    break
            start=new_start 
            edge_visited_tmp=[]
            i=0
            edge_found=False
            # pour reformer un cycle avec comme sommet de départ notre nouveau sommet, nous devons rechercher l'arc correspondant à notre nouveau sommet
            for edge in edge_visited :
                if edge[0]==start :
                    edge_found=True
                
                if edge_found==True :
                    edge_visited_tmp.append(edge)
                else :
                    i=i+1
            for j in range(0,i) :
                edge_visited_tmp.append(edge_visited[j])

            # nouvelle liste d'arc avec comme 1er arc notre nouveau sommet de départ
            edge_visited=edge_visited_tmp
            start=edge_visited[len(edge_visited)-1][1]

            # recherche d'un sommet adjacent qui n'est pas déjà visité (donc un nouveau chemin d'arc que nous pouvons explorer)
            for potential_end in self.graph[start][1] :
                if ((start,potential_end)) not in edge_visited :
                    end = potential_end
                    break
            edge_visited.append((start,end))
            edge_visited=self.making_cycle(start,end,edge_visited)                 
                            
        return self.build_genome(edge_visited)
        
