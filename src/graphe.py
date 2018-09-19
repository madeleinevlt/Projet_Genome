#!/usr/bin/python3
# coding: utf-8
import copy
import random
class Graph() :
    """
    Initialization of a graph and its methods are regrouped here.
    The graph is in the form of a dictionary with a vertex as the key and as 2 lists that contain the incoming and outgoing arcs (the name of the vertices).
    """
    def __init__(self) :
        """
        Initialization of the class
        """
        self.graph={}
        self.number_edge=0

    def add_edge(self,vertex1,vertex2) :
        """
        This method allows you to add a vertex in a graph
        """
        if vertex1 in self.graph :
            if vertex2 not in self.graph[vertex1][1]  :
                # outgoing arc for vertex1
                self.graph[vertex1][1].append(vertex2)
                self.number_edge=self.number_edge+1
        else :
            self.graph[vertex1]=[[],[vertex2]]
            self.number_edge=self.number_edge+1

        if vertex2 in self.graph :
            if vertex1 not in self.graph[vertex2][0]  :
                # incoming arc for vertex2
                self.graph[vertex2][0].append(vertex1)
        else :
            self.graph[vertex2]=[[vertex1],[]]


    def build_genome(self,edge_path) :
        """
        This method allows from a vertex list to reconstruct the genome
        """
        genome=""
        for all_tuples in edge_path :
            genome=genome+all_tuples[1][:1]
        print("LENGTH OF GENOM BUILT :",len(genome))
        return genome

    def is_connected(self) :
        """
        This method verifies that the graph is connected. The algorithm used here is a DFS algorithm (in-depth search)
        """
        vertex_visited=[]
        # I take a vertex at random (I take the first key of the list of keys)
        vertex_processing= copy.copy(self.graph[list(self.graph.keys())[0]][1])
        #print(vertex_processing)
        while vertex_processing :
            v=vertex_processing.pop()
            if v not in vertex_visited :
                vertex_visited.append(v)
                if v not in self.graph :
                    return False
                for elem in self.graph[v][1] :
                    vertex_processing.append(elem)
        print(len(vertex_visited))
        return(len(vertex_visited)==len(self.graph))

    def making_cycle(self,start,end,edge_visited) :
        """
        This method searches for a cycle from a starting vertex and a vertex adjacent to the starting vertex (end).
        """
        keep_going=True
        while end!=start and keep_going==True :
            random_path=random.randint(0,len(self.graph[end][1])-1)
            # search for a potential arc that is not explored
            new_end=self.graph[end][1][random_path]
            while ((end,new_end)) in edge_visited :
                random_path=random.randint(0,len(self.graph[end][1])-1)
                new_end=self.graph[end][1][random_path]
            edge_visited.append((end,new_end))
            end=new_end
            # if we went back to our starting point (so we cycled)
            if start==end :
                keep_going=False
                for possible_next_step in self.graph[start][1] :
                    # if there is another arc adjacent to the starting vertex that we have not visited
                    if ((start,possible_next_step) not in edge_visited) :
                        end=possible_next_step
                        edge_visited.append((start,end))
                        keep_going=True
        return edge_visited

    def eulerian_cycle(self) :
        """
        This method makes it possible to see if there is an Eulerian cycle or not, and if it exists, returns the cycle of arc corresponding to the Eulerian cycle.
        """
        # check that the number of incoming arc = number of outgoing arc for each vertex
        for elem in self.graph:
            edge_in=self.graph[elem][0]
            edge_out=self.graph[elem][1]
            if len(edge_in)!=len(edge_out):
                print("ERREUR : THIS GRAPH DOES NOT CONTAIN AN EULERIAN CYCLE")
                return 0
                #exit()

        # research of the eulerian cycle
        start=list(self.graph.keys())[0]
        random_path=random.randint(0,len(self.graph[start][1])-1 )
        end=self.graph[start][1][random_path]
        edge_visited=[(start,end)]
        edge_visited=self.making_cycle(start,end,edge_visited)

        # if our cycle that we found is not the Eulerian cycle
        while len(edge_visited)!=self.number_edge :
            # I look at my arches that I visited
            found=False
            for tuples in edge_visited :
                # I look for each vertex that I crossed through with my arches if they have another path
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
            # to reform a cycle with our new vertex as our starting point, we need to look for the arc corresponding to our new peak
            for edge in edge_visited :
                if edge[0]==start :
                    edge_found=True

                if edge_found==True :
                    edge_visited_tmp.append(edge)
                else :
                    i=i+1
            for j in range(0,i) :
                edge_visited_tmp.append(edge_visited[j])

            # new bow list with as 1st bow our new starting vertex
            edge_visited=edge_visited_tmp
            start=edge_visited[len(edge_visited)-1][1]

            # search for an adjacent vertex that is not already visited (so a new arc path that we can explore)
            for potential_end in self.graph[start][1] :
                if ((start,potential_end)) not in edge_visited :
                    end = potential_end
                    break
            edge_visited.append((start,end))
            edge_visited=self.making_cycle(start,end,edge_visited)

        return self.build_genome(edge_visited)
