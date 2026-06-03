address=('Robert-Schuman','24','York','New York','Grofe','63124')
print(address)
print(type(address))
print(address[2])
for i in range(len(address)):
    print(address[i])
for a in address:
    print(a)

#Unpacking
numbers=(1,2)
n1,n2=numbers
print(n1)
print(n2)

#One Item Tuple
place=('germany',)
print(type(place))

#Tuple without Brackets
nums=5,7,9,11
print(type(nums))
nums.remove(11)