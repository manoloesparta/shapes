# Convierte decimal a cualquier base

def converterBase(base, num):

	arr = []
	hexa = {10:'A',11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

	while num != 0:

		new = num % base

		if new >= 10:
			new = hexa[new]

		arr.append(new)
		num = num // base

	reverse = []
	for i in range(len(arr)):
		reverse.append(arr[- i - 1])

	return "".join(map(str, reverse))