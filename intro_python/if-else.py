"""
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Shorthand if statement
if x > 5: print("x is greater than 5")

# Shorthand if ... else statements
print("Even") if x % 2 == 0 else print("Odd")

# Nested If statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions

age = 20

if age >= 18 and age < 20:
    print("You are between 18 and 21")

MINI CHALLENGE: Club Entry
Ask the user to enter their age and store it in a variable called age.
Ask the user if they have a valid ID.(The user should enter "yes" or "no".)
Store the answer in a variable called has_id.
Determine admission rules:
If age is 21 or older AND has_id is "yes":
   print "Access Granted"
If age is 21 or older BUT has_id is "no":
   print "Access Denied - ID Required"
If age is between 18 and 20 inclusive:
   print "Access Limited"
Otherwise:
   print "Access Denied - Too Young"
Create a variable called can_enter:
 Set it to True only if the user is 21 or older AND has_id is "yes".
 Otherwise set it to False.
BONUS:
 If can_enter is True:
     print "Welcome inside!"
 Otherwise:
     print "Please see the front desk."
EXTRA BONUS:
 If the user enters a negative age,
 print "Invalid age entered."

age = input("Enter you age: ")
id = input("Do you have an ID (Enter \"yes\" or \"no\"): ")

has_id = False
if id == "yes":
    has_id = True

can_enter = False

print("\n")
if int(age) >= 21 and has_id:
    print("Acces granted.\n")
    can_enter = True
elif int(age) >= 21 and not has_id:
    print("Acces denied - ID required.\n")
elif int(age) >= 18 and int(age) <= 21:
    print("Acces limited.")
elif int(age) < 0:
    print("Invalid age\n")
else:
    print("Acces Denied - Too Young.\n")

if can_enter:
    print("Welcome inside\n")
else:
    print("please see the front desk\n")


my_list = [1, 2, 3, 4, 5]
print(my_list)

mix_list = [1, "apple", 3.5, True]
print(mix_list)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])
print(numbers[:4])
print(numbers[4:])
print(numbers[::2])

fruits[1] = "mango"
print(fruits[1])

fruits.append("pineapple")
print(fruits[-1])

fruits.insert(1, "kiwi")
print(fruits[1])

fruits.extend(["grape", "pear"])
print(fruits)

# REMOVINT ITEMS
fruits.remove("grape")
print(fruits)

fruits.pop()
print(fruits)


fruits.pop(0)
print(fruits)


fruits.clear()
print(fruits)


for fruit in fruits:
    print(fruit)

print(len(fruits))

numbers = [4, 2, 6, 1, 7, 9]

print(numbers.count(2))

print(numbers.index(2))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
"""


"""
#  MINI CHALLENGE: THE GROCERY LIST
# You're building a grocery list app.
# 1. Create a list called "groceries" with at least 5 items.
# 2. Print the first and last item using indexing.
# 3. Use slicing to print just the first 3 items.
# 4. Add "eggs" to the end of the list using append().
# 5. Insert "milk" at the very beginning of the list.
# 6. Remove one item using remove().
# 7. Check if "bread" is in the list — print a message either way.
# 8. Sort the list alphabetically and print it.
# 9. Print how many items are in the final list.
"""

groceries = ["cereal", "chicken", "bread", "onion", "butter"]
print(groceries)

print(groceries[0])
print(groceries[-1])

print(groceries[:3])

groceries.append("eggs")
groceries.insert(0, "milk")

print(groceries)

groceries.remove("butter")

print(groceries)

if "bread" in groceries:
    print("bread is on the list")
else:
    print("bread is not on the list")

groceries.reverse()

print(groceries)

groceries.sort()

print(groceries)

print(len(groceries))