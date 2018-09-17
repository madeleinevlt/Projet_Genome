#!/usr/bin/python3
# coding: utf-8

import graphe 
import random


def create_genom(length_genom) :
    """
    Create a random genom 
    Input : length of the genom
    Output : a string which contain the genom
    """

    genom=""
    while length_genom!=0 :
        genom=genom+random.choice('atgc')
        length_genom=length_genom-1
    return genom

#def genom_from_fasta(path) :
#    with open(path)

def random_reads(genom,length_reads,number_reads) :
    """
    Function which create random reads from a genom
    Input : genom, reads length, number of reads
    Oupit : a list which contains reads
    """
    list_reads=[]
    list_pos=list(range(len(genom)))
    while number_reads!=0 : 
        random_number=random.choice(list_pos)
        list_pos.remove(random_number)
        if random_number+length_reads>=len(genom) :
            read=genom[random_number:]+genom[0:length_reads-len(genom[random_number:])]
        else :
            read=genom[random_number:random_number+length_reads]
        number_reads=number_reads-1
        list_reads.append(read)
    return list_reads

def reads_to_kmers_graph(l_genom, length_reads,number_reads,length_kmers) :
    """
    Function which create a kmer graph from a read list
    """
    G=graphe.Graph()
    if type(l_genom)==int :
        genom=create_genom(l_genom)
    list_reads=random_reads(genom, length_reads,number_reads)
    for read in list_reads :
        for i in range(0,len(read)-length_kmers) :
            kmer=read[i:i+length_kmers] 
            kmers1=kmer[:-1]
            kmers2=kmer[1:]
            G.add_edge(kmers1,kmers2)
    return(genom,G)        


def areRotations(genom1, genom2):
    """
    Function which check is a string is a rotation of an other (if 2 circular genoms are the same)
    """
    s1=len(genom1)
    s2=len(genom2)
    if s1!=s2 :
        return False
    temp=genom1+genom1
    if (temp.count(genom2)> 0):
        return True
    else:
        return False
    

#100000,100,50000,55


