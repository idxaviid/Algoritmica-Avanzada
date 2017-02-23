
def motxila(capacitat,obj1,obj2):
    n=5
    i=0
    numObjetos=0
    optimi=capacitat
    valorMochila=0
    pesoMochila=0
    print "\nOBJETOS CON MEJOR VALOR:"
    print "Valor Peso"
    print"----- ----"    
    while i < n:                                                    
        if obj1[0][i] == obj2[0][i] and obj1[1][i] == obj2[1][i]:   #Si tiene mismo valor y peso
            print " ",obj1[0][i],"  ",obj1[1][i]                    #Muestro el valor y peso del objeto
            if capacitat >= obj1[1][i]:                             #Si la mochila aun no esta llena...
                capacitat=capacitat-obj1[1][i]                      #Resto el peso del objeto a la capacidad de la mochila
                valorMochila=valorMochila+obj1[0][i]                #Sumo el valor del objeto al valor de la mochila
                pesoMochila=pesoMochila+obj1[1][i]                  #Sumo el peso del objeto al peso de la mochila
                numObjetos+=1
                      
        if obj1[0][i] == obj2[0][i] and obj1[1][i] < obj2[1][i]:    #Si tiene mismo valor pero objeto1 menor peso
            print " ",obj1[0][i],"  ",obj1[1][i]
            if capacitat >= obj1[1][i]:
                capacitat=capacitat-obj1[1][i]
                valorMochila=valorMochila+obj1[0][i]
                pesoMochila=pesoMochila+obj1[1][i] 
                numObjetos+=1
        
        if obj1[0][i] == obj2[0][i] and obj1[1][i] > obj2[1][i]:    #Si tiene mismo valor pero objeto2 menor peso
            print " ",obj2[0][i],"  ",obj2[1][i] 
            if capacitat >= obj2[1][i]:
                capacitat=capacitat-obj2[1][i]
                valorMochila=valorMochila+obj2[0][i]
                pesoMochila=pesoMochila+obj2[1][i] 
                numObjetos+=1
        
        if obj1[0][i] < obj2[0][i] and obj1[1][i] == obj2[1][i]:    #Si objeto1 tiene menor valor pero mismo peso
            print " ",obj2[0][i],"  ",obj2[1][i] 
            if capacitat >= obj2[1][i]:
                capacitat=capacitat-obj2[1][i]
                valorMochila=valorMochila+obj2[0][i]
                pesoMochila=pesoMochila+obj2[1][i]
                numObjetos+=1
        
        if obj1[0][i] > obj2[0][i] and obj1[1][i] == obj2[1][i]:    #Si objeto1 tiene mayor valor pero mismo peso
            print " ",obj1[0][i],"  ",obj1[1][i] 
            if capacitat >= obj1[1][i]:
                capacitat=capacitat-obj1[1][i]
                valorMochila=valorMochila+obj1[0][i]
                pesoMochila=pesoMochila+obj1[1][i] 
                numObjetos+=1
        
        if obj1[0][i] > obj2[0][i] and obj1[1][i] < obj2[1][i]:    #Si objeto1 tiene mayor valor y menos peso
            print " ",obj1[0][i],"  ",obj1[1][i]
            if capacitat >= obj1[1][i]:
                capacitat=capacitat-obj1[1][i]
                valorMochila=valorMochila+obj1[0][i]
                pesoMochila=pesoMochila+obj1[1][i] 
                numObjetos+=1
        
        if obj1[0][i] > obj2[0][i] and obj1[1][i] > obj2[1][i]:    #Si objeto1 tiene mayor valor y mayor peso
            print " ",obj1[0][i],"  ",obj1[1][i]
            if capacitat >= obj1[1][i]:
                capacitat=capacitat-obj1[1][i]
                valorMochila=valorMochila+obj1[0][i]
                pesoMochila=pesoMochila+obj1[1][i] 
                numObjetos+=1
        
        if obj1[0][i] < obj2[0][i] and obj1[1][i] > obj2[1][i]:    #Si objeto1 tiene menor valor y mas peso
            print " ",obj2[0][i],"  ",obj2[1][i] 
            if capacitat >= obj2[1][i]:
                capacitat=capacitat-obj2[1][i]
                valorMochila=valorMochila+obj2[0][i]
                pesoMochila=pesoMochila+obj2[1][i] 
                numObjetos+=1
        
        if obj1[0][i] < obj2[0][i] and obj1[1][i] < obj2[1][i]:    #Si objeto1 tiene menor valor y menos peso
            print " ",obj2[0][i],"  ",obj2[1][i]
            if capacitat >= obj2[1][i]:
                capacitat=capacitat-obj2[1][i]
                valorMochila=valorMochila+obj2[0][i]
                pesoMochila=pesoMochila+obj2[1][i] 
                numObjetos+=1
        i=i+1  
    print "* Nº de objetos metidos en mochila:",numObjetos
    print "* Valor total de la mochila:",valorMochila,"€"
    print "* Peso total de la mochila:",pesoMochila,"kg"
    optimi=100*(optimi-capacitat)/optimi
    capacitat = 100 - optimi
    print "* Capacidad restante de la mochila:",capacitat,"%"
    print "* Optimización de la mochila:",optimi,"%"
    
    
    
def main():
    c = input("Quants Kg de capacitat te la motxila?:\n")
                 #valor            #peso
    objeto1=([5, 1, 2, 9, 5], [5, 2, 5, 4, 7])
    objeto2=([5, 9, 8, 8, 9], [5, 9, 5, 2, 9]) 
    motxila(c,objeto1,objeto2)
main()


#Creo que hay 3 maneras de enfocar el problema, seleccionar los objetos con menor
#peso, mayor valor o mejor relacion valor/peso, en mi caso he optado por seleccionar
#los de mayor valor. No es una solución del todo optima, puesto que seguro que podré
#llevar un poco menos de valor con mucho menos peso. Lo ideal seria seleccionar siempre
# la mejor relacion valor/peso, ya que generalmente sea lo mas optimo.