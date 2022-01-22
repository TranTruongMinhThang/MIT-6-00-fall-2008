from random import seed
from random import randrange
def solve(leg, head):
    for ga in range(0, head+1):
        heo = head - ga
        totlegs = 4*heo + 2*ga
        if totlegs == leg:
            return [heo, ga]
    return [None,None]


def timcapDauChan(a):
    s=[]
    st=[]
    cout = 0;
    while len(s) <= a:
        dau = randrange(100)
        chan = randrange(100)
        d = solve(dau, chan)
        cout += 1;
        if d != [None,None]:
            s.append(d)
            st.append([dau, chan])
    return [s, st]
    
