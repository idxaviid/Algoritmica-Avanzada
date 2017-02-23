import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_adjlist("graf4.dat")                #Leo el ficher de datos y creo el grafo con sus respectivas conexiones

def dfs(v):
    G.node[v]['visitado']='True'                #Marco el nodo como visitado
    numVecinos=G.neighbors(v)                   #Creo una lista con los vecinos adyacentes que tiene el nodo actual
    print v,             
    numVecinos.sort()                           #Ordeno de manera ascendente la lista de vecinos
    for i in numVecinos:
        if G.node[i]['visitado'] == 'False':    #Para cada nodo adyacente al actual si no se ha visitado aun
            dfs(i)                              #vuelvo a llamar a dfs() pasandole como parametro el nodo actual
    
def bfs(v):    
    G.node[v]['distancia']=0                    #Asigno distancia cero al nodo actual
    cola=[]                                     
    cola.append(v)                              #Añado el nº nodo a la lista 
    n = 0
    while cola != []:                           
        u=cola.pop(0)                           #Elimino el primer elemento de la lista y lo guardo en u
        print u,
        n = G.neighbors(u)                      
        n.sort()                                #Ordeno de forma ascendente los vecinos de u
        for i in n:                             #Para cada vecino de u
            if G.node[i]['distancia']== 100:    
                cola.append(i)                  #Añado i a la lista,de esta manera no estará vacia y volvera a hacer el while
                G.node[i]['distancia']= G.node[u]['distancia'] + 1   #Incremento en 1 la distancia del nodo del cual venia      
                
def main():                                                
    for i in G:                                 #Recorro todos los nodos y les 
        G.node[i]['distancia']= 100             #pongo distancia "infinita"
  
    print "BFS:",
    bfs('1')                                    #Llamo a la funcion bfs() y le paso el nodo inicial
    
    for i in G:                                 #Recorro todos los nodos y los 
        G.node[i]['visitado']= 'False'          #inicializo como no visitado
    print "\nDFS:",    
    dfs('1')                                    #Llamo a la funcion recursiva dfs() y le paso el nodo inicial
    
    
main()
    
    
    
    
    
    

