prompt = input ("\nTell me something, and I will repeat it back to you:")
prompt += ("\nEnter 'quit' to end the program. ")

# message = " "
while prompt != 'quit':
	prompt = input(prompt)
	print(prompt)
	