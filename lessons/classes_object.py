"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    #attribute definitions
    size: str
    toppings: int
    extra_cheese: bool


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False 
print(Pizza)
print(a_pizza)
print(a_pizza.size)