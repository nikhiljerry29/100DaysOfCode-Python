"""
BMI Calculator 2.0
It should tell them the interpretation of their BMI based on the BMI value.

1. Under 18.5 they are underweight
2. Over 18.5 but below 25 they have a normal weight
3. Over 25 but below 30 they are slightly overweight
4. Over 30 but below 35 they are obese
5. Above 35 they are clinically obese.

"""

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