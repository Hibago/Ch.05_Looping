'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Varun Vepa


 1. Make the following program work.
   '''
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + int(x)
print("The total is:", total)
  
'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    x = i
    print(int(x))

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while i >= 0:
    print(i)
    i -= 1
print("BLAST OFF!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
x = random.randrange(1,11)
print(x)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("Psst.. hey, kid!")
total = 0
poscount = 0
negcount = 0
zerocount = 0
i = 0
for i in range(7):
    number = int(input("Gimme a couple numbers: "))
    total = total + int(number)
    if number > 0:
        poscount += 1
    elif number == 0:
        zerocount += 1
    elif number < 0:
        negcount += 1

print("Your sum is:", total)
print("The amount of positive entries is: ", poscount)
print("The amount of negative entries is: ", negcount)
print("The amount of zero entries is: ", zerocount)
