#! based uopn argument / parameter  there are diffrent ways to call out functions :-
#  a real time example of args & parameter functions calling 
#!  This simulates placing an order on a shopping app.
def place_order(customer_name, /, item, quantity=1, *extras, discount=0, **details):
    print("Customer:", customer_name)
    print("Item:", item)
    print("Quantity:", quantity)

    # Extra items (like toppings, add-ons)
    if extras:
        print("Extras:", extras)

    # Discount
    print("Discount:", discount, "%")

    # Additional details (like address, payment mode)
    if details:
        print("Other Details:", details)

    print("-" * 40)


# ✅ Calling the function in different ways

place_order(
    "sawai",
    "Pizza",
    2,
    "Cheese", "Olives",
    discount=10,
    address="Ahmedabad",
    payment="UPI"
)