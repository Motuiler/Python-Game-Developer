file=open('test.txt','w')
file.write('Hello, My name is Ekaansh?\n') 
file.close()

file=open('test.txt','a')
file.write('How are u?\n')
file.close()

file=open('test.txt','r')
contents=file.read()
file.close()
print(contents)

with open('test.txt','a') as file:
    file.write('I am good!')