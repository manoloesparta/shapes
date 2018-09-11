from converterBase import converterBase
from deconverterBase import deconverterBase

while True:
	base = int(input('En que base es el numero: '))
	num = input('Que numero quieres convertir: ')

	if base == 2:
		num = deconverterBase(base=2, num=num)
		print('Decimal: ', num)
		print('Hexadecimal: ', converterBase(base=16, num=num))

	elif base == 10:
		print('Binary: ', converterBase(base=2, num=int(num)))
		print('Hexadecimal: ', converterBase(base=16, num=int(num)))

	elif base == 16:
		num = deconverterBase(base=16 ,num=num)
		print('Decimal: ', num)
		print('Binary: ', converterBase(base=2, num=num))

	else:
		print('No tengo esa opcion')

