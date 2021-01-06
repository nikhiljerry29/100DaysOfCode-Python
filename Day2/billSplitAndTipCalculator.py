print("Welcome to SplitBill Calculator")
billAmount = float(input("Enter your bill amount\n"))
tip = float(input("What percentage tip you want to give?(10%, 12% and  15%)\n"))
numberOfPersons = int(input("Number of people in bill splitting\n"))

totalAmount = billAmount * (1 + tip * 0.01)
splitAmount = round(totalAmount/numberOfPersons, 2)

print(f'Each person should pay Rs.{splitAmount}')