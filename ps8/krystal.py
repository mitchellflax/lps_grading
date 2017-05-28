# primeLister.py

# this function will determine if a number is prime 
def isPrime(number):
	for prime in range(2,number):
		k = number % prime
		
		# program will return false if no remainder
		if k == 0:
			return False 
		
		# program will return true for all prime numbers in a certain range  
		elif k != 0:
			return True

# execution begins 
# this is where the prime numbers are put into a different file 
myFile = open("primes.txt", "w")
for cookies in range(2,10000):
	if isPrime(cookies):
		myFile.write(str(cookies) + '\n')
		print(str(cookies))
