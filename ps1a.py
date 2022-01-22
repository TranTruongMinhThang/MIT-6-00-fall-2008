# Problem Set 1
 # Name: Thang
 # Collaborators:
 # Time:
 #
# ans = 0
# c = 0
# a = 0
# max_c = 1
# while c < max_c:
#     if a == 1:
#         c += 1
#         ans = a
#         a += 1
#     elif a == 2:
#             c += 1
#             ans = a
#             a += 1
#     elif a == 3:
#                 c += 1
#                 ans = a
#                 a += 1
#     elif a >3 and a < 5 and a%2 == 0:
#                     a += 1
#     elif a == 5:
#                         c += 1
#                         ans = a
#                         a += 1
#     elif a > 5 and a < 7 and a%2 == 0:
#                             a += 1
#     elif a == 7:
#                                 c += 1
#                                 ans = a
#                                 a += 1
#     elif a> 7 and a%2 ==0 and a%3 == 0 and a%5 == 0 and a%7 == 0:
#                                     c +=1
#                                     ans = a
#                                     a += 1
#     else: a +=1
# print(a)
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

print(primeNumber(1000))

