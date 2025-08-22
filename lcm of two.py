a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
x,y=a,b
while b!= 0:
    rem=a%b
    a=b
    b=rem
lcm=(x*y)
print("LCM:",lcm)
