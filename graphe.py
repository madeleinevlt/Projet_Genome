#!/usr/bin/python3
# coding: utf-8
import copy
import random 
class Graph() :
    def __init__(self) :
        self.graph={}
        self.number_edge=0

        ##dico de liste ex : {0 : [[1,2,3],[2,4,5]]}
    def add_edge(self,vertex1,vertex2) : 
        if vertex1 in self.graph :
            if vertex2 not in self.graph[vertex1][1]  :
                ##arc sortant pour vertex1
                self.graph[vertex1][1].append(vertex2)
                self.number_edge=self.number_edge+1  
        else :
            self.graph[vertex1]=[[],[vertex2]]
            self.number_edge=self.number_edge+1

        if vertex2 in self.graph :
            if vertex1 not in self.graph[vertex2][0]  :
                ##arc entrant pour vertex2
                self.graph[vertex2][0].append(vertex1)  
        else :
            self.graph[vertex2]=[[vertex1],[]]




    def build_genome(self,edge_path) :
        first=edge_path[0][0]
        genome=first
        for all_tuples in edge_path :
            genome=genome+all_tuples[1][-1:]

        #print("GENOME a la fin :", genome[:-len(first)])
        print("TAILLE genome fin :",len(genome[:-len(first)]))
        return genome[:-len(first)]
        
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
        return(len(vertex_visited)==len(self.graph))
    
    def making_cycle(self,start,end,edge_visited) :
        keep_going=True
        while end!=start and keep_going==True :
            random_path=random.randint(0,len(self.graph[end][1])-1)
            new_end=self.graph[end][1][random_path]

            while ((end,new_end)) in edge_visited :
                random_path=random.randint(0,len(self.graph[end][1])-1)
                new_end=self.graph[end][1][random_path]
            edge_visited.append((end,new_end))
            end=new_end
            if start==end :
                keep_going=False
                for possible_next_step in self.graph[start][1] :
                    if ((start,possible_next_step) not in edge_visited) :
                        end=possible_next_step
                        edge_visited.append((start,end))
                        keep_going=True
        return edge_visited                
            
    def eulerian_cycle(self) : 
        #veref nb entrant=nbsortant
        for elem in self.graph:
            edge_in=self.graph[elem][0]
            edge_out=self.graph[elem][1]
            if len(edge_in)!=len(edge_out):
                print("ERREUR")
                exit()

        ##recherche du cycle eulerian
        start=list(self.graph.keys())[0]
        random_path=random.randint(0,len(self.graph[start][1])-1 )
        end=self.graph[start][1][random_path]
        edge_visited=[(start,end)]
        edge_visited=self.making_cycle(start,end,edge_visited)

        #si notre cycle n'est pas eulérien
        ##notre : peut etre garder en mémoire que le nb d'arcs
        #for k in range(0,10) :
        while len(edge_visited)!=self.number_edge :
            #je regarde mes arcs que j'ai visité
            found=False
            for tuples in edge_visited :
                #je regarde pour chaque sommet que j'ai traverse avec mes arcs s'ils ont un autre chemin
                for vertex in self.graph[tuples[0]][1] :
                    if ((tuples[0],vertex)) not in edge_visited :
                        new_start = tuples[0]
                        found=True
                        break
                if found==True :
                    break
            start=new_start 
            edge_visited_tmp=[]
            i=0
            edge_found=False
            for edge in edge_visited :
                ##si on a trouvé l'arc de départ
                if edge[0]==start :
                    edge_found=True
                
                if edge_found==True :
                    edge_visited_tmp.append(edge)
                else :
                    i=i+1
            for j in range(0,i) :
                edge_visited_tmp.append(edge_visited[j])

            ##nouvelle liste d'arc toute belle toute propre
            edge_visited=edge_visited_tmp
            start=edge_visited[len(edge_visited)-1][1]

            for potential_end in self.graph[start][1] :
                if ((start,potential_end)) not in edge_visited :
                    end = potential_end
                    break
            edge_visited.append((start,end))
            edge_visited=self.making_cycle(start,end,edge_visited)                 
                            
        print(self.build_genome(edge_visited))

        return self.build_genome(edge_visited)
        

# g1 = Graph()
# g1.add_edge('0', '1')
# g1.add_edge('1', '3')
# g1.add_edge('3', '4')
# g1.add_edge('4', '0')
# g1.add_edge('1', '2')
# g1.add_edge('2', '1')
# g1.add_edge('4', '5')
# g1.add_edge('5', '6')
# g1.add_edge('6', '4')


# print(g1.graph)
# print(g1.number_edge)
# print(g1.is_connected())
# print(g1.eulerian_cycle())