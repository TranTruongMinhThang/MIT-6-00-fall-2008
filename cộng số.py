
vitri = 4
debai = [(4,2),(1,3),(1,5),(5,4),(2,5)]
so_to = 100000000
so_nho = 0.000001
tesst =5
def tinhtrongsoB (vitri,debai):
    print(debai[vitri])
    trongsoB = debai[vitri][0]/debai[vitri][1]
    return trongsoB


def foremannho (debai):
    B = tinhtrongsoB (vitri,debai)
    print('trong so B =', B,'a')
    print(debai)
    dapan = []
    for i in range(0,len(debai)):
        tmp = debai[i][0] + B*debai[i][1]
        dapan.append(tmp)
    print(dapan)
    return dapan

def foremannhotest1 (sodacbiet,debai):
    B = sodacbiet
    print('trong so B =', B,'a')
    dapan = []
    for i in range(0,len(debai)):
        tmp = debai[i][0] + B*debai[i][1]
        dapan.append(tmp)
    print(dapan)
    return dapan

# foremannho (debai)
# foremannhotest1 (so_to, debai)
# foremannhotest1 (so_nho, debai)
foremannhotest1 (tesst, debai)
