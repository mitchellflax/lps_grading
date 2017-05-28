# the code starts here
def primeNum(num, list):
        um = range(1,int(num))
        beep = num - 2
        p = 0
        for number in um:
                yeet = int(num) % int(number)
                if yeet != 0:
                        p = p + 1
                        if p == beep:
                                print(num)
                                list.append(num)

# this is the list that will contain the prime numbers 
primeLister = []
# these are the numbers that will be tested 
rangeList = range(2, 100)
# this loop tests the range numbers to see if they're prime        
for pasta in rangeList:
        sp00kegetti = primeNum(pasta, primeLister)

print(primeLister)
