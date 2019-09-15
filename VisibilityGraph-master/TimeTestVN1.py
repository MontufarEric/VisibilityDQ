import networkx as nx
import numpy as np
import time


def SerieToNetMod(serie):
    arrG1=[]
    G=nx.Graph()
    for Na in range (len(serie)):
        ya=serie[Na]
        maxslp=-1000
        for Nb in range(Na,len(serie)):
            yb=serie[Nb]
            slp=(yb-ya)/(Nb-Na)
            if slp > maxslp:
                arrG1.append((Na,Nb))
                maxslp=slp
                
    
    for i in range(len(serie)):
        G.add_node(i, y=serie[i])
                                    
    G.add_edges_from(arrG1)
    
    return(G)



    for i in range(10):
    for n in range(6):
        nn=10**(i+2)
        serie=np.random.randint(1,100,nn)
        start=time.time()
        G=SerieToNetMod(serie)
        stop=time.time()-start
        f=open("random1.txt",'a+')
        stri=str(nn)+" "+str(stop)+"\n"
        f.write(stri)
        f.close