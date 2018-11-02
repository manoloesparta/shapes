from randomJerry.registrar import registrar
from randomJerry.aleatorio import aleatorio

def main():


	while True:

		print('\nMENU PRINCIPAL')

		decision = int(input('\n1. Registrar\n2. Elegir\n3. Salir\nElige una opcion: '))

		if decision == 1:
			registrar()
		elif decision == 2:
			aleatorio()
		elif decision == 3:
			break
		else:
			print('Opcion no valida')

if __name__ == '__main__':
	main()