import random

def gasolineres(n,b,d,p):
    print "\nLlista de benzineres respecte a Sitges:",b,"kms"
    i=0
    j=0
    p.append(0)  
    while j < n:    
        if b[0]> d: #Si la primera gasolinera esta a mas de 100kms
            print "\n!!!GASOLINA INSUFICIENT!!!, el coche no pot continuar... es un trasto vell...no val per res..."
            return 1   
      
        if b[j]-p[i] >= d : #Si la distancia que hay desde donde estoy a la siguiente es mayor que 100
            i=i+1           #Hago una parada
            p.insert(i,b[j-1])  #Añado a la lista de paradas la gasolinera 
        j=j+1
    print "\nEl coche ha parat a les benzineres que estan a:",p[1:],"kms"
    print "\nNumero de parades:",i

def main():
    d=100
    b=[]
    p=[]
    n=random.randint(5,10)  #Genero entre 5 y 10 gasolineras de forma aleatoria
    
    for k in range(n):                  
        b.append(random.randint(1,400)) #Genero una gasolinera a distancia aleatoria y la añado a la lista
    
    bOrdenada=sorted(b) #Ordeno de menor a mayor, la lista de distancias de gasolineras
    gasolineres(n,bOrdenada,d,p)        
        
main()    

#El algoritmo recibe un nº de gasolineras y lista con las distancias de estas 
#respecto al origen, la idea es parar cuanto mas tarde mejor y ir comparando la 
#diferencia entre la gasolinera actual y la mas proxima y compararla con la gasolina
#que tiene el coche, segun el resultado, se para o no. 
        
         
