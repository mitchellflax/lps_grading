primeList = []
def isPrime(myNum):
	# divides every number by numbers lower than itself
	for x in range(2, myNum - 1):
		if myNum % x == 0:
			return False
		# b/c code doesn't work properly needed to add this extra code that takes out things divisible by 3 and 5
		elif myNum % 5 == 0:
			return False
		elif myNum % 3 == 0:
			return False
		# else it adds number to a list and returns true to be added to file
		else:
			primeList.append(myNum)
			return True
# adds prime numbers to file and closes it
myFile = open("numbersPrime.txt", "w")
for n in range(2, 10001):
	if isPrime(n):
		myFile.write(str(n) + "\n")
myFile.close()

print(primeList)
