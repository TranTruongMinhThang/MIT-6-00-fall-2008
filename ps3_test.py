def subStringMatchExact(target,key):
    arr =[]
    for i in range(len(target)):
        if target[i:i+len(key)] == key:
            arr.append(target.find(key, i))
    return arr

def constrainedMatchPair(match1,match2,L1):
    tup_3c =[]
    for i in range(len(match1)):
        for j in range(len(match2)):
            if match1[i] + L1 + 1 == match2[j]:
                tup_3c.append(match1[i])
    return tup_3c

target = 'atgacatgcacaagtatgcat'
key = 'atgc'
key1 = 'a'
key2 = 'gc'
L1 = len(key1)


match1 = subStringMatchExact(target,key1)
match2 = subStringMatchExact(target,key2)


print('match1 = ', match1)
print('match2 = ', match2)

print('ket qua của 3c: ',constrainedMatchPair(match1,match2,L1))