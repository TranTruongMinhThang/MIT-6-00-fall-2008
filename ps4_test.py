# nam = 0
# years = 1
# f = []
# print(range(0,years+1))
# for i in range(0,years+1):
#     nam = nam + i
#     f.append(nam)
#     print(f)
salary = 1000
save = 100
growthRates = [1,100,10]
print(len(growthRates))

f = []
for i in range(0, len(growthRates)):
    if i == 0:
        a = salary * save * 0.01
        f.append(a)

    if i > 0:
        a = a * (1 + 0.01 * growthRates[i]) + salary * save * 0.01
        f.append(a)
print(f)




