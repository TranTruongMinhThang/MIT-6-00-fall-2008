# lower = 900
# upper = 1000
# print('Prime numbers between ', lower , 'and', upper, "are:")
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range (2, num):
#             if (num % i) == 0:
#                 break
#         else:
#                 print(num)
def primeNumber(a):
    c = 0
    c_max = a
    arr = []

    for num in range(2, 10000):
        if c < c_max:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                    print(num)
                    arr.append(num)
                    c += 1
    print('prime number is: ',arr[a-1])

print(primeNumber(90))