from datetime import datetime
a=input("Enter your birthday in (YYYY-MM-DD)")
b=input("Enter your birthday in (YYYY-MM-DD)")
a1=datetime.strptime(a,"%Y-%m-%d")
b1=datetime.strptime(b,"%Y-%m-%d")
print("No of days lived ::",b1-a1)
