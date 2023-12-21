# Create list of toppings
toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]

# Create list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Number of occurrences of $2 in the prices list
num_two_dollar_slices = prices.count(2)

# Number items in toppings list
num_pizzas = len(toppings)

# Print store ad 
print(f"We sell {num_pizzas} different kinds of pizzas!")

# Create 2D list combining prices and toppings lists
pizza_and_prices = [[x,y] for x,y in zip(prices, toppings)]
print(pizza_and_prices)

# Sort menu in ascending order by price
pizza_and_prices.sort()
print(pizza_and_prices)

# Store first menu element in new variable
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Store last menu element in new variable
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Sold out of most expensive pizza. Remove it from the menu
pizza_and_prices.pop()
print(pizza_and_prices)

# Add new topping, 'peppers' to the menu
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Store 3 cheapest pizzas in a new variable
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
