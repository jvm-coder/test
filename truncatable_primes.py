def prime(n):
	flag=True
	if n==1:
		flag= False
	elif n==2:
		flag=True
	else:
		for i in range(2,n):
			if n%i==0:
				flag=False
				break
	return flag
	
p=int(input('ENTER the RANGE : '))
print('Right TRUNCATABLE PRIMES : ')
for num in range(1,p):
	flag=True
	n=num
	for i in range(0,len(str(num))):
		if (not(prime(num))):
			flag=False
			break
		num=num//10
	if flag:
		print(n)
print('LEFT TRUNCATABLE PRIMES : ')	
for i in range(1,p):
	flag=True
	num=i
	if '0' not in str(i):
		s=len(str(i))
		d=10**s
		for j in range(0,s):
			i=i%d
			if not(prime(i)):
				flag=False
				break
			d=d//10
		if flag:
			print(num)	