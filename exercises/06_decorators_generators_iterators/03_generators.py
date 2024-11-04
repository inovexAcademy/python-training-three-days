# Exercise 1. Create your first generator
def countdown(n):
    pass

for number in countdown(5):
    print(number)  # Expected output: 5, 4, 3, 2, 1, 0

# Exercise 2: Consuming the Generator with next()
countdown_generator = countdown(3)
while True:
    try:
        pass
    except StopIteration:
        pass

# Exercise 3: Discarding a Generator with close()
def simple_gen():
    pass

generator = simple_gen()
print(next(generator))
generator.close()

try:
    pass
except StopIteration:
    print("Cannot get value; generator is closed.")

# Exercise 4: Generator vs List Comprehension
# List comprehension example
list_squares = [x * x for x in range(10)]
print("List comprehension (can be reused):")
for square in list_squares:
    print(f"Square from list: {square}")  # Outputs the squares from 0 to 9
print("\nReusing the list comprehension:")
for square in list_squares:
    print(f"Reusing square from list: {square}")  # Outputs the squares from 0 to 9 again

# Generator comprehension example
generator_squares = []
# Perform the same example as in list comprehension
