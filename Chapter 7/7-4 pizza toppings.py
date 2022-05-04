prompt = "Please enter your pizza toppings: "

while True:
	pizza = input(prompt)

	if pizza == 'quit':
		break
	else:
		print("I'll add " + str(pizza) + " to your pizza!")