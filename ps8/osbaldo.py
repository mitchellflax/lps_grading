#the def function sorts out the variables and will put out all the prime numbers
def isprime(quack, list):
        dank = range(1,int(quack))
        hamham = quack - 2
        yee = 0
        for num in dank:
                oscar = int(quack) % int(num)
                if oscar != 0:
                        yee = yee + 1
                        if yee == hamham:
                                print(quack)
                                list.append(quack)
#This list is where all the prime numbers will go
mortyList = []
#this will tell the program what is the range of numbers it will run
ohJeezList = range(1, 10000)

file = open("prime.txt", "w")
for rick in ohJeezList:
        final = isprime(rick, mortyList)
        file.write(str(mortyList) + "\n")
