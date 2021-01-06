two_digit_number = input("Type a two digit number: ")
two_digit_number = int(two_digit_number)

sum = (two_digit_number // 10) + (two_digit_number % 10)
print(f'The sum of digits in Two Digit Number is {sum}')