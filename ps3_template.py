from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code
#  target strings

target1 = 'atgacatgcacaagtatgcat'
target = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key = 'atg'
key12 = 'atgc'
key13 = 'atgca'

### ps3b
def subStringMatchExact(target,key):
    arr =[]
    for i in range(len(target)):
        if target[i:i+len(key)] == key:
            arr.append(target.find(key, i))
    return arr

### ps3c
def constrainedMatchPair(match1,match2,L1):
    tup_3c =[]
    for i in range(len(match1)):
        for j in range(len(match2)):
            if match1[i] + L1 + 1 == match2[j]:
                tup_3c.append(match1[i])
    return tup_3c

### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = []
    for miss in range(len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print ('breaking key',key,'into','"',key1,'"','and','"',key2,'"')
        print ('do dai key1:', len(key1))
        print ('do dai key2:', len(key2))
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print ('match1',match1)
        print ('match2',match2)
        print ('possible matches for',key1,key2,'start at',filtered)
    return allAnswers

subStringMatchOneSub(key,target)

    






            



