"""
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

loveMatrix = {'T' : 0, 'R' : 0, 'U' : 0, 'E' : 0, 'L' : 0, 'O' : 0, 'V' : 0}

combinedName = name1 + name2
for x in loveMatrix :
    loveMatrix[x] = combinedName.count(x)

firstDigit = 0
for x in ['T', 'R', 'U', 'E'] :
    firstDigit += loveMatrix[x]

lastDigit = 0
for x in ['L', 'O', 'V', 'E'] :
    lastDigit += loveMatrix[x]

score = (10 * firstDigit) + lastDigit

if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score <= 40 or score >= 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}")