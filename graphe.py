#!/usr/bin/python3
# coding: utf-8
import copy
class Graph() :
    def __init__(self) :
        self.list_vertex=[]
        self.number_egde=0
        self.graph={}

        ##dico de liste ex : {0 : [[1,2,3],[2,4,5]]}
    def add_edge(self,vertex1,vertex2) : 
        if vertex1 in self.graph :
            if vertex2 not in self.graph[vertex1][1]  :
                ##arc sortant pour vertex1
                self.graph[vertex1][1].append(vertex2)  
        else :
            self.graph[vertex1]=[[],[vertex2]]

        if vertex2 in self.graph :
            if vertex1 not in self.graph[vertex2][0]  :
                ##arc entrant pour vertex2
                self.graph[vertex2][0].append(vertex1)  
        else :
            self.graph[vertex2]=[[vertex1],[]]

        self.number_egde=self.number_egde+1

        
    def is_connected(self) :
        #utilisation algo BFS ici
        #vérification si le graphe est connexe (d'un sommet on peut aller à tous les autres)
        vertex_visited=[list(self.graph.keys())[0]] 
         ##je prends un sommet au pif (je prend la 1ere clé de la liste des clés)
        vertex_processing= copy.copy(self.graph[vertex_visited[0]][1])
        while vertex_processing :
            v=vertex_processing[0]
            if v not in vertex_visited :
                vertex_visited.append(v)
                if v not in self.graph :
                    return False
                for elem in self.graph[v][1] :
                    vertex_processing.append(elem)
            del vertex_processing[0]
        print(vertex_visited)    
        return(len(vertex_visited)==len(self.graph))
    
    def eulerian_cycle(self) : 
        #veref nb entrant=nbsortant
        for elem in self.graph:
            edge_in=self.graph[elem][0]
            edge_out=self.graph[elem][1]
            print("in :", edge_in)
            print("out :",edge_out)

            if len(edge_in)!=len(edge_out):
                return False
        return True  
        

#g1 = Graph()
#g1.add_edge('0', '1')
#g1.add_edge('0', '2')
#g1.add_edge('1', '2')
#g1.add_edge('2', '3')
#print(g1.graph)
#print(g1.is_connected())
#print(len(g1.graph))