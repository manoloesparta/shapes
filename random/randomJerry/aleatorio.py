import json
from random import randint, choice
from PIL import Image

def aleatorio():

	# Load data
	with open('data.json', 'r') as file:
		data = json.load(file)

	# Get grupos
	grupos_registrados = []
	imp = ""
	for i in range(len(data['grupos'])):

		actual = list(data['grupos'][i])[0]
		grupos_registrados.append(actual)

		imp += actual + ', '

	print(imp[:-2])

	# Choose grupo
	eleccion = input('Que grupo elige: ').lower()

	# If group doesnt exist
	if not eleccion in grupos_registrados:
		return 'elegir grupo valido'

	grupos = []
	for i in range(len(data['grupos'])):
		sample = list(data['grupos'][i].keys())[0]
		grupos.append(sample)

	direccion = grupos.index(eleccion)
	estudiantes = data['grupos'][direccion][eleccion]['estudiantes']

	# Find if group if exists
	for i in range(len(estudiantes)):

		maldito = choice(estudiantes)
		estudiantes.remove(maldito)

		# Open Image and print name
		if(maldito['ruta_img'] != ''):
			img = Image.open(maldito['ruta_img'])
			img.show()

		print('\n'+maldito['nombre'].title(), maldito['apellido'].title())

		sigue = input('Quiere seguir(s/n): ')

		if sigue[0] == 'n':
			break

		