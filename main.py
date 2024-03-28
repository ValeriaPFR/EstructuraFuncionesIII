
# No modificar. Importación de módulos y librerías de Python
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# valores iniciales 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10 #nivel inicial 0 y los 9 niveles de las preguntas
# esta línea define la forma en la que se limpiará la terminal, si es Windows (op_sys se designa como 'cls', si no, 'clear'
op_sys = 'cls' if sys.platform == 'win32' else 'clear' 

# ----------------------------------------

os.system(op_sys) # limpiar terminal

print('Bienvenido a la Trivia')
opcion = input
('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
''')
# 1. validar opción
opcion = validate(['0','1'],opcion)

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print("Programa finalizado") #Cambiar luego
    time.sleep(2)
    os.system(op_sys)
    # finalizar programa
    
# Funcionamiento de preguntas
while correcto and n_pregunta < 3*p_level:
    
    if n_pregunta == 0:
        p_level = input('\n¿Cuántas preguntas por nivel? (Máximo 3): \n')
        # 3. Validar el número de preguntas por nivel
        p_level = int(validate(['1','2','3'],p_level))
        
    if continuar == 'y':
        #contador de preguntas
        n_pregunta += 1
        # 4. Escoger el nivel de la pregunta
        nivel = choose_level(n_pregunta,p_level)
        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        enunciado, alternativas = choose_q(nivel)
        #6. Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado,alternativas)
        
        respuesta = input(f'\nEscoja la alternativa correcta:\n> ').lower()
        # 7. Validar la respuesta entregada
        respuestas = validate(['a','b','c','d'],respuesta)
        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas,respuestas)

        if correcto and n_pregunta < 3*p_level:
            print('Muy bien sigue así!')
            continuar = input('Desea continuar? [y/n]: ').lower()
            #9. Validar si es que se responde y o no
            continuar = validate(['y','n'],continuar)
            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(5)
            os.system(op_sys)
        else: 
            print(f'Lo siento, conseguiste {n_pregunta - 1 } respuestas correctas,\n Sigue participando!!')
            time.sleep(8)
            os.system(op_sys)
            # exit()
    else: 
        print('Nos vemos la próxima vez, sigue practicando')
        time.sleep(5)
        exit()