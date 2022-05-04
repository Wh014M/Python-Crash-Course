current_users =['mack', 'blake', 'winston', 'lamar', 'rivers', 'cooper']
new_users = ['ekeler', 'hyde', 'hopkins', 'LAMAR', 'rivers']

for users in new_users:
	if users.lower() in current_users:
		print("The username " + users + " is taken, please choose another username.")
	else:
		print("The username " + users + " is available.")