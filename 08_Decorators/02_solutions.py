import time
def debug(func):
	def wrapper(*args, **kwargs):
		func_args = ",".join(str(arg) for arg in args)
		func_kwargs = ",".join(f"{k} = {v}" for k,v in kwargs.items())

		print(f"args : {func_args}, kwargs: {func_kwargs}")

		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
		return result
	return wrapper
@debug
def hello(name):
	time.sleep(1)
	print(f"Hello, {name}!")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


print(hello("aman"))
print(greet("rajneesh", "Namaste"))