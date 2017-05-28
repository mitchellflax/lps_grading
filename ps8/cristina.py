# this creates a function that finds out if the number is prime
def Prime(balls, list):
	bear = range(1,int(balls))
	yee = balls - 2
	lol = 0 
# this creates a boolean that says if it is True or False
	for number in bear:
		cool = int(balls) % int(number)
# this proves if it is a prime number or not
		if cool !=0:
			lol = lol + 1
			if lol == yee:
# it prints this if the Remainder is 0
				print(balls)
				list.append(balls)
# creates an empty and a range list
yeehawList = []
rangeList = range(2, 10001)
# this prints out all of the prime numbers from 2-10000
for stop in rangeList:
	bruh = Prime(stop, yeehawList)
