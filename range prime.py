a=int(input("Enter lower range:"))
b=int(input("Enter high range:"))
for i in range(a,b+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
