ordinal_numbers = [1,2,3,4,5,6,7,8,9]


for numbers in ordinal_numbers:
	if numbers == 1:
		print(str(numbers) + "st")

	elif numbers == 2:
		print(str(numbers) + "nd")

	elif numbers == 3:
		print(str(numbers) + "rd")

	else:
		print(str(numbers) + "th")
