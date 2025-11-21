items = ["apple", "banana", "orange", "apple", "mango", "banana"]

unque_item= set()

for item in items:
	if item in unque_item:
		print('Duplicate item :', item)
		break
	unque_item.add(item)
