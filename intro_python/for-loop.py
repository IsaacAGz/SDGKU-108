fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("=================================")

for letter in "Hello":
    print(letter)

print("=================================")

for x in range(5):
    print(x)

print("=================================")

for x in range (2,6):
    print(x)

print("=================================")

for x in range(0, 10, 2):
    print(x)

print("=================================")

for x in range(3):
    print(x)
else:
    print("loop done")

print("=================================")

for number in [3, 2, 7, 9]:
    if number % 2 == 0:
        print("Found and even number")
        break
else:
    print("no even numbers found")

print("=================================")

for x in range(20):
    if x == 5:
        continue
    elif x == 8:
        break
    print(x)

print("=================================")

num = int(input("Enter a number: "))

for x in range(1, 11):
    print(num * x)