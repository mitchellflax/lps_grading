# creates the numbers to test
numL = range(2,10001)
# creates the file to save the prime numbers
File = open('primes.txt','w')
# empty list to print out the prime numbers later
PnumList = []
# loop to test the numbers
for x in numL:
  # keep track of multiples
  ct = 0
  # loop to check for multiples
  for y in range(2, x + 1):
    if x % y == 0:
      ct += 1
  # saves prime numbers to list and file
  if ct == 1:
    PnumList.append(x)
    File.write(str(x) + '\n')
File.close()
# print
print(PnumList)