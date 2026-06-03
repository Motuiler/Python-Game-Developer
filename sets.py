numbers=[1,9,2,12,3,23,41,3,4,2]
numset=set(numbers)
print(numset)
print(type(numset))
numset.add(71)
print(numset)
numset.remove(1)
print(numset)
numset.discard(100)
print(numset)

fruits={'orange','apple','banana','lime','pear'}
citrus_fruits={'lemon','lime','orange','grapefruit'}

#Union
print(fruits.union(citrus_fruits))
print(fruits|citrus_fruits)

#Intersection
print(fruits.intersection(citrus_fruits))
print(fruits&citrus_fruits)

#Difference
print(fruits.difference(citrus_fruits))
print(fruits-citrus_fruits)

#Symmetric Difference
print(fruits.symmetric_difference(citrus_fruits))
print(fruits^citrus_fruits)