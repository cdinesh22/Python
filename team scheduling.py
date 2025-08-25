import random
a=int(input("Enter the number of teams:"))
teams=[]
for i in range(a):
    b=input("Enter the team name {}:".format(i+1))
    teams.append(b)
c=int(input("Enter the number of time to be matched:"))
matches=[]
for i in range(a-1):
    for j in range(i+1,a):
        for k in range(c):
          matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("MATCH {}.{}-{}".format(i+1,matches[i][0],matches[i][1]))
