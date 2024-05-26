from programacion1_tp1.funcionteca import *

"""
Cadenas de caracteres:

1-Crear un algoritmo que determine si una cadena dada es un palíndromo 
(un palíndromo es una palabra o frase que se lee de la misma forma de 
atrás para adelante o viceversa. Ejemplo: Somos o no somos)

2-Desarrolle un algoritmo que cuente la cantidad de vocales y de 
consonantes en una palabra

3-Desarrolle una función que cuente la cantidad de dígitos que contiene 
una cadena de texto

4-Desarrollar una función que elimine todos los caracteres de una cadena 
que no sean alfanuméricos

5-Crear una función que invierta una cadena de caracteres. No esta 
permitido utilizar [::-1], deberán implementar su propia lógica

6-Desarrollar un algoritmo que encuentre las palabra mas largas y mas 
cortas de una cadena dada. 
"""
def punto_uno():
    """
    1-Crear un algoritmo que determine si una cadena dada es un palíndromo 
    (un palíndromo es una palabra o frase que se lee de la misma forma de 
    atrás para adelante o viceversa. Ejemplo: Somos o no somos)
    """
    string_correcto = "somos o no somos"
    string_incorrecto = "aca probamos el que estaria mal"

    def es_palindromo (cadena:str):
        aux = cadena.replace(" ", "")
        invertida = aux[::-1]
        if aux == invertida:
            return True
        return False
        

    print (es_palindromo(string_correcto))
    print (es_palindromo(string_incorrecto))
#punto_uno()

def punto_dos():
    """
    2-Desarrolle un algoritmo que cuente la cantidad de vocales y de 
    consonantes en una palabra
    """
    string_correcto = "qwertyuiop"
    string_incorrecto = "a1 2 qwertyuiop"
    def contar_vocales_y_consonantes (cadena:str):
        """
        Recibe string, no cuenta espacios\n
        Retorno 0 = vocales\n 
        Retorno 1 = consonantes
        """
        if validar_solo_alfabeticos(cadena,0,100000000) == True:
            aux2 = cadena.replace(" ", "") #saca espacios
            aux = aux2.lower() #convierte todo en minuscula
            lista = list(aux)
            contador_vocales = 0
            contador_consonantes = 0 
            for i in lista:
                if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                    contador_vocales +=1
                else:
                    contador_consonantes +=1
            
            return contador_vocales, contador_consonantes
        else:
            return print("No se puede calcular si hay numeros en el string")
        
    print(f"la cantidad de vocales es {contar_vocales_y_consonantes(string_correcto)[0]} y la cantidad de consonantes es {contar_vocales_y_consonantes(string_correcto)[1]}")
    print (contar_vocales_y_consonantes(string_incorrecto))
#punto_dos()

def punto_tres():
    """
    3-Desarrolle una función que cuente la cantidad de dígitos que contiene 
    una cadena de texto
    """
    string_correcto = "somos o no somos" #tiene 16 digitos

    def contar_digitos(cadena:str):
        lista = list(cadena)
        return len(lista)

    print(f"El string tiene {contar_digitos(string_correcto)} digitos")
#punto_tres()

def punto_cuatro ():
    """
    4-Desarrollar una función que elimine todos los caracteres de una cadena 
    que no sean alfanuméricos
    """
    string_prueba = "qwertyuiop/*+-"

    def solo_alfanumericos (cadena:str):
        aux = "".join(filter(str.isalnum, cadena))

        return aux
    
    return print(solo_alfanumericos(string_prueba))
#punto_cuatro ()

def punto_cinco():
    """
    5-Crear una función que invierta una cadena de caracteres. No esta 
    permitido utilizar [::-1], deberán implementar su propia lógica
    """
    string_prueba = "qwertyuiop"
    def invertir_str (cadena:str):
        aux = ""
        for i in cadena:
            aux = i + aux
        return aux
    print (f"El string ingresado es {string_prueba} y el mismo invertido es {invertir_str(string_prueba)}")
#punto_cinco()

def punto_seis():
    """
    6-Desarrollar un algoritmo que encuentre las palabra mas largas y mas 
    cortas de una cadena dada. 
    """
    string_prueba = "aca vamos aa probar las palabras mas largas" #mas larga palabras y mas corta aa

    def buscar_palabra_mas_corta_y_mas_larga(cadena:str):
        lista = cadena.split(" ")
        palabra_mas_corta = lista[0]
        palabra_mas_larga = lista[0]

        for i in lista:
            if len(i) > len(palabra_mas_larga):
                palabra_mas_larga = i
            if len(i) < len(palabra_mas_corta):
                palabra_mas_corta = i
        print (f"La palabra mas corta es: {palabra_mas_corta}")
        print (f"La palabra mas larga es: {palabra_mas_larga}")

    buscar_palabra_mas_corta_y_mas_larga(string_prueba)
punto_seis()