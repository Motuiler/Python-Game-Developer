temperature=('21','23','27','25','29','24','20','22','26','28')
print(temperature[1:5])
print(max(temperature))
print(min(temperature))
days=0
for i in temperature:
    if int(i)>25:
        days+1
print(days)

templist=list(temperature)
templist.append(30)
print(templist)