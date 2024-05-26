from programacion1_tp1.funcionteca import *

# DESARROLLAR EL MISMO COMPORTAMIENTO DE:
# map(func, lista)
# reduce(func, lista)
# filter(func, lista)
# sort(func) --------

lista_a_evaluar = [2,5,62,83,44,35,]

def mi_map(funcion, lista:list)->list:
    aux = []
    for i in lista:
        aux.append (funcion(i))
    return aux
#mama = mi_map(es_par, lista_a_evaluar) #es_par recibe un int y evalua si es par, si es par devuelve el numero, si no es par retorna None, no es el mejor ejemplo para aplicar un mapeo
#para que mi_map retorne una lista solo con los int que son pares seria asi:
#pero no es lo que buscamos en este caso
"""
    aux = []
        for i in lista:
            if funcion(i) != None
                aux.append (funcion(i))
        return aux
"""
#print (mama)



def es_mayor(numero_uno:int, numero_dos:int): #defino funcion basica para probar el reduce despues
    if numero_uno < numero_dos:
        return numero_dos
    return numero_uno
def mi_reduce(lista:list,funcion):
    acumulador = lista[0]
    for i in range (len(lista)):
        acumulador = funcion(acumulador, lista [i])  

    return acumulador
#prueba_reduce = mi_reduce(lista_a_evaluar, es_mayor)
#print (prueba_reduce)



def es_impar (int):#defino funcion basica para probar el filter despues
    if int % 2 == 1:
        return True
    else:
        return False
def mi_filter(lista:list, funcion):
    aux = []
    for i in lista:
        if funcion(i) == True:
            aux.append(i)
    return aux
#prueba_filter = mi_filter(lista_a_evaluar, es_impar)
#print(prueba_filter)



#para prueba de sorted:
tupla = [(3, 'Hernan', 350), (2, 'Lucas',351), (1, 'Jimena',349)]
diccionario = [{'nombre': 'Hernan', 'edad': 45}, 
               {'nombre': 'Lucas', 'edad': 30}, 
               {'nombre': 'Jimena', 'edad': 25}]
def mi_sorted(lista:list, key): #no funciona, no supe como ubicar la key en el codigo para que sea el dato a ordenar de cada elemento 
    lista_ordenada = []
    for i in range(len(lista)-1):
        for j in range( i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista
        
prueba_sorted = mi_sorted(tupla, 2)
print(prueba_sorted)


