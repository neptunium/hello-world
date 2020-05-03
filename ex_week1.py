import math

a1=float(input('Please enter a1: '))
a2=float(input('Please enter a2: '))
b1=float(input('Please enter b1: '))
b2=float(input('Please enter b2: '))


X1=a1*b1+a2*b2

X2a=math.sqrt(a1**2+a2**2)
X2b=math.sqrt(b1**2+b2**2)

costh=X1/(X2a*X2b)

print('costh= ', costh)

goniath=math.degrees(math.acos(costh))

print("goniath= ",goniath, " degrees")
