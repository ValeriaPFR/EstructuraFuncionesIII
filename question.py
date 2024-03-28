import preguntas as p
import random
from shuffle import shuffle_alt
"""
Summary:
Escoge una pregunta y mezcla  sus alternativas según el nivel de dificultad indicado.
Args:
- dificultad: Un string que  indica el nivel de dificultad de la pregunta
Returns:
- Una tupla que contiene la preguntay  una lista con las respuestas, mezcladas
"""

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    # print(opciones)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f"pregunta_{n_elegido}"] 
    alternativas = shuffle_alt(pregunta)

    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')