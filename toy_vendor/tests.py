import random
tripulantes=['Luis Angel Guarin',
    'Camilo Ortega',
    'Camilo Orozco',
    'Andrés Cañón Muñoz',
    'Sandra Giraldo', 
    'Catherin Sarasty',
    'Juan Camilo Cespedes Romero',
    'Gabriel Jaime Osorio H',
    'Henry David Díaz Velandia',
    'Daniel Melo Salamanca',
    'Javier Hernández',
    'Johan Manuel Collazos',
    'Juan Esteban Gomez',
    'Brayan Baez Mejia',
    'Oswaldo Pamo',
    'Jorge Eliecer Perez',
    'Angie Pino',
    'Johan Zubieta Marín',
    'Sebastian Ariza',
    'Jorge Morantes',
    'José Alfredo Jiménez Franco',
    'Hector Jesid Florez Macias',
    'Paul Leteliel Moros Anacona', 
    'Miguel Angel Alfonso Baquero', 
    'Santiago Andres Ramirez',
    'Juan Manuel Rodriguez Farias',
    'Felipe Andrés Silva Gómez',
    'Wilmer Andres Nova Pinilla',
    'Francisco Martínez Torreglosa',
    'Carlos Ortiz',
    'Fabián Henao',
    'Leonel Doria',
    'Fredy Caballero',
    'Shalem Janna Díaz',
    'Pablo Andrés Villegas',
    'Luis Bautista',
    'Esteban Velasco Sanabria',
    'Gregorio Morales Pajaro',
    'Jeison Steven Rodríguez', 
    'Ricardo Rincon' ]
grupos =[]
activo = True
while(activo):
    subgrupo =[]
    print('Grupo N')
    if len(tripulantes) >= 5:    
        for a in range(5):
            random_number = random.randint(0,len(tripulantes)-1)
            print(tripulantes[random_number])
            subgrupo.append(tripulantes[random_number])
            del tripulantes[random_number]
        grupos.append(subgrupo)
        print('=========================')
    else:
        print('Ultimo grupo')
        for b in range(len(tripulantes)):
            print(tripulantes[b])
        tripulantes=[]
    if (len(tripulantes) <= 0):
        activo = False

