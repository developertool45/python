import time
def chahe(func):
	chached_value = {}
	def wrapper(*args):
		if args in chached_value:
			return chached_value[args]
		
		result = func(*args)	

		chached_value[args]= result
		return result
	
	return wrapper
@chahe
def sum(a, b):
	time.sleep(4)
	return a+b

print(sum(4,5))
print(sum(4,5))
print(sum(8,5))