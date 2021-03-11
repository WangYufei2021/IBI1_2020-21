# Some simple math
a = 160301
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
print ("d = ", d)
print ("e = ", e)
if d > e:
    print ("d > e")
elif d < e:
    print ("d < e")
else:
    print ("d = e")
    

# Booleans
# either X or Y is true
# Z encodes “(X and not Y) or (Y and not X)
# Prove Z is true
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
print ("When X = False    Y = True     W and Z are the same: ",  W == Z)

X = False 
Y = False
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("When X = False   Y = False     W and Z are the same: ",  W == Z)

X = True
Y = True
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("When X = True     Y = True     W and Z are the same: ",  W == Z)

X = True
Y = False
Z = ( X and not Y) or (Y and not X)
W = X != Y
print ("When X = True    Y = False     W and Z are the same: ",  W == Z)
