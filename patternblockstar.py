star=int(input("Enter the number of stars:"))
block=int(input("Enter the number of Blocks:"))
line=int(input("Enter the number of lines:"))
for i in range(block):
    c=0
    for j in range(line-i):
        for k in range(star):
            print("*",end=" ")
            c=c+1
        print()
    print(c)
    print("------------")
