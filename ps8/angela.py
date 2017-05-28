#the def function defines the different variables and will set up how the program will write the prime numbers
def isPrime(myNum, list):
    nums = range(1,int(myNum))
    raange= myNum - 2
    count = 0
    for num in nums:
        ranges = int(myNum) % int(num)
        if ranges != 0:
                count = count + 1
                if count == raange:
                       print(myNum)
                       list.append(myNum)
#the empty is used to put the numbers that are in the range from 1-1001, that are prime
myNumsList = []
#this list is set to tell the program from what range to find the prime numbers
oderList = range(1, 1001)
#this function will open up a txt file and write the prime numbers that are in the range from 1-1001     
file = open("primes.txt","w")
#this argument is for putting the prime numbers in the range into the empty list and writing them into the txt file 
for difnums in oderList:
    final = isPrime(difnums, myNumsList)
    file.write(str(myNumsList)+ "\n")
