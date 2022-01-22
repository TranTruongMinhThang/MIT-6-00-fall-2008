def search(s, e):
    answer = None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print(answer, numCompares)

def bsearch(s, e, first, last):
    print(first, last)
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1)
    return bsearch(s, e, mid + 1, last)

def search1(s, e):
    print(bsearch(s, e, 0, len(s)-1))
    print('Search complete')
def testSearch():
    s = range(0,1000000)
    input('basic,-1')
    print(search(s,-1))
    input('basic, -1')
    print(search(s,-1))
    input('basic, end')
    print(search(s, 10000000))

print(bsearch(range(1,10000),3,1,10000))
