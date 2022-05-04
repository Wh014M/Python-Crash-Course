sandwiches = ['blt', 'turkey', 'ham', 'chopped cheese']
finished_sandwiches = []

while sandwiches:
	current_sandwiches = sandwiches.pop()

	print("I made your " + current_sandwiches.title())
	finished_sandwiches.append(current_sandwiches)

print("\nThe following sandwiches are finished: ")
for current_sandwich in finished_sandwiches:
	print(current_sandwich.title())