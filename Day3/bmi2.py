height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height * height))
print(f'Your BMI is {bmi}')

if bmi <= 18.5 :
    print("You are underweight.")
elif bmi > 18.5 and bmi <= 25 :
    print("You have a normal weight.")
elif bmi > 25 and bmi <= 30 :
    print("You are slightly overweight.")
elif bmi > 30 and bmi <= 35 :
    print("You are obese.")
elif bmi < 35 :
    print("You are clinically obese.")