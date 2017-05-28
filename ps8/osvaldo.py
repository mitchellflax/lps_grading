#prime number bois




numberList = [] 

#creates a function for prime numbers. 

def primeNumbers(myNum):
#for everything in my range, it checks if the biggest number is divisible by the numbers in the range.  
	for thing in range(2,myNum):
		if myNum % thing == 0:
			return False			
	return True
 
#for every number in the range, it runs the prime Numbers function
for numbers in range(2,10000):
	kev = primeNumbers(numbers)
	if kev == True:
		numberList.append(numbers)
#writes to a file and then closes it. 
my_file = open("primeNumber.txt", "w")
my_file.write(str(numberList))
my_file.close()

print(numberList)
