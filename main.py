flavors = ["vanilla", "chocolate", "strawberry", "cookies_n_cream", "bubblegum"]
toppings = ["almonds", "banana_slices", "chocolate syrup", "caramel syrup", "white_chocolate_chips"]

ice_cream = dict(zip(flavors, toppings))

print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})

print(ice_cream)
