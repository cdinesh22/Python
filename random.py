import random
c=[]
k=5
while len(c)<5:
    b=random.randint(0,10)
    if b in c:
        k=k+1
        continue
    else:
        c.append(b)
print(c)



???? for i in range(k): ?????



ANOTHER WAY



import random
c = []
k = 5
for _ in range(100):   # big enough loop
    if len(c) == k:    # stop once we have k unique numbers
        break
    b = random.randint(1, 11)
    if b not in c:
        c.append(b)
print(c)

