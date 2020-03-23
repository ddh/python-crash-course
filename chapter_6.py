pokemon = { 'charmander': 'fire', 'bulbasaur': 'grass', 'squirtle': 'water' }
print("Charmander's type is: " + pokemon['charmander'].title())

for mon in pokemon:
  print(mon.title() + "'s type is: " + pokemon[mon].title())

pokemon = {}
pokemon['pikachu'] = 'electric'
print(pokemon['pikachu'])

pokemon = { 'charmander': 'fire', 'bulbasaur': 'grass', 'squirtle': 'water' }
for mon in pokemon:
	print(mon)

for key, value in pokemon.items():
  print("Key: " + key)
  print("Value: " + value)
  print("")

for mon in sorted(pokemon.keys()):
	print(mon)

pokemon = { 'charmander': 'fire', 'ponyta': 'fire', 'growlithe': 'water' }
pokemon_list = set(pokemon.values())
print(pokemon_list)