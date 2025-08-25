n=int(input("Enter the num:"))
num=[]
num.append(n)
while(n!=1 or n not in num):
    n=sum([int(i)*int(i) for i in str(n)])
    num.append(n)
if(1 in num):
    print(" ROUND TRUE")
else:
    print(" ROUND FALSE")
print(num)
