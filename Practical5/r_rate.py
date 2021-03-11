# Define r rate as 1.2
r = 1.2

# Define the number at the start
n = 84

# Use for loop to circulate 5 times
for i in range (1,6):

# Each time 1.2 times of the number of the previous infectors will be added, that is n*r
# The total number of infectors is n + n*r
    n = n + n*r 

# Output r and the number of infectors
# r should be described as defined
print("When r(the rate of reproduction of COVID-19) is ",str(r), ", ",  "The total number of individuals infected after 5 generations is ", str(n))
