import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()                                #Creo el Grafo vacio

def explore(v):
    G.node[v]['visitado']='True'            #Marco el nodo como visitado
    numVecinos=G.neighbors(v)               #Miro los nodos adyacentes que hay respecto al nodo actual
    for i in numVecinos:
        if G.node[i]['visitado'] == 'False':#Para cada nodo adyacente al actual si no se ha visitado aun
            explore(i)                      #vuelvo a llamar a eplore() pasandole como parametro el nodo actual
            
def main():
    
    numAislados=0
                               
    G.add_edge(1,2)                         
    G.add_edge(2,3)                         #Creo los nodos y las conexiones del grafo
    G.add_edge(3,4)
    G.add_node(5)                           #Creo un nodo sin conexion, de esta forma será el unico nodo aislado
    
    nx.draw(G)                              
    plt.show()                              #Dibujo el grafo para ver que es correcto
    
    for i in G:                         
        G.node[i]['visitado']= 'False'      #Recorro todos los nodos y los inicializo como no visitados
        
    explore(1)                              #Llamo a la funcion recursiva explore y le paso el nodo inicial
    
    for i in G:
        if G.node[i]['visitado']=='False':  #Compruebo que nodo no ha sido visitado 
            numAislados=numAislados + 1     # y hago un contador de nodos no visitados
    
    print "Numero de Nodes Aillats: ",numAislados
    
main()