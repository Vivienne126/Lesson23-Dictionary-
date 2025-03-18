dic_1={"id1" : {"Name" : "Zoey" , "St" : "Fifth"} , "id2" : {"Name" : "Vivienne" , "St" : "Fourth"} , "id1" : {"Name" : "Zoey" , "St" : "Fifth"}}
dic_2={}
for key,value in dic_1.items():
    if value not in dic_2.values():
        dic_2[key]=value
print(dic_2)