

def coroutine(function):
	def wrapper(*args, **kwargs):
		gen = function(*args, **kwargs)
		next(gen) # или g.send(None)
		return gen
	return wrapper


def sum():
	sum_values = 0

	while True:
		try:
			new_value = yield sum_values
		except StopIteration:
			print('done')
		else:
			sum_values += new_value


def sum2():
	sum_values = 0

	while True:
		try:
			new_value = yield sum_values
		except StopIteration:
			print('done')
			break
		else:
			sum_values += new_value
	return sum_values