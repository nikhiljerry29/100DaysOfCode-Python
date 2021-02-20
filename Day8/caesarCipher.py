from cipher_art import logo
import os

os.system('cls')
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction ,text, shift_amount):
	output_text =  ""
	while (shift_amount > 26) :
		shift_amount = shift_amount // 26

	for letter in text:
		position =  alphabet.index(letter)
		if direction == 'encode':
			new_postion = position + shift_amount
			if new_postion > 26:
				new_postion -= 26

		elif direction == 'decode':
			new_postion = position - shift_amount
			if new_postion < 0:
				new_postion += 26

		new_letter = alphabet[new_postion]
		output_text += new_letter

	print(f'Your {direction}d text :: {output_text}')

execution = 'yes'

while (execution == "yes") :
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(direction = direction, text = text, shift_amount =  shift)
	execution = input("Do you want to re-enter (yes or no):\n").lower()
	if execution == 'no' :
		print("Bye!! Bye!!")