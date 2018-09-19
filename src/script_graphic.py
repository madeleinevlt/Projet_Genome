import graphe
import genom_functions as genom
import argparse
import matplotlib.pyplot as plt



if __name__ == "__main__":

    listkmer=[0,1,2,3,4,5,6,7]
    listtrue=[0,0,0,0,0,0,0,0]
    for k in range(1,5000,10) :
        print(k)
    #k=9
        genom_start,brujin_graph=genom.reads_to_kmers_graph(10000,100,5000,20)
        print(brujin_graph.is_connected())
        if brujin_graph.is_connected() :
            genom_result=brujin_graph.eulerian_cycle()
            if genom_result==0 :
                listkmer.append(k)
                listtrue.append(0)
            else :
                listkmer.append(k)
                listtrue.append(1)
        else :
                listkmer.append(k)
                listtrue.append(0)

    plt.plot(listkmer,listtrue)
    plt.show()
    print(listkmer)
