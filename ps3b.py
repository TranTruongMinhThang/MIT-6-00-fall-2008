def subStringMatchExact(target,key):
    arr =[]
    for i in range(len(target)):
        if target[i:i+len(key)] == key:
            arr.append(target.find(key, i))
    return tuple(arr)


target = 'atgacatgcacaagtatgcat'
key = 'atgc'
key1 = 'a'
key2 = 'gc'

print(subStringMatchExact(target,key2))
print(subStringMatchExact(target,key1))