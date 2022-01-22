import math
def SumPrimeNumber(a):
    c = 0
    c_max = a
    arr = []
    total = 0
    for num in range(2, 10000):
        if c < c_max:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                #print(num)
                arr.append(num)
                c += 1
                for val in arr:
                    total = total + math.log2(val)
    print('prime number', a, ': ', arr[a-1])
    print('sum of prime numbers from 2nd to', a, 'is: ', total)
    print('ratio total/n: ', total/arr[a-1])
print(SumPrimeNumber(10))
