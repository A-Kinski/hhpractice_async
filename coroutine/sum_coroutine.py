def sum():
	sum_values = 0

	while True:
		try:
			new_value = yield sum_values
		except StopIteration:
			break
		else:
			sum_values += new_value
	return sum_values

