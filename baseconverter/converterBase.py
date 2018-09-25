def converterBase(base, num):

	arr = []
	hexa = {10:'A',11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

	while num != 0:
		new = num % base
		if new >= 10:
			new = hexa[new]
		arr.append(new)
		num = num // base

	arr.reverse()
	return "".join(map(str, arr))