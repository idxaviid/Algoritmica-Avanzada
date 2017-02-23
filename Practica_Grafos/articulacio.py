import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_adjlist("graf5.dat")                #Leo el ficher de datos y creo el grafo con sus respectivas conexiones
numVecinos = 0   
lista1 = []                                 

def dfs(v):
    numVecinos = G.neighbors(v)                 #Creo una lista con los vecinos adyacentes que tiene el nodo actual
    numVecinos.sort()                           #Ordeno de manera ascendente la lista de vecinos
    lista1.append(v)                            #Añado a un a lista el nodo actual
    G.node[v]['visited'] = 'True'               #Marco como visitado el nodo actual
    for i in numVecinos:                        
        if G.node[i]['visited'] == 'False':     #Para cada nodo adyacente al actual si no se ha visitado aun
            dfs(i)                              #vuelvo a llamar a dfs() pasandole como parametro el nodo actual
                    
def main():
    lista2 = []
    for i in G:                                 #Para cada nodo del grafo aplico un dfs() eliminando el nodo (i)
        for j in G:
            G.node[j]['visited'] = 'False'
        lista2 = G.neighbors(i)
        G.remove_node(i)
        if i == '1':                            #Si empiezo el dfs() por el nodo 1 , como previamente lo he eliminado
            dfs('2')                            #por logica deberé seguir por el 2
        else:
            dfs('1')
        if len(lista1) != G.order():            #Si la longitud de lista1 es diferente a nº nodos del grafo -1 el nodo actual será un punto de articulación
            print "Punts d'articulació del graf: Node(",i,")"   
            
        for v in lista2:                        
            G.add_edge(i,v)                     #Vuelvo a crear el nodo eliminado para poder hacer el dfs() en la siguiente iteracion
        del lista1[0:]                          #Limpio la lista para poder usarla sin problema en la siguiente iteración
            
main()