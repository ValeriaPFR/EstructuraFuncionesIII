#Se importa el módulo 'preguntas', como 'p', que contiene el diccionario ´pool_preguntas'
import preguntas as p
#Docstring
"""
Imprime la pregunta y las alternativas de respuestas
Args:
    enunciado (str): La pregunta.
    alternativas (list): Lista de alternativas.

Returns:
    None
"""
def print_pregunta(enunciado, alternativas):
    # Imprimir enunciado y alternativas
    preguntas = enunciado
    #Se inicia un bucle 'for' que itera sobre cada carácter en la cadena preguntas.
    for i in preguntas:
        #Se asigna el carácter actuala la variable 'contador', 'i' representa cada carácter de la cadena preguntas. 
        contador = i
        #Se imprime el carácter actual en líneas aparte.
        print(f"{contador}\n")
    
    preguntas2 = alternativas
    lista = ["A", "B", "C", "D"]
    for i,k in zip(lista,preguntas2):
        print(f"{i}. {k[0]}")
    pass
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado en el siguiente print
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4