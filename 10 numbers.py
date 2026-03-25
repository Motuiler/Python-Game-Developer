import random
file=open('numbers.txt','w')
for i in range(10):
    number=random.randint(1,99)
    file.write(str(number)+'\n')
file.close()
total=0
file=open('numbers.txt','r')
for num in file:
    total=total+int(num.strip())
file.close()
print(f'The sum is:',total)