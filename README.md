# Projet_Genome !

REQUIRES :
-------------

python3 with library copy, random and argparse


HOW TO RUN
---------------

python3 src/main.py  [-h] [-rd RANDOM_GENOM] [-wg WITH_GENOM] [-out OUTPUT_FILE] [--with_check] length_reads number_reads length_kmers

flag :

-h : help

-rd : random genom (need a int after the flag)   example : -rd 10

-wg : with genom (need a path after the flag)    example : -wg example/res1.txt

!!! file which contains the genom have to be in fasta format or in a file which contains the genom ONLY !!!

--with_check : check if the start genom and genom built with the program are the same

-out : name of the outfile (default : result.txt)    example : -out genom_result.txt




example with random genom :  python3 src/main.py 100 5000 20 -rd 10000

example with genom in a fasta file :  python3 src/main.py 10 9 8 -wg example/res1.txt


