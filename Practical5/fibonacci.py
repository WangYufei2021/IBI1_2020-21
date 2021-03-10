# Name the first number a and assign it 1
a = 1
# Output the first number
print ("1 place: ",a)

# Name the second number b and assign it 1
b = 1
#  Output the second number 
print ("2 place: ", b)

# Use a for loop to define fibonacci
for i in range (3,14):
# Each number is the sum of the previous two
    c = a + b
# Let the pointer move
    a = b
# Let the latter pointer move
    b = c
    print (i, " place: ", c)
