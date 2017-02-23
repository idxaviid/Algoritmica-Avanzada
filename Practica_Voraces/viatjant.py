import networkx as nx
import random
import matplotlib.pyplot as plt

G = nx.complete_graph(5)
#nx.draw(G)
#plt.show()

altura = [] 
listanodo = [] 
      
def viatjant(G):
  
  for i,j in G.edges(): #Para cada arista genero un peso "al azar"
    G.edge[i][j]['peso'] = random.randint(1,5)  
    
  for i in G: #Para cada nodo le pongo una altura
    makeset(i)  
    
  aOrdenadas = 0 
  aOrdenadas =  sorted( G.edges(data=True), key = lambda edge: edge[2].get('peso',1)) #Ordeno las aristas de forma creciente por su peso
  lista = []
  
  #print "\nArestes del graf:"
  #print aOrdenadas
  
  for i in aOrdenadas:  #Para cada arista de las ordenadas anteriormente añado su "origen/destino" a cada una
    lista.append((i[0],i[1]))   
  
  minispat = [] 
  
  for i,j in lista: #Para cada arista de las ordenadas
    if find(i) != find(j):  #Si no genera ciclo
      minispat.append((i,j))  #Añado la arista a la lista de candidatas
      union(i,j)  #Hago la union a los nodos
  
  print "\nEl cicle simple de minim cost es:"    
  print minispat
    

def makeset(x):
  listanodo.append(x)
  altura.append(0)
  
def find(x):
  while x != listanodo[x]:
    x = listanodo[x]
  return x

def union(x,y):
  r = find(x)
  s = find(y)
  if r == s:
    return
  if altura[r] > altura[s]:
    listanodo[s] = r
  else:
    listanodo[r] = s
    if altura[r] == altura[s]:
      altura[s] = altura[s] + 1

viatjant(G)


#El programa se podria implementar por Prim o Kruskal, en este caso he elegido
#Kruskal añadiendo la heuristica(linea 21) de a cada iteracion tener siempre 
#la arista de menor peso y menor altura y comprobando que no se generen ciclos
#en el grafo al hacer las uniones.
