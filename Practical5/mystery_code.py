# What does this piece of code do?
# Answer: Draw a random number between 1 and 100.
              # If the number is bigger than 50, then draw another random number between 1 and 100 until the number is smaller than or equals to 50.
              # Print the number(smaller than or equals to 50).
              # End the instructions.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)
