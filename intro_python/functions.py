"""
MINI CHALLENGE: PASSWORD STRENGTH
Create a function called check_password().
1. The function should accept one parameter:
      - password
2. Inside the function:
      - If the password length is 8 or more:
            return "Strong Password"
      - If the password length is between 5 and 7:
            return "Medium Password"
      - Otherwise:
            return "Weak Password"
3. Ask the user to enter a password.
4. Call the function and store the returned result.
5. Print the result.
BONUS:
If the password contains an exclamation mark (!),
print "Special character detected!"
"""
def check_password(password):
    length = len(password)
    if '!' in password:
        print("Special character detected!")

    if length >= 8:
        return "Strong password"
    if length >= 5 and length <= 7:
        return "Medium password"
    else:
        return "Weak password"

user_password = input("Please create a password: ")
print(check_password(user_password))
