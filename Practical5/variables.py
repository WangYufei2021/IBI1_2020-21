# Some simple math
a = 160301
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
print ("d = ", d)
print ("e = ", e)
print("d >= e? ", d >= e)

# Booleans
X = False 
Y = True
Z = ( X and not Y) or (Y and not X)
print ("X = False   Y = True   Z = ", Z)

X = True 
Y = False
Z = ( X and not Y) or (Y and not X)
print ("X = True    Y = False   Z = ", Z)



# Make a variable W that encodes Zhiwen’s more elegant solution (“X !=Y”)
X = False 
Y = True
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("X = False    Y = True     W = Z? ",  W == Z)

X = False 
Y = False
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("X = False   Y = False     W = Z?",  W == Z)

X = True
Y = True
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("X = True     Y = True     W = Z?",  W == Z)

X = True
Y = False
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("X = True    Y = False     W = Z?",  W == Z)
