#!/usr/bin/python3
# coding: utf-8

class Graph() :
    def __init__(self) :
        self.list_vertex=[]
        self.number_egde=0
        self.graph={}

        ##dico de liste ex : {0 : [1,2,3]}
    def add_edge(self,vertex1,vertex2) : 
        if vertex1 in self.graph :
            if vertex2 not in self.graph[vertex1]  :
                self.graph[vertex1].append(vertex2)  
        else :
            self.graph[vertex1]=[vertex2]
        self.number_egde=self.number_egde+1
        
    def is_connected(self) :
        #utilisation algo BFS ici
        #vérification si le graphe est connexe (d'un sommet on peut aller à tous les autres)
        vertex_visited=[list(self.graph.keys())[0]] 
         ##je prends un sommet au pif (je prend la 1ere clé de la liste des clés)
        vertex_processing= self.graph[vertex_visited[0]]
        while vertex_processing :
            v=vertex_processing[0]
            if v not in vertex_visited :
                vertex_visited.append(v)
                if v not in self.graph :
                    return False
                for elem in self.graph[v] :
                    vertex_processing.append(elem)
            del vertex_processing[0]
        print(vertex_visited)    
        return(len(vertex_visited)==len(self.graph))
    def eulerian_cycle(self) :   
        print("a faire")

#g1 = Graph()
#g1.add_edge('0', '1')
#g1.add_edge('0', '2')
#g1.add_edge('1', '2')
#g1.add_edge('2', '3')
#print(g1.graph)
#print(g1.is_connected())
#print(len(g1.graph))