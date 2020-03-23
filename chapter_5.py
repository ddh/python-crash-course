foods = ['sushi', 'lasagna', 'broccoli']
for food in foods:
	if food == 'sushi':
		print("My favorite food is " + food + "!")
	else:
		print(food.title() + " is so-so.")

apple = True
print(apple)

age = 18
print(age > 16 and age < 21) # False

# Check if element in list:
vegetables = ['broccoli', 'cucumber', 'eggplant']
print('broccoli' in vegetables) # True

# Check if NOT in list:
print('banana' not in vegetables)

if 'banana' not in vegetables:
	print("A banana is not a vegetable!")

age = 21
if age >= 21:
	print("You can drink!")
elif age >= 16:
	print("You can drive!")
else:
	print("Not old enough to do either!")

requested_toppings = []
if requested_toppings:
	print("we got toppings!")
else:
	print("hey, we ran out of toppings!")