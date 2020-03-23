# 4-3. Counting to Twenty
for num in range(1,21):
  print(num)

# 4-4. One Million
million = range(1, 1000001)
for num in million:
  print(num)

# 4-5. Summing a Million:
million = range(1, 1000001)
print(min(million) == 1)
print(max(million) == 1000000)
print(sum(million))

# 4-6. Odd Numbers:
odd_numbers = range(1,21,2)
for odd_num in odd_numbers:
  print(odd_num)

# 4-7. Threes:
threes = range(3, 31, 3)
for num in threes:
  print(num)

# 4-8. Cubes:
numbers = range(1,11)
for num in numbers:
  print(num**3)

# 4-9. Cube Comprehension:
cubes = [num**3 for num in range(3,11)]
for cube in cubes:
  print(cube)

pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pikachu', 'meowth']
print(pokemon[0:3]) # Returns elements 0, 1, 2 (not 3)
print(pokemon[:3]) # Default starts at beginning of list
print(pokemon[:2]) # Start at beginning; bulbasaur, charmander, squirtle

# Slicing to include up until the end
print(pokemon[2:]) # squirtle, pikachu, meowth

pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pikachu', 'meowth']
for mon in pokemon[3:]:
	print(mon)

pizza_toppings = ['pepporoni', 'pineapple', 'anchovies']
copy_toppings = pizza_toppings[:] # This copies from the first to the last element
for topping in copy_toppings:
  print(topping)

# 4-10. Slices:
pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pikachu', 'meowth']
print("The first three items in the list are: " + str(pokemon[:3]))
print("Three items from the middle of the list are: " + str(pokemon[1:4]))
print("The last three items in the list are: " + str(pokemon[-3:]))

# 4-13. Buffet:
foods = ('pizza', 'sushi', 'lobster', 'soup', 'cheesecake')
for food in foods:
  print(food)