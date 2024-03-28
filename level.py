"""
Summary:
Determina el nivel de dificultaad de la pregunta.
Args:
- n_pregunta: Número de la pregunta en integer
- p_level: Número integuer que indica el máx número de preguntas por nivel.

Returns:
- Un string que indica el nivel de dificultad.
"""
#Especificación del nivel de dificultad por pregunta, mediante un ciclo 'for'
def choose_level(n_pregunta, p_level):

    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2*p_level:
        level = 'intermedias'
    else:
        level = 'avanzadas'
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias