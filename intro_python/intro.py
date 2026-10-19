print("Hello world!")
print(2)
print(5 + 3)
print(True)

# This is a comment

"""
    This
    is all
    a 

    comment
"""

# Creating a variable
name = "Isaac Angulo"
age = 28

print(name + " is " + str(age) + " years old.")

"""
Mini challenge 
Write a briefe story using 5 variables and print in the terminal.
Use different data types (str, int,...)
Use concatinate to create the story
"""

num = 2
text = "The old man took a walk"
flag = False
fl = 72.5
char = 'h'

print(text + ". He came back home " + str(num) + " hours later. It was " + str(fl) + " degrees by then. He said his favorite letter is " + char + " but this is " + str(flag) + ".")


print(f"{text}. He came back home {num} hours later. It was {fl} degrees by then. He said his favorite letter is {char} but this is {flag}.")

print(f"""\n{text}. He came back home {num} hours later. 
It was {fl} degrees by then. 
He said his favorite letter is {char} but this is {flag}.""")

print(f"\n{type(name)}")
print(f"\n{type(num)}")
print(f"\n{type(flag)}")

user_name = input("Please enter your name: ")
print(f"User input: {user_name}")
print(f"{type(user_name)}")

new_age = int(input("Enter your age: "))
print(f"{type(new_age)}")
print(f"Age added: {age + new_age}")

"""
Pizza Calculator
Ask how many slices of pizza and how many people.
Use math operators to calculate slices per person.
Show the result with an f-string.
"""

slices = int(input("Enter the amount of slices: "))
people = int(input("Enter the number of people: "))

print(f"Then each person should get {slices / people} slices")
