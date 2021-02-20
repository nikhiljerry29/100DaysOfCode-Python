def greet_with(name, location):
	print(f'Hello {name}')
	print(f'What it is like in {location}?')

def greet_with_1(location, name):
	print(f'Hello {name}')
	print(f'What it is like in {location}?')

greet_with('Nikhil', 'Kanpur')
greet_with_1('Nikhil', 'Kanpur')

# Keyword Arguments
greet_with(name = 'Nikhil', location = 'Kanpur')
