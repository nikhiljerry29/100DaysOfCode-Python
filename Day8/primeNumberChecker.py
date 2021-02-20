def primeNumberChecker(number):
	isPrime = True;
	for x in range(2,number):
		if number % x == 0:
			isPrime = False
	if isPrime:
		print(f'{number} is a prime number.')
	else:
		print(f'{number} is a prime number.')

primeNumberChecker(number = 13)