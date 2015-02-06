#explain how the str() works
#and code itself

sum = 0

for n in str(2**1000):
	sum = sum + int(n)
	
print(sum)
