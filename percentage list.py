a=["RAM","SAHITH","MANISH","MURALI"]
mark=[[21,33,12],[89,33,11],[43,65,76],[33,55,33]]
per=[]
for i in mark:
    per.append(sum(i)//4)
for i in range(len(mark)):
    print("{}.{} got {}%".format(i+1,a[i],per[i]))
