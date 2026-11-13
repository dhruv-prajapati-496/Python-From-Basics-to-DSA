#String and numeric values can operate together with *
A,B = 2,3
txt = "@"
print(2*txt*3)
#String and string can operate with +, it is also known as concatination
C = "2"
print("\n",(C+txt)*B)
#Numeric values can operate with all arithmetic operators
D,E,F = 5,6,4
print(D+E*F) #29
#Arithmetic expressions with integer and float will result in float
X,Y = 5.0,10
Z = X*Y
print(Z)
#Result of Division operator with two integers will be float
P,Q = 1,2
R = P/Q
print(R)
#Integer Division with int and float will give int displayed as float
a,b = 1.5,3
c = a//b
print (c, a/b)
#result of a//b is same as floor(a/b). floor gives closest integer, which is lesser than or equal to the float value

#remainder is negative when denominator is negative
S,T,U,V = -5,2,5,-2
print(S%T)
print(U%T)
print(U%V)

"""This is a Multiline comment"""