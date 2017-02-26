ans = int(input("num: "))
res = []


for dig in str(ans):
	res.append(dig)

for index in res:
	index = int(index)

res.sort
print(type(res[0]))
print(res)

yo = 0
for index, dig in enumerate(res):
	yo += int(dig) * 10**index

print(yo)