# This creates an empty list so i can add my prime numbers
Primes = []
#This selects numbers from this range
list = range(1, 10000)
# This puts the amount of factors for each number in a list then adding the number to the primes list if there was exactly 2 factors
for num in list:
	MultiNums = []
	div = num 
        while div > 0:		
		if num % div == 0:
			MultiNums.append(div) 
		div = div - 1
	if len(MultiNums) == 2:
		Primes.append(num)
# this prints the primes list
print Primes
#Writs the list to the file
file = open("prime.txt", "w")
for p in Primes:
	file.write(str(p) + "\n")
file.close()


