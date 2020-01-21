def coroutine(function):
	def wrapper(*args, **kwargs):
		gen = function(*args, **kwargs)
		next(gen) # или g.send(None)
		return gen
	return wrapper
