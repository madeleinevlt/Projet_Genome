#!/usr/bin/python
# coding: utf-8

import graphe 
import random

##generateur aleatoire

def random_reads(length_genom, length_reads,number_reads) :
    genome=""
    while length_genom!=0 :
        genome=genome+random.choice('atgc')
        length_genom=length_genom-1
    #genome="atata"
    list_reads=[]
    list_pos=[]
    while number_reads!=0 : 
       random_number=random.randint(0,len(genome)-1)
       if random_number not in list_pos :
           if random_number+length_reads>=len(genome) :
                read=genome[random_number:]+genome[0:length_reads-len(genome[random_number:])]
           else :
                read=genome[random_number:random_number+length_reads]
           list_pos.append(random_number)
           number_reads=number_reads-1
           list_reads.append(read)
    print(genome)
    print(list_reads)
    print(list_pos)
    return(list_reads)     

def reads_to_kmers_graph(length_genom, length_reads,number_reads,length_kmers) :
    G=graphe.Graph()
    list_reads=random_reads(length_genom, length_reads,number_reads)
    for read in list_reads :
        #print("read :",read)
        for i in range(0,len(read)-length_kmers) :
            kmer=read[i:i+length_kmers] 
            #print("kmer :",kmer)
            kmers1=kmer[:-1]
            kmers2=kmer[1:]
            #print(kmers1, kmers2)
            G.add_edge(kmers1,kmers2)
    print(G.graph)
    print(G.is_connected())    

if __name__ == '__main__': 
    reads_to_kmers_graph(10,5,10,4)
