guests = input("Good Day, how many people are in your party? ")
guests = int(guests)

if guests > 8:
	print("Sorry, you will have to wait for a table.")
else:
	print("We have a table available, right this way.")