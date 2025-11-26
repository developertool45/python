import time


def timer(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
		return result
	return wrapper

@timer
def hello(name):
	time.sleep(2)
	print(f"Hello,{name} !")

hello("roy")