#preguntas básicas
preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuál es el resultado de 2 + 2?'],
    'alternativas': [['5', 0], 
                    ['4', 1], 
                    ['3', 0], 
                    ['2', 0]]},
    'pregunta_2': {'enunciado':['¿Qué animal es conocido como el "rey de la selva"?'],
    'alternativas': [['Lobo', 0], 
                    ['León', 1], 
                    ['Elefante', 0], 
                    ['Tigre', 0]]},
    
    'pregunta_3': {'enunciado':['¿Cuál es el planeta más grande del sistema solar'],
    'alternativas': [['Urano', 0], 
                    ['Júpiter', 1], 
                    ['Venus', 0], 
                    ['Tierra', 0]]}
}
#preguntas intermedias
preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Quién escribió "Don Quijote de la Mancha"?'],
    'alternativas': [['Gabriel García Márquez', 0], 
                    ['Miguel de Cervantes', 1], 
                    ['William Shakespeare', 0], 
                    ['Federico García Lorca', 0]]},
    
    'pregunta_2': {'enunciado':['¿Cuál es el río más largo del mundo?'],
    'alternativas': [['Nilo', 0], 
                    ['Amazonas', 1], 
                    ['Misisipi', 0], 
                    ['Biobío', 0]]},
    
'pregunta_3': {'enunciado':['¿Quién pintó la famosa obra "La noche estrellada"?'],
    'alternativas': [['Claude Monet', 0], 
                    ['Vincent van Gogh', 1], 
                    ['Leonardo da Vinci', 0], 
                    ['Pablo Picasso', 0]]}
}
#preguntas avanzadas
preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Cuál es la molécula responsable del efecto invernadero?'],
    'alternativas': [['Metano (CH4)', 0], 
                    ['Dióxido de carbono (CO2)', 1], 
                    ['Óxido nitroso (N2O)', 0], 
                    ['Oxígeno (O2)', 0]]},
    
    'pregunta_2': {'enunciado':['¿Qué es la estratificación de las semillas?'],
    'alternativas': [['Proceso de desarrollo de frutos', 0],
                    ['Proceso de tratamiento para estimular la germinación', 1], 
                    ['Proceso de polinización', 0], 
                    ['Proceso de reproducción asexual', 0]]},
    
'pregunta_3': {'enunciado':['¿Cuál es la diferencia entre una lista y una tupla en Python?'],
    'alternativas': [['Las listas están ordenadas y las tuplas no', 0], 
                    ['Las listas son mutables y las tuplas son inmutables', 1], 
                    ['Las listas son más largas que las tuplas', 0], 
                    ['Las tuplas son más importantes que las listas', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                'intermedias': preguntas_intermedias,
                'avanzadas': preguntas_avanzadas}