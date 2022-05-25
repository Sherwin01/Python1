x = 500
if x > 100:
    raise Exception("if x is bigger than 100 this will be an error")

try:
    print(variable_1)

except:
    print("variable_1 is not defined")

for i in range(6):
    print("i'm so happy!")

try:
    print(12*6)
except:
    print("this operation cant be performed.")
else:
    print("this can be performed")

best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert best_burger == "McDonald's"

