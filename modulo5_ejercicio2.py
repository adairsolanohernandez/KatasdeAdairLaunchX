primerplaneta = input('Introduzca la distancia del sol para el primer planeta en KM')

segundoplaneta = input('Introduzca la distancia desde el sol para el segundo planeta en KM')

primerplaneta = int(primerplaneta)
segundoplaneta = int(segundoplaneta)
Distancia = segundoplaneta - primerplaneta

print(Distancia)

Distancia_millas = Distancia * 0.621
print(Distancia_millas) 