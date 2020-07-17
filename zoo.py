# # Tuples (ordered, immutable & allows duplicates)

# my_tup = (1, 2, 3, 3, "hello")
# print(my_tup)

# # Loop through the values in the tuple
# for value in my_tup:
#     print(value)

# # You CAN reassign a variable to a new tuple, though.
# my_tup = ("I'm thirsty", "I'm hungry")
# print(my_tup)

# # If you have one value in a tuple, you have to follow it with a comma!
# my_little_tup = ("hello",)

# print(isinstance(my_little_tup, tuple))
# print(type(my_little_tup))
# print(my_little_tup)
# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("Lion", "Tiger", "Bear", "Monkey", "Snake",
       "Tortoise", "Turtle", "Elephant", "Zebra", "Penguin")
print(zoo)


zoo.index("Penguin")
print(zoo.index("Penguin"))


animal_to_find = "Tiger"
if animal_to_find in zoo:
    print(f"The {animal_to_find} was found")
(first_animal, second_animal, third_animal, forth_animal, fifth_animal,
 sixth_animal, seventh_animal, eight_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(tenth_animal)
zoo = list(zoo)
zoo.extend(['Giraffe', 'Aardvark', 'Hippopotamus'])
zoo = tuple(zoo)
print(zoo)
