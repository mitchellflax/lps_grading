def isOdd(Num):
	if Num % 2 == 0:
		return False 
	if Num % 3 == 0:
		return False
	if Num % 5 == 0:
		return False
	if Num % 7 == 0: 
		return False 
	if Num % 9 == 0:
		return False 
	return True 
prime = []
myFile = open("prime.txt", "w")
for n in range(1,1001):
	p = isOdd(n)
	if p: 
		prime.append(n)
for d in prime: 
	myFile.write(str(d) + "\n")		
print(prime)
myFile.close()
