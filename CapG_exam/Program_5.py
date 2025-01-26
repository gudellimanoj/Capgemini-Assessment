# 5 Shopping Cart

def shoppingCart():
    cart = []
    while True:
        print("1. Add item")
        print("2. View cart")
        print("3. Calculate total")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            cart.append((item, price))
        elif choice == 2:
            print("Cart items:")
            for item, price in cart:
                print(item, price)
        elif choice == 3:
            total = sum([price for item, price in cart])
            print("Total price:", total)
        elif choice == 4:
            break
shoppingCart()
