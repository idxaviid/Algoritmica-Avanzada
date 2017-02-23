#Xavi Cano Granada

def motxilla(maxpeso):
    
    #Leo el fichero de datos, su formato es [Valor,Peso]
    h= [[int(i) for i in line.split()] for line in open('dadesMotxilla.txt').readlines()]
    tuplas_de_tuplas = tuple(tuple(x) for x in h)
    matriz=list(tuplas_de_tuplas)
   
    #Guardo los objetos en una lista    
    items=matriz
    
    #Calculo el mejor valor
    def mejorvalor(i, j):
        if i == 0: 
            return 0
        valor, peso = items[i - 1]
        if peso > j:
            return mejorvalor(i - 1, j)
        else:
            return max(mejorvalor(i - 1, j),mejorvalor(i - 1, j - peso) + valor)

    j = maxpeso
    resultado = []
    #Voy comparando desde el final de la lista
    for i in xrange(len(items), 0, -1):
        if mejorvalor(i, j) != mejorvalor(i - 1, j):
            resultado.append(items[i - 1])
            j -= items[i - 1][1]
    resultado.reverse()    
    
    #Imprimo los resultados
    print "\nCapacidad inicial mochila:",maxpeso,"\nMaximo valor:",mejorvalor(len(items), maxpeso)
    print "Mejor combinacion de lista de items introducidos[valor,peso]:",resultado,
    

def main():
    
    #Capacidad inicial de la mochila
    c=10
    
    motxilla(c)
    
    
main()

'''

                    Analisis de eficiencia
                    ----------------------
                    
* Complejidad funcion motxilla():

n^2+n+1+1+1+1+n(1(1+1))+1+1+1 = n^2 + 2n

* Complejidad funcion motxilla():

1(1)+1(1)+1(1) = 1

* Complejidad funcion main():

1+1 = 1

* COMPLEJIDAD TOTAL:

((n^2 + 2n) * 1) + 1 = n^2 + 2n + 1


'''
