from catalog import store_items

cart = []

def menu():
    print("\nMenu")
    print(" 1. View Catalog")
    print(" 2. View Product")
    print(" 3. View Cart")
    print(" Q.- Quit")

def header(text):
    print("---------------------")
    print(text)
    print("---------------------")

def add_product_cart(prod_id):
    found = False
    for prod in store_items:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)
            print(f'{prod["title"]} added to your cart.')
            break

    if not found:
        print("** ERROR: Invalid ID")

def print_catalog():
    header("- Our Catalog -")
    for prod in store_items:
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')

    answer = input("Type ID to add a product (N to close): ")       
    if answer.lower == 'n':
        return
    else:
        add_product_cart(answer)


def search_product():
    text = input("Please enter a product title:").lower()
    found = False

    for prod in store_items:
        if prod["title"] == text:
            found = True
            print(f'Product found | ID: {prod["id"]} | {prod["title"]} | ${prod["price"]:.2f}')
            choice = input("Do you want to add this item to your cart? (y/n)")

            if choice == 'y':
                add_product_cart(prod["id"])

    if not found:
        print("Product not found")

def view_cart():
    header("Your Cart")
    total = 0
    if len(cart) == 0:
        print("Your cart is empty")
        return

    for prod in cart:
        print(f'  {prod["title"]} | ${prod["price"]:<15.2f}')
        total += prod["price"]

    print("  =====================")
    print(f'  Your total is: {total:.2f}') 


options = ""
while options != 'q' and options !='Q':
    header("Welcome to Store x")
    menu()

    options = input("Choose and option:")

    if options == "1":
        print_catalog()
    elif options == "2":
        search_product()
    elif options == "3":
        view_cart()
    elif options == 'q' or options == 'Q':
        print("Thank you for your visit")
    else:
        print("Invalid Option")
