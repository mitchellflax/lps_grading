# This is where the code is supposed to start
def primeTime(this, list):
	why = range(1,int(this))
	x = this - 2
	b = 0 
	for num in why:
		yee = int(this) % int(num) 
# Makes sure it is a prime numer or nah 
		if yee != 0:
			b = b + 1
# To continue, the remainder has to be zero 
			if b == x:
				print(this)
				list.append(this)
# Dis is da empty list 
primeList = []
# Has to start from the beginning to the end 
powerRanger = range (2, 10001)
# Prints da numbahs 
for no in powerRanger:
	noot = primeTime(no, primeList)  

