thing=input()
one="I"
two="M"
three="W"
four="C"
I=0
W=0
M=0
C=0
for char in thing:
    if char==one:
        I+=1
    elif char==two:
        M+=1
    elif char==three:
        W+=1
    else:
        C+=1
if I<2:
    print("I")
elif W<1:
    print("W")
elif M<1:
    print("M")
else:
    print("C")
