
run = True
orders = []

all_menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

all_menu_list = [
    "wings", "cookies", "spring rolls", "salmon", "steak",
    "meat tornado", "a literal garden", "ice cream", "cake",
    "pie", "coffee", "tea", "unicorn tears"
]

intro = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""

prompt = """
***********************************
** What would you like to order? **
***********************************
"""

outro = """**Thank you for visiting Snakes Cafe**
**Order Summary**"""

print(intro)
def display_menu():
    for menu in all_menu:
        print(menu)
        print("-" *6)
        for item in all_menu[menu]:
            print(item)
        print("")
    print(prompt)
display_menu()

def order_summary():
    order_set = set(orders)
    print(outro)
    for order in order_set:
        cnt = orders.count(order)
        s = ""
        if cnt > 1:
            s = "s"
        print(f"{cnt} order{s} of {order}")

while run:
    def order_menu():
        user_input = input("> ")
        if user_input.lower() not in all_menu_list and user_input.lower() != "quit":
            print("Item not in the menu")
        if user_input.lower() in all_menu_list:
            orders.append(user_input)
            cnt = orders.count(user_input)
            s = ""
            if cnt > 1:
                s = "s"
            print(f"{orders.count(user_input)} order{s} of {user_input} have been added to your meal")
        if user_input.lower() == "quit":
            import sys
            order_summary()
            sys.exit(0)
    order_menu()