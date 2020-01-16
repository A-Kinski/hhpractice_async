def subgen2():
	x = 'Subgen start value'
	value = yield x
	print('Subgen received:', value)

