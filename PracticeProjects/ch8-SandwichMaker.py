# Practice project - Sandwich Maker

import pyinputplus as pyin

sandwichIngredients = []
sandwichPrice = 0

# Using inputMenu() for a bread type: wheat, white, or sourdough
breadPrices = {"Wheat":40, "White":35, "Sourdough":50}

breadType = pyin.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
sandwichIngredients.append(breadType)
sandwichPrice += breadPrices[breadType]
print("Selected Option: " + str(breadType) + "\n")

# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu
proteinPrice = {"Chicken": 90, "Turkey":110, "Ham":90, "Tofu":120}

proteinType = pyin.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
sandwichIngredients.append(proteinType)
sandwichPrice += proteinPrice[proteinType]
print("Selected Option: " + str(proteinType) + "\n")

# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
cheeseYN = pyin.inputYesNo("Would you like cheese with that? (Y/N)")
cheesePrice = {"Cheddar":10, "Swiss":20, "Mozzarella":14}

if cheeseYN == "yes":
	cheeseType = pyin.inputMenu(["Cheddar", 'Swiss', 'Mozzarella'], numbered=True)
	sandwichIngredients.append(cheeseType)
	sandwichPrice += cheesePrice[cheeseType]
	print("Selected Option: " + str(cheeseType) + "\n")

# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
mayoYN = pyin.inputYesNo("Add mayo?")

if mayoYN == "yes":
	sandwichIngredients.append("Mayo")
	sandwichPrice += 15

mustardYN = pyin.inputYesNo("Add mustard?")

if mustardYN == "yes":
	sandwichIngredients.append("Mustard")
	sandwichPrice += 15

lettuceYN = pyin.inputYesNo("Add lettuce?")

if lettuceYN == "yes":
	sandwichIngredients.append("lettuce")
	sandwichPrice += 10

tomatoYN = pyin.inputYesNo("Add tomato?")

if tomatoYN == "yes":
	sandwichIngredients.append("tomato")
	sandwichPrice += 10

# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
numOfSandwiches = pyin.inputInt("How many sandwiches do you want? ", min=1)

# Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
print("\nSandwich: ")
print(sandwichIngredients)
print("Price per sandwich: %s" % sandwichPrice)
print("Total Price: %s" % (sandwichPrice*numOfSandwiches))


