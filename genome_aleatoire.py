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
    #print("GENOME au debut :",genome)
    print("TAILLE GENOME :",len(genome))
    return(genome,list_reads)     

def reads_to_kmers_graph(length_genom, length_reads,number_reads,length_kmers) :
    G=graphe.Graph()
    genome,list_reads=random_reads(length_genom, length_reads,number_reads)
    for read in list_reads :
        for i in range(0,len(read)-length_kmers) :
            kmer=read[i:i+length_kmers] 
            kmers1=kmer[:-1]
            kmers2=kmer[1:]
            G.add_edge(kmers1,kmers2)
    #print(G.graph)
    print(G.is_connected())    
    genome_result=G.eulerian_cycle()
    #print("TAILLE DU GRAPHE :",len(G.list_edge))
    return (genome,genome_result)


# Python program to check if strings are rotations of
# each other or not
 
# Function checks if passed strings (str1 and str2)
# are rotations of each other
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
 
    # Now check if str2 is a substring of temp
    # string.count returns the number of occurences of
    # the second string in temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
    
# This code is contributed by Bhavya Jain
if __name__ == '__main__': 
    #genome_start,genome_end=reads_to_kmers_graph(10000,100,5000,50)
    genome_start,genome_end=reads_to_kmers_graph(10000,100,5000,20)
    if areRotations(genome_start, genome_end):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")

