planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

planets_ingresados = input('Ingrese el nombre de un planeta)')

planet_index = planets.index(planets_ingresados)
print('Planeta es ' + planets_ingresados)
print(planets[0:planet_index])

print('Los planetas son ' + planets_ingresados)
print(planets[planet_index + 1:])