def convertToNewBase(number=44, targetBase=6):
	newNum = ''
	powers = []
 
	for x in reversed(range(targetBase)):
		powers.append(2**x)
 
	for i, x in enumerate(powers):
		if number - x >= 0:
			newNum += '1'
			number = number - x
		else:
			newNum += '0'
 
	print(''.join(newNum))


