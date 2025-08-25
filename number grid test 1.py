n=int(input("Enter number of rows: "))
a=[[' ' for _ in range(n)]for _ in range(n)]
num=1
for i in range(n):
    if i%2==0:                              #increasing order
        for j in range(i+1):
            a[i][j]=num
            num+=1
    else:                                   #decreasing order
        for j in range(i,-1,-1):
            a[i][j]=num
            num+=1
for row in a:
    print(*row)
