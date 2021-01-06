height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height * height))
print(f'Your BMI is {bmi}')
