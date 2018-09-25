def deconverterBase(base, num):
	hexa = {'A':10, 'B':11, 'C': 12, 'D':13, 'E':14, 'F':15}
	
	num = list(str(num).upper())
	maxbit = base ** (len(num) - 1)

	num_arr = []
	for i in num:
		try:
			num_arr.append(hexa[i])
		except:
			num_arr.append(i)

	num = list(map(int, num_arr))
	
	result = []
	for i in range(len(num)):
		maxbit = maxbit // base
		res = maxbit * num[i]
		result.append(res)

	return sum(result)
