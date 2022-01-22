# s=[55,56,57,58,59,60,61,62,63,64,65]
# for num in s:
#     for a in range(0, 50):
#         for b in range(0, 50):
#             for c in range(0, 50):
#                 if 6*a+9*b+20*c == num:
#                     print(a, b, c, num)

# s=[]
# f=[]
# x=6
# y=9
# z=30
# k=range(0,50)
# for num in range(0, 50):
#     for a in range(0, 50):
#         for b in range(0, 50):
#             for c in range(0, 50):
#                 if x*a+y*b+z*c == num:
#                     s.append(num)
# news=list(set(s))
# # print(news)
# # print(k)
# # print(list(set(k)-set(news)))
# print(max(list(set(k)-set(news))))

x = int(input('enter your x: '))
y = int(input('enter your y: '))
z = int(input('enter your z: '))

def packages(x,y,z):
    s=[]
    k=range(0,150)
    for num in range(0, 150):
        for a in range(0, 150):
            for b in range(0, 150):
                for c in range(0, 150):
                    if x*a+y*b+z*c == num:
                        s.append(num)
                        print(a,b,c,num)
    news=list(set(s))
    # print(news)
    # print(k)
    # print(list(set(k)-set(news)))
    print(max(list(set(k)-set(news))))

print(packages(x,y,z))