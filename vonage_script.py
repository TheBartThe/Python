import random

while True:	
	while True:
		try:
			num1 = int(input('Type your first whole number:\n'))
			break
		except ValueError:
			print('This is not a whole number')
			continue
	while True:
		try:
			num2 = int(input('Type your second whole number:\n'))
			break
		except ValueError:
			print('This is not a whole number')
			continue
	while True:
		try:
			num3 = int(input('Type your third whole number:\n'))
			break
		except ValueError:
			print('This is not a whole number')
			continue
	while True:
		try:
			num4 = int(input('Type your fourth whole number:\n'))
			break
		except ValueError:
			print('This is not a whole number')
			continue
	while True:
		try:
			num5 = int(input('Type your fifth whole number:\n'))
			break
		except ValueError:
			print('This is not a whole number')
			continue
	while True:
		try:
			num6 = int(input('Type your sixth whole number:\n'))
			break
		except ValueError:
			print('This is not a whole number')
			continue
	numbers = [num1, num2, num3, num4, num5, num6]
	while True:
		option = input('Pick an option from 1 to 5 to perform on your numbers:\n1. Subtraction\n2. Multiplication\n3. Pick a random number\n4. Show your number from highest to lowest\n5. Show your numbers from lowest to highest\n')
		if option in '12345':
			break
		else:
			print('Please select a number from 1 to 5')
			continue
	if (option == '1'):
		result1 = num1 - num2
		result2 = num2 - num3
		result3 = num3 - num4
		result4 = num4 - num5
		result5 = num5 - num6
		print(f'{result1}, {result2}, {result3}, {result4}, {result5}')
	elif (option == '2'):
		product = num1 * num2 * num3 * num4 * num5 * num6
		result = {'InputNumber1': num1, 'InputNumber2': num2, 'InputNumber3': num3, 'InputNumber4': num4, 'InputNumber5': num5, 'InputNumber6': num6, 'Multiplication': product }
		print(result)
	elif (option == '3'):
		result = random.choice(numbers)
		print(result)
	elif (option == '4'):
		numbers.sort(reverse=True)
		print(numbers)
	elif (option == '5'):
		numbers.sort()
		print(numbers)
	continue