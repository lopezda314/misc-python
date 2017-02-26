import sys


numberPrimes = int(input('How many primes do you want?: '))
ret = []

if numberPrimes <= 0:
	print("Nice try smart guy...")
	sys.exit(-1)

if numberPrimes == 1:
	print([2])
	sys.exit(0)
i = 2
num = 0

while num < numberPrimes:	
	for number in range(2, i+1):
		if i % number == 0:
			if number == i:
				ret.append(i)
				num += 1
				i += 1
				break
			else:
				i += 1
print(ret)
