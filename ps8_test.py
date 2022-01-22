smallCatalog = {
    '6.00': (16, 8),
    '1.00': (7, 7),
    '6.01': (5, 3),
    '15.01': (9, 6),
    'th1': (3,5),
    'th2': (2,5),
    'th3': (12,4)
}
maxWork = 15
VALUE , WORK = 0 , 1
def countAdvisor (smallCatalog, maxWork):
    new_smallCatalog = smallCatalog.copy()
    subName = list(new_smallCatalog.keys())
    count = 0
    if maxWork == 0: return 1
    if maxWork < 0: return 0
    if maxWork > 0:
        for i in subName:
                # print(new_smallCatalog[i][WORK])
                new_maxWork = maxWork - new_smallCatalog[i][WORK]
                # print(new_maxWork)
                del new_smallCatalog[i]
                a = countAdvisor( new_smallCatalog , new_maxWork )
                count += a
    return count

def allConstruct  (smallCatalog, maxWork):
    new_smallCatalog = smallCatalog.copy()
    subName = list(new_smallCatalog.keys())
    result = []

    if maxWork == 0: return [[]]
    if maxWork < 0: return []
    if maxWork > 0:
        for i in subName:
            new_maxWork = maxWork - new_smallCatalog[i][WORK]
            if new_maxWork >= 0:

                del new_smallCatalog[i]
                a = allConstruct(new_smallCatalog, new_maxWork)
                b = a
                result.append(c for c in b)

print(allConstruct (smallCatalog, maxWork))
print(countAdvisor (smallCatalog, maxWork))

abc = "1.03,1,32"
ghj = abc.split(",")
map(int, )
print (ghj)
