student1={'math','science','english'}
student2={'science','history','spanish'}

print(student1&student2)

print(student1|student2)

print(student1-student2)
print(student2-student1)

if student1==student2:
    print("The sets are exactly the same!")
else:
    print("The sets are different.")
