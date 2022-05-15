
orders = []
special_orders = []
all_menu_list = []

all_menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

intro = """
*****************************************
**     Welcome to the Snakes Cafe!     **
**     Please see our menu below.      **
**                                     **
**   To quit at any time, type "quit"  **
*****************************************
"""

prompt = """
***********************************
** What would you like to order? **
***********************************
"""

outro = """**Thank you for visiting Snakes Cafe**
\n**Order Summary**"""

print(intro)
def display_menu():
    for menu in all_menu:
        print(menu)
        print("-" *6)
        for item in all_menu[menu]:
            print(item)
            all_menu_list.append(item.lower())
        print("")
    print(prompt)
display_menu()

def order_summary():
    order_set = set(orders)
    special_order_set = set(special_orders)
    print(outro)
    for order in order_set:
        cnt = orders.count(order)
        s = ""
        if cnt > 1:
            s = "s"
        print(f"{cnt} order{s} of {order}")
    for special in special_order_set:
        cnt = special_orders.count(special)
        s = ""
        if cnt > 1:
            s = "s"
        print(f"Special: {cnt} order{s} of {special}")


def order_menu():
    user_input = input("> ")
    if user_input.lower() not in all_menu_list and user_input.lower() != "quit":
        print("Item not in the menu, press Y to place special order")
        custom = input("> ")
        if custom.lower() == "y":
            special_orders.append(user_input)
            cnt = special_orders.count(user_input)
            s = ""
            if cnt > 1:
                s = "s"
            print(f"Special: {cnt} order{s} of {user_input} have been added to your meal")
    if user_input.lower() in all_menu_list:
        orders.append(user_input)
        cnt = orders.count(user_input)
        s = ""
        if cnt > 1:
            s = "s"
        print(f"{cnt} order{s} of {user_input} have been added to your meal")
    if user_input.lower() == "quit":
        import sys
        order_summary()
        sys.exit(0)

while True:
    order_menu()