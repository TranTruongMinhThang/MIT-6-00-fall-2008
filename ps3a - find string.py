
#copy trên mạng
# s = 'arunununghhjj'
# sb = 'nun'
# results = 0
# sub_len = len(sb)
# for i in range(len(s)):
#     if s[i:i+sub_len] == sb:
#         results += 1
# print results

# def count_substring(string, sub_string):
#     return len([i for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string])
#
# string = "atgacatgcacaagtatgcat"
# sub_string = "atgc"
# print(count_substring(string, sub_string))

#Thang viet code dở lần 1
# def countSubStringMatch(target,key):
# #print(target.find(key,6))
# #print(len(target))
#     ss=[]
#     for i in range(len(target)):
#         if target.find(key,i) >= 0:
#             ss.append(target.find(key,i))
#             print('i la: ',i)
#     new_ss=list(set(ss))
#     print('arr la: ',new_ss)
#
# target = "atgacatgcacaagtatgcat"
# key = "atgc"
# countSubStringMatch(target,key)

#Thang viết lần 2 vào thẳng vấn đề học trên mạng
#teration

def countSubStringMatch(target,key):
    count = 0
    for i in range(len(target)):
        if target[i:i+len(key)] == key:
            count +=1

            #print(target.find(key,i))
    print(count)

target = "atgacatgcacaagtatgcat"
key = "atgc"
countSubStringMatch(target,key)

#viết theo kiểu recursion
def countSubStringMatchRecursive(target, key):
        n1 = len(target)
        n2 = len(key)
        if n1 < n2 or n1 == 0:
            return 0
        if target[0:n2] == key:
            return 1 + countSubStringMatchRecursive(target[1:], key)
        else:
            return countSubStringMatchRecursive(target[1:], key)

# target = "atgacatgcacaaatgcgtatgcat"
# key = "at"
# print(countSubStringMatchRecursive(target,key))


# def countSubstrig(str1, str2):
#     n1 = len(str1);
#     n2 = len(str2);
#
#     # Base Case
#     if (n1 == 0 or n1 < n2):
#         return 0;
#
#     # Recursive Case
#     # Checking if the first
#     # substring matches
#     if (str1[0: n2] == str2):
#         return countSubstrig(str1[n2 - 1:],str2) + 1;
#
#     # Otherwise, return the count
#     # from the remaining index
#     return countSubstrig(str1[n2 - 1:],str2);
#
#
# # Driver Code
#
# # str1 = "atgacatgcacaagtatgcat"
# # str2 = "atgc"
#
# # str1 = "geeksfgeeksorgeeks"
# # str2 = "geeks"
# # print(countSubstrig(str1, str2))
# str1 = "hiikanekihiishiishii"
# str2 = "hii"
# print(countSubstrig(str1, str2))