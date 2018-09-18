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
    parser.add_argument("--with_check", action="store_true", help="check if your start genom is the same as the genom made by the program")
    args=parser.parse_args()
    if args.random_genom==None and args.with_genom==None :
        print("You have to choose 1 option between --random_genom and --with_genom")
        exit()

    if args.random_genom!=None and args.with_genom!=None :    
        print("You have to choose only 1 option between --random_genom and --with_genom")
        exit()

    if (args.length_kmers+1)>args.length_reads :
        print("The length of a kmer can't be equal or higher than the length of a read")
        exit()
    
    if args.random_genom!=None :
        if args.length_reads>args.random_genom :
            print("The length of a read can't be higher than the length of the genom")
            exit()
        genom_start,brujin_graph=genom.reads_to_kmers_graph(args.random_genom,args.length_reads,args.number_reads,args.length_kmers)
        #print("START GENOM :",genom_start)
        print("LENGTH OF GENOM AT START :",len(genom_start))
        print("NUMBER OF EDGE : ",brujin_graph.number_edge)
    
    if args.with_genom!=None :
        genom_start,brujin_graph=genom.reads_to_kmers_graph(args.with_genom,args.length_reads,args.number_reads,args.length_kmers)    

    if not brujin_graph.is_connected() :
        print("Graph is not related")
        exit()
    else :
        genom_result=brujin_graph.eulerian_cycle()  
        if args.output_file :
            outfile=args.output_file
        else :
            outfile="result.txt"
        with open(outfile,"w") as fillout :
            fillout.write(genom_result)    
              
    
    if args.with_check :
        if genom.areRotations(genom_start, genom_result):
            print("The genom found with the program and the genom input are the same ")
        else:
            print("The genom found with the program and the genom input are not the same")

