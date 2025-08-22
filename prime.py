a=int(input("Enter any num:"))
c=0
for i in range(2,a):
    if(a%i==0):
        c=c+1
if(c==0):
    print("PRIME")
else:
    print("Composite")
