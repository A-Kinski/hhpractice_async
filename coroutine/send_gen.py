
def simple_gen_01():
	value = yield
	print('simple generator received:', value)

def simple_gen_02():
	x = 'simple generator start value'
	value = yield x
	print('simple generator received:', value)
