def nestEggFixed (salary, save, growthRate, years):
    f = []
    for i in range(1,years+1):
        if i == 1:
            a = salary*save*0.01
            f.append(a)

        if i > 1:
            a = a*(1 + 0.01*growthRate) + salary*save*0.01
            f.append(a)
    return f


salary = 1000
save = 100
growthRate = 100
years = 3
print(nestEggFixed (salary, save, growthRate, years))
