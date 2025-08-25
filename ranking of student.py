students=[{"Name":"Ram","Marks":[20,30,40]},
{"Name":"Poorna","Marks":[50,60,70]},
{"Name":"Dinesh","Marks":[56,76,96]}]
des=["FIRST","SECOND","THIRD"]
for i in students:
    i["per"]=sum(i["Marks"])//3
res=sorted(students,key=lambda x:x["per"],reverse=True)
for i in range(3):
    print("{} . {}% stands {}".format(res[i]["Name"],res[i]["per"],des[i]))
