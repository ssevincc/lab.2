b=-8
a=int(input())
x=int(input())
while b<=-4:
    if a<=b:
        z=3*x**2*a-2*b
    else:
        z=6*a*b-3*x
    b=b+0.5
print(z)
