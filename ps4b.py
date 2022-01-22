def nestEggVariable(salary, save, preRetireGrowthRates):
    f = []
    for i in range(0, len(preRetireGrowthRates)):
        if i == 0:
            a = salary * save * 0.01
            f.append(a)

        if i > 0:
            a = a * (1 + 0.01 * preRetireGrowthRates[i]) + salary * save * 0.01
            f.append(a)
    return f

def postRetirement(savings, postRetireGrowthRate, expenses):
    postRetire = []
    for i in range(0, len(postRetireGrowthRate)):
        if i == 0:
            b = savings*(1 + 0.01*postRetireGrowthRate[0]) - expenses
            postRetire.append(b)

        if i > 0:
            b = b * (1 + 0.01 * postRetireGrowthRate[i]) - expenses
            postRetire.append(b)
    return postRetire

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRate, epsilon):
    low = 0
    high = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    print('in giá trị cao nhất', high)
    guess_expenses = (low + high)/len(postRetireGrowthRate)
    print('doan',guess_expenses)
    ctr = 0
    while abs(postRetirement(nestEggVariable(salary, save, preRetireGrowthRates)[-1], postRetireGrowthRate, guess_expenses)[-1]) > epsilon and ctr <= 100:
        print('tien con lai:',postRetirement(nestEggVariable(salary, save, preRetireGrowthRates)[-1], postRetireGrowthRate, guess_expenses)[-1])
        if  postRetirement(nestEggVariable(salary, save, preRetireGrowthRates)[-1], postRetireGrowthRate, guess_expenses)[-1] > 0:
            low = guess_expenses
            print('low trong lap',low)
        else:
            high = guess_expenses
            print('high trong lap', high)
        guess_expenses = (low + high)/2
        print('doan trong lap:',guess_expenses)
        ctr +=1
        print(ctr)
    return guess_expenses


salary = 1000
save = 10
preRetireGrowthRates = [1,10,10,10]
postRetireGrowthRate = [100,10,10,100,10,10,15,6,5,7,52]
epsilon = 0.001
# years = 3
savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
expenses = findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRate, epsilon)
print(expenses)

# print('saving là',savings)
print('tien tiết kiệm:',nestEggVariable(salary, save, preRetireGrowthRates))
print('tien de gianh con lai', postRetirement(savings, postRetireGrowthRate, expenses))
# print('tien can tieu:',findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRate, epsilon))
