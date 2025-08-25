a=[[' ' for i in range(10)]for i in range(10)]
s=3
for i in range(10):
    for j in range(10):
        if(i==0 and j==0):
            a[i][j]=1
        if(i==1 and j<=1):
            a[i][j]=s
            s=s-1
        if(i==2 and j<=2):
            a[i][j]=s+3
            s=s+1
        if(i==3 and j<=3):
            a[i][j]=s+6
            s=s-1
        if(i==4 and j<=3):
            a[i][j]=s+11
            s=s+1
for i in range(10):
    for j in range(10):
        print(a[i][j],end=' ')
    print()
