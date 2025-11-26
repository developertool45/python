file = open("error.txt", "w")
try:
	file.write("Hello")
except:
	print("Error")
finally:
	file.close()

with open("error.txt", "w") as file:
	file.write("chai aur python")