count = 1

while count <= 5:
    print("Count is", count)
    count += 1

print("=================================")

number = 0
while True:
    print(number)
    number += 1
    if number == 5:
        break

print("=================================")

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
else:
    print("loop finished")

print("=================================")

tasks = ["dishes", "homework", "walk dog"]

while tasks:
    current = tasks.pop()
    print("Doing: ", current)

while True:
    answer = input("Enter a whole number: ")
    try:
        number = int(answer)
        break
    except ValueError:
        print("Thats not a whole number, try again")

print(f"Thank you! You entered {number}")

password = ""
while password != "secret123":
    password = input("Enter passowrd: ")
    if password != "secret123":
        print("Wrong! Try again.")

print("Access granted")

