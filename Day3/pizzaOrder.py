"""
Price list for Pizza
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Toppings Charges
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
addPepperoni = input("Do you want pepperoni? Y or N ").upper()
extraCheese = input("Do you want extra cheese? Y or N ").upper()

priceChart = {'S': 15, 'M': 20, 'L': 25}

totalBill = priceChart[size]

pepperoniCharges = 3 
if addPepperoni == 'Y':
	totalBill += 3;  
	if size == 'S':
		# Pepperoni for Small Pizza: +$2
		totalBill -= 1;  

cheeseCharges = 1
if extraCheese == 'Y':
	totalBill += 1

print(f"Your final bill is: Rs.{totalBill}")

	