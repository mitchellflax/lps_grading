#creates an empty list
list = []
#determines whether number is a prime number or not and adds the prime numbers to the list 
def primeLister(num): 
	for prime in range(2,num): 
		if num  % prime == 0:
			return False
		
	
	list.append(num)
	return True

#creates prime.txt and adds prime numbers to prime.txt from (2,10001)
myFile = open ("prime.txt", "w")
for y in range(2,10001):
	if primeLister(y):
		myFile.write(str(y) + "\n")
#prints the list and closes the file 
print(list)
myFile.close()

