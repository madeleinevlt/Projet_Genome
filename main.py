#!/usr/bin/python3
# coding: utf-8

import graphe 
import genom
import argparse




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='De Novo assembly for circulary genom')
    parser.add_argument("-rd","--random_genom",type=int,help="define the lenght the genom")
    parser.add_argument("length_reads",help="define the lenght of reads",type=int)
    parser.add_argument("number_reads",help="define the number of reads",type=int)
    parser.add_argument("length_kmers",help="define the lenght of kmers",type=int)
    parser.add_argument("-wg","--with_genom",type=str,help="define the past of a fasta file of a genom")
    parser.add_argument("-out","--output_file",type=str,help="Name of the output file which contain the genom result")
    args=parser.parse_args()
    if args.random_genom==None and args.with_genom==None :
        print("Vous devez choisir au moins une option")
        exit()

    if args.random_genom!=None and args.with_genom!=None :    
        print("Vous devez choisir seulement une option")
        exit()

    if args.random_genom!=None :
        genom_start,brujin_graph=genom.reads_to_kmers_graph(args.random_genom,args.length_reads,args.number_reads,args.length_kmers)

    if not brujin_graph.is_connected() :
        print("Le graphe n'est pas connexe")
        exit()
    else :
        genom_result=brujin_graph.eulerian_cycle()    
    
    if genom.areRotations(genom_start, genom_result):
        print("The genom found with the program and the genom input are the same ")
    else:
        print("The genom found with the program and the genom input are not the same")

##faire un output avec les résultats
##faire génome à partir d'un input

