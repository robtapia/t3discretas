def largoDeCaminoMasCorto(pelicula1,pelicula2,diccionario):
    grafo=aGrafo(diccionario)
    peliculas=list(diccionario.keys())
    indicePelicula1=peliculas.index(pelicula1)
    indicePelicula2=peliculas.index(pelicula2)
    n=1
    while(True):
        g=expmatriz(grafo,n)
        if n>1000:
            inf = 9e999
            return inf
        if g[indicePelicula1][indicePelicula2]>0:
            n=n+1
        else:
            break
    return g[indicePelicula1][indicePelicula2]+1
    

##Sacada de mi tarea 3 del semestre pasado
def expmatriz(matriz,n):
    if n==1:
        return matriz
    elif n%2==0:    ##n par
        A=expmatriz(matriz,n/2)
        return multiplicacion(A,A)
    else:  ## n impar
        return multiplicacion(matriz,expmatriz(matriz,n-1))


##Sacada de mi tarea 3 del semestre pasado
def multiplicacion(A,B):          ##para los casos en los que usaremos esta funcion
    anchoA=len(A)       ##las medidas de todas las matrices son iguales
    largoA=len(A[0])
    anchoB=len(B)
    largoB=len(B[0])
    C=[0]*anchoA
    for i in range(len(C)):
        C[i]=[0]*largoA
    ##Ahora tengo una matriz C vacia donde se ira guardando la matriz resultante
    for x in range(anchoA):
        for y in range(largoA):
             for z in range (anchoB):   
                C[x][y]+= A[x][z]*B[z][y]
            
    return C





def aDic(peliculas,actoresPorPelicula):
    resultado={}
    for i in range(len(peliculas)):
        resultado[peliculas[i]]=actoresPorPelicula[i]
    return resultado


coleccion= ["Eficiente y furioso 3: Dijkstra Drift","Mi papa es un grafo!","Discretas 4, una nueva esperanza"]
actores=[["Peibl Towers","Vim Diesel"],["Vim Diesel","Maryl Streep", "Andrea Lalancha"],["Andrea Lalancha","Kevin Bacon"]]
A=aDic(coleccion,actores)

def aGrafo(diccionario):
    cantidad=len(diccionario)
    peliculas=list(diccionario.keys())
    a=[]
    for i in range(cantidad):
        b=[None]*cantidad
        a.append(b)
    for j in range(cantidad):
        for l in range(cantidad):
            if (set(diccionario[peliculas[l]]) & set(diccionario[peliculas[j]])):
                a[j][l]=1
            else:
                a[j][l]=0
    return a
print(aGrafo(A))

def NroMinPeliculas(A,coleccion,actores):
    
    MS="Maryl Streep"
    KB="Kevin Bacon"
    dic=aDic(coleccion,actores)
    peliculasConA=[]
    peliculasConMS=[]
    peliculasConKB=[]
    for key in dic.keys():
        if A in dic[key]:
            peliculasConA.append(key)
        if MS in dic[key]:
            peliculasConMS.append(key)
        if KB in dic[key]:
            peliculasConKB.append(key)
    largosAMS=[]
    largosMSKB=[]
    for i in range(len(peliculasConA)):
        for j in range(len(peliculasConMS)):
            largosAMS.append(largoDeCaminoMasCorto(peliculasConA[i],peliculasConMS[j],dic))
    for i in range(len(peliculasConMS)):
        for j in range(len(peliculasConKB)):
            largosMSKB.append(largoDeCaminoMasCorto(peliculasConMS[i],peliculasConKB[j],dic))
    return min(largosAMS)+min(largosMSKB)
print(NroMinPeliculas("Peibl Towers",coleccion,actores)) 

