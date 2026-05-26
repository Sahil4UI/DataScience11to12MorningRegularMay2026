
order = int(input('''Press 1 to Order Pizza
Press 2 to Order Burger
Press 3 to Order Dessert :'''))

match (order):
    case 1:print("Your Pizza Ordered Successfully")
    case 2:print("Your Burger Ordered Successfully")
    case 3:print("Your Dessert Ordered Successfully")
    case _:print("Invalid Order")
