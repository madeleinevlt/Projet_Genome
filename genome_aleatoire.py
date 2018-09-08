# coding: utf-8


import random

##generateur aleatoire

def random_reads(length_genom, length_reads,number_reads) :
    genome=""
    for i in range(0,length_genom) :
        genome=genome+random.choice('atgc')
    
    list_reads=[]
    for j in range(0,number_reads) :
       random_number=random.randint(0,length_reads-1)
       if random_number+length_reads>=length_genom :
           read=genome[random_number:]+genome[0:length_reads-len(genome[random_number:])]
       else :
           read=genome[random_number:random_number+length_reads]
       list_reads.append(read)
    print(genome)
    print(list_reads)     



if __name__ == '__main__': 
    random_reads(5,6,6)

