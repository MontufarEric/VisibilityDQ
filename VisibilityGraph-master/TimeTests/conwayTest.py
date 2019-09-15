import networkx as nx
import numpy as np
import time
import matplotlib.pyplot as plt

def SerieToNetMod(serie):
    arrG1=[]
    G=nx.Graph()
    for Na in range (len(serie)):
        ya=serie[Na]
        maxslp=-1000
        for Nb in range(Na+1,len(serie)):
            yb=serie[Nb]
            slp=(yb-ya)/(Nb-Na)
            if slp > maxslp:
                arrG1.append((Na,Nb))
                maxslp=slp
                
    
    for i in range(len(serie)):
        G.add_node(i, y=serie[i])
                                    
    G.add_edges_from(arrG1)
    
    return(G)

def genConway(N):
	conway=[0,1,1]
	test=[]
	for n in range(3,N):
	    an=conway[conway[n-1]]+conway[n-conway[n-1]]
	    conway.append(an)
	    test.append(an/n)
	test=np.array(test)
	return(test)

for i in range(10):
	for n in range(1,8):
	    nn=n*10000
	    serie=genConway(nn)
	    start=time.time()
	    SerieToNetMod(serie)
	    stop=time.time()-start
	    print(nn,stop)