# 8-1. Message:
def display_message():
  print("I am learning about functions")

display_message()

# 8-2. Favorite Book:
def favorite_book(title):
  print("One of my favorite books is " + title)

favorite_book("Harry Potter and The Sorceror's Stone")

def describe_pet(animal_type='dog'):
	print(animal_type)

describe_pet() # "dog"
describe_pet("hamster") # "hamster"