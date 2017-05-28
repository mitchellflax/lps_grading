def isPrime(myNum, list):
    nums =  range(1, int(myNum))
    range = myNum - 2 
    count = 0 
    for num in nums:
        ranges = int(myNum) % int(num)
        if ranges != 0: 
            count = count + 1 
        if count == range:
            print(myNum)
#this will add the numbers to the list
            list.append(myNum)
#creates an empty list for the numbers that will get put in it
myList = []

oderList = range(1, 10001)
#opens the file primes.txt and writes it out
file = open(" primes.txt","w")

for difnums in oderList:
    final = isPrime(difNums, myNumsList)
    file.write(str(myNumsList)+"/n")

