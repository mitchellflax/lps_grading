# a funtion the determines whether a number is prime
def Prime(myNum):
        for num in range(2,myNum):
               if myNum % num == 0:
                        return False
        return True
# this creates an empty list to add to it 
empty_list = []
# checks which numbers betwen 2 and 10000 is prime or not
for number in range(2,10000):
        # make it a variable
        z = Prime(number)
        # if the number is prime then add it to the list
        if z == True:
                empty_list.append(number)
# this opens a file and add to it
my_file = open("primeNums.txt", "w")
# write empty_list to it
my_file.write(str(empty_list))
# this will close the file
my_file.close()
# this will print out the prime numbers
print("Here are some prime numbers for you guys:")
print(empty_list)

