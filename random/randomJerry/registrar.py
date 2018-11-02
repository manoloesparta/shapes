import json
import os
from shutil import copyfile

def registrar():

	# Get inuts
	nombre = input('\nNombre: ').lower()
	apellido = input('Apellido: ').lower()
	grupo = input('Grupo: ').lower()
	imagen = input('Ruta Imagen: ')

	ruta_img = ''

	# Load images
	if imagen[-5:-1] == '.jpg' or imagen[-5:-1] == '.png':
		if imagen[-1] == ' ':
			imagen = imagen[:-1]

		if not 'imgs' in os.listdir():
			os.mkdir('imgs')

		copyfile(imagen, './imgs/' + str(len(os.listdir('./imgs/'))) + '.jpg')
		ruta_img = './imgs/' + str(len(os.listdir('./imgs/')) - 1) + '.jpg'
		
	else:
		print("\nNo se pudo cargar la imagen")

	# Loading data
	with open('data.json', 'r') as file:
		data = json.load(file)

	# Formatting new data
	new_data = {
		'nombre':nombre,
		'apellido':apellido,
		'ruta_img': ruta_img
	}

	# Load existing groups
	grupos_registrados = []

	if len(data['grupos']) > 1:
		for i in range(len(data['grupos'])):
			grupos_registrados.append(list(data['grupos'][i])[0])

	# Check for new groups
	if not grupo in grupos_registrados:

		print('Grupo no encontrado, creando ...')

		new_data = {
			grupo: { "estudiantes":[new_data] }
		}

		data['grupos'].append(new_data)

	else:

		for i in range(len(grupos_registrados)):
			
			if grupos_registrados[i] == grupo:

				data['grupos'][i][grupo]['estudiantes'].append(new_data)

	# Remove default group
	if data['grupos'][0] == {}:
		data = { 'grupos': data['grupos'][1:] }

	# Register new data
	with open('data.json', 'w') as file:
		json.dump(data, file)
		print('REGISTRADO')