# def countConstruct (target, wordBank):
#     count = 0
#
#     if target == '' :
#         return 1
#     for word in wordBank:
#         if target[0:len(word)] == word:
#             numWaysForRest = countConstruct(target[len(word):], wordBank)
#             count += numWaysForRest
#
#     return count
#
# print(countConstruct('purple',['purp','p','ur','le','purpl']))
# print(countConstruct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
# print(countConstruct('stakeboard',['bo','rd','ate','t','ska','sk','boar']))
# print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))

smallCatalog = {
    '6.00': (16, 8),
    '1.00': (7, 7),
    '6.01': (5, 3),
    '15.01': (9, 6)
}

del smallCatalog['6.00']
print(smallCatalog)