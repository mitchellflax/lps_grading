# empty list to add prime numbers
PrimesNumbers = []


# values from 1 to 10000
for aNumbers in range(1, 10001):
        prime = True
# divides all numbers from 1 to 10000 with numbers from 2 to all numbers from 1 to 10000
        for value in range(2,aNumbers):
# if the remainder is 0, then the number is not prime
                if (aNumbers % value == 0):
                        prime = False
# if the number is prime then it is added to an empty list
        if prime:
                PrimesNumbers.append(aNumbers)



# opens a file called prime.txt and allows the program to write into the file
newFile = open("prime.txt", "w")
# puts every number inside the list PrimesNumbers into the file 
for num in PrimesNumbers:
        newFile.write(str(num) + "\n")
# closes the file
newFile.close()
