cc={"India":"Delhi","Germany":"Berlin","USA":"Washington","Australia":"Canberra","Russia":"Moscow"}
print(cc)
#Get Keys
print(cc.keys())
#Get Values
print(cc.values())
#Retrieve Value using Key
print(cc["India"])
#Retrieve all Items
for key in cc:
    print(key,cc[key])
#Add Item
cc["China"]="Beijng"
print(cc)
#Update Item
cc["China"]="Beijing"
print(cc)
#Delete Item
del cc["China"]
print(cc)