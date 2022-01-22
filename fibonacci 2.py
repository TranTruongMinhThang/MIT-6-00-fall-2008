# def fib(n):
# 	if n == 0: return 0
# 	if n == 1: return 1
# 	return fib(n-1) + fib(n-2)

def fib2(n):
	n2, n1 = 0, 1
	for i in range(n-2):
		n2, n1 = n1, n1 + n2
		#print(n2,n1)
	return n2+n1

n=2
print(fib2(n))